#!/usr/bin/env python3
"""Check the built site (_site/) for problems a visitor would notice.

Errors (exit code 1, fail the PR):
  - internal links or images pointing at files that don't exist
  - same-page links to #anchors that don't exist
  - <img> without an alt attribute
  - pages without exactly one <h1>

With --external, also requests every external link and reports dead ones (404/410, DNS or
connection failures) as GitHub Actions warnings. They never fail the run: external sites go
down, rate-limit, or block bots (ACM, IEEE, LinkedIn), so a human should take a look first.

Usage: python3 scripts/check_site.py [--external] [site_dir]
"""
import concurrent.futures
import html
import os
import pathlib
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

SKIP_PAGES = {"404.html"}  # its links are relative to wherever the visitor got lost
# Hosts that refuse automated requests even when the page is fine
BOT_BLOCKERS = ("linkedin.com", "dl.acm.org", "acm.org", "ieeexplore.ieee.org", "sciencedirect.com",
                "researchgate.net", "mystrikingly.com", "scholar.google.com")
DEAD_STATUSES = {404, 410}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.srcs, self.ids, self.no_alt, self.h1 = [], [], set(), [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("img", "source", "script") and (a.get("src") or a.get("srcset")):
            src = a.get("src") or a["srcset"].split(",")[0].split()[0]
            self.srcs.append(src)
        if tag == "link" and a.get("rel") in ("stylesheet", "icon") and a.get("href"):
            self.srcs.append(a["href"])
        if tag == "img" and "alt" not in a:
            self.no_alt.append(a.get("src") or a.get("data-src") or "?")
        if tag == "h1":
            self.h1 += 1


def target_exists(site, page, url):
    path = url.split("#", 1)[0].split("?", 1)[0]
    if path.startswith("/"):
        base = site / path.lstrip("/")
    else:
        base = page.parent / path
    base = pathlib.Path(os.path.normpath(base))
    # GitHub Pages serves /foo from foo.html and /dir/ from dir/index.html
    return any(p.is_file() for p in (base, base.with_name(base.name + ".html"), base / "index.html"))


def check_external(urls):
    def probe(url):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site link check)"})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return url, r.status
        except urllib.error.HTTPError as e:
            return url, e.code
        except Exception as e:  # DNS, connection refused, timeout
            return url, type(e).__name__

    dead = []
    with concurrent.futures.ThreadPoolExecutor(12) as pool:
        for url, status in pool.map(probe, sorted(urls)):
            if status in DEAD_STATUSES or status in ("URLError", "gaierror"):
                dead.append((url, status))
    return dead


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    external = "--external" in sys.argv
    site = pathlib.Path(args[0] if args else "_site").resolve()
    errors, ext_links = [], {}

    for page in sorted(site.rglob("*.html")):
        rel = page.relative_to(site).as_posix()
        if rel in SKIP_PAGES:
            continue
        p = Page()
        p.feed(page.read_text(errors="replace"))
        if p.h1 != 1:
            errors.append(f"{rel}: has {p.h1} <h1> elements (expected 1)")
        for src in p.no_alt:
            errors.append(f"{rel}: <img src=\"{src}\"> has no alt attribute")
        for url in p.links + p.srcs:
            url = html.unescape(url)
            if url.startswith(("http://", "https://")):
                ext_links.setdefault(url, rel)
                continue
            if url.startswith(("mailto:", "tel:", "javascript:", "data:", "//")):
                continue
            if url.startswith("#"):
                if len(url) > 1 and url[1:] not in p.ids:
                    errors.append(f"{rel}: link to missing anchor {url}")
                continue
            if not target_exists(site, page, url):
                errors.append(f"{rel}: broken internal link {url}")

    errors = list(dict.fromkeys(errors))  # one report per problem, not per occurrence
    for e in errors:
        print(f"::error::{e}")
    print(f"Checked {sum(1 for _ in site.rglob('*.html'))} pages: {len(errors)} error(s).")

    if external:
        urls = {u for u in ext_links if not any(h in u for h in BOT_BLOCKERS)
                and "localhost" not in u and "fonts.g" not in u}
        dead = check_external(urls)
        for url, status in dead:
            print(f"::warning::Dead external link ({status}) on {ext_links[url]}: {url}")
        print(f"Checked {len(urls)} external links: {len(dead)} dead.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
