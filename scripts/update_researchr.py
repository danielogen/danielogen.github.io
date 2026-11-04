#!/usr/bin/env python3
"""Sync conference committee service from the public researchr profile.

Writes:
  _data/committees.yml  one entry per "Member of Committee" contribution, newest first

Authored papers on the profile are ignored (they come from Google Scholar). Venue short and
full names come from VENUES below; a series not listed there falls back to the name researchr
shows. If the page cannot be fetched or no committees are found, the file is left untouched.
"""
import html
import json
import pathlib
import re
import sys
import urllib.request

PROFILE_URL = "https://conf.researchr.org/profile/conf/danielogenrwot"
OUT = pathlib.Path(__file__).resolve().parent.parent / "_data" / "committees.yml"

# researchr series heading -> (short name, full name)
VENUES = {
    "Mining Software Repositories": ("MSR", "International Conference on Mining Software Repositories"),
    "MSR": ("MSR", "International Conference on Mining Software Repositories"),
    "ASE": ("ASE", "IEEE/ACM International Conference on Automated Software Engineering"),
    "ISSTA": ("ISSTA", "ACM SIGSOFT International Symposium on Software Testing and Analysis"),
    "ICSME": ("ICSME", "IEEE International Conference on Software Maintenance and Evolution"),
    "ESEC/FSE": ("ESEC/FSE", "ACM International Conference on the Foundations of Software Engineering"),
    "FSE": ("ESEC/FSE", "ACM International Conference on the Foundations of Software Engineering"),
    "ICSE": ("ICSE", "IEEE/ACM International Conference on Software Engineering"),
    "AIware": ("AIware", "ACM International Conference on AI-powered Software"),
    "SCAM": ("SCAM", "IEEE International Conference on Source Code Analysis and Manipulation"),
    "SANER": ("SANER", "IEEE International Conference on Software Analysis, Evolution and Reengineering"),
    "ICPC": ("ICPC", "IEEE/ACM International Conference on Program Comprehension"),
    "ESEM": ("ESEM", "ACM/IEEE International Symposium on Empirical Software Engineering and Measurement"),
    "EASE": ("EASE", "International Conference on Evaluation and Assessment in Software Engineering"),
}
SMALL_WORDS = {"and", "or", "of", "the", "in", "on", "for", "to", "a", "an"}


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; danielogen.github.io researchr sync)",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def text(fragment):
    return html.unescape(re.sub(r"<.*?>", "", fragment)).strip()


def title_case(s):
    # researchr capitalises tracks inconsistently ("Artifact evaluation" vs "Artifact Evaluation").
    words = s.split()
    return " ".join(w if (i and w.lower() in SMALL_WORDS) or not w[:1].islower() else w[:1].upper() + w[1:]
                    for i, w in enumerate(words))


def q(value):
    # JSON strings are valid double-quoted YAML scalars.
    return json.dumps(value, ensure_ascii=False)


def parse(page):
    entries = []
    timeline = page.split('id="contributions-timeline"', 1)[-1]
    for year_block in re.split(r'<div class="contribution-year">', timeline)[1:]:
        year = re.search(r"<h3>(\d{4})</h3>", year_block)
        if not year:
            continue
        for series_block in re.split(r"<h4>", year_block)[1:]:
            series = text(series_block.split("</h4>", 1)[0])
            for li in re.findall(r"<li>(.*?)</li>", series_block, re.S):
                if 'title="Member of Committee"' not in li:
                    continue
                link = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', li, re.S)
                if not link:
                    continue
                # e.g. "Committee Member in Artifact Evaluation Committee within the Artifact Evaluation-track"
                m = re.match(r"(.+?) in (.+?) within the (.+?)-track$", text(link.group(2)))
                if not m:
                    continue
                role, committee, track = m.groups()
                kind = ("jpc" if "junior" in (committee + track).lower()
                        else "aec" if "artifact" in (committee + track).lower() else "pc")
                if kind == "jpc":
                    track = committee.split(" - ")[0]
                    role = "Junior PC Member" if role == "PC Member" else role
                short, full = VENUES.get(series, (series, series))
                entries.append({
                    "venue": f"{short} {year.group(1)}",
                    "full_name": full,
                    "role": role,
                    "track": title_case(track),
                    "kind": kind,
                    "year": int(year.group(1)),
                    "url": html.unescape(link.group(1)),
                })
    return entries


def main():
    try:
        page = fetch(PROFILE_URL)
    except Exception as exc:  # network error or block: keep last data
        print(f"researchr fetch failed ({exc}); keeping existing data")
        return 0
    entries = parse(page)
    if not entries:
        print("No committee entries found (layout change?); keeping existing data")
        return 0

    lines = [f"# Generated by scripts/update_researchr.py from {PROFILE_URL}",
             "# Do not edit by hand: changes are overwritten on the next sync. Fix venue names in VENUES there.",
             "# `kind` is one of: pc (program committee), aec (artifact evaluation committee), jpc (junior PC)"]
    for e in entries:
        lines.append(f"- venue: {q(e['venue'])}")
        for key in ("full_name", "role", "track", "kind", "year", "url"):
            lines.append(f"  {key}: {e[key] if key == 'year' else q(e[key])}")
    content = "\n".join(lines) + "\n"
    if OUT.exists() and OUT.read_text() == content:
        print(f"{len(entries)} committee entries, no changes")
    else:
        OUT.write_text(content)
        print(f"Wrote {len(entries)} committee entries to {OUT.relative_to(OUT.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
