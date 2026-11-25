#!/usr/bin/env python3
"""Collect the icons the site uses and save their SVG shapes to _data/icons.json.

The site doesn't load an icon font. Templates keep writing icons the familiar way,
e.g. <i class="fas fa-trophy"></i>, and _plugins/inline_icons.rb swaps each one for a
small inline SVG at build time, using the shapes stored in _data/icons.json.

Run this after adding an icon the site hasn't used before (the build fails and names it):
    python3 scripts/fetch_icons.py

Sources: Font Awesome Free 6.5.1 (icons CC BY 4.0) and Academicons 1.9.1 (SIL OFL 1.1).
"""
import json
import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "icons.json"
SCAN = ["_includes", "_layouts", "_data", "_showcase", "_news", "_publications", "_posts",
        "assets/js"]
FA = "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/svgs/{}/{}.svg"
AI = "https://cdn.jsdelivr.net/npm/academicons@1.9.1/svg/{}.svg"
SETS = {"fas": "solid", "fa-solid": "solid", "far": "regular", "fa-regular": "regular",
        "fab": "brands", "fa-brands": "brands", "ai": "ai"}
# Font Awesome 5 names still used in the templates -> their Font Awesome 6 file names
ALIASES = {
    "project-diagram": "diagram-project", "hands-helping": "handshake-angle",
    "external-link-alt": "up-right-from-square", "check-circle": "circle-check",
    "file-alt": "file-lines", "calendar-alt": "calendar-days", "angle-double-right": "angles-right",
    "exclamation-triangle": "triangle-exclamation",
}
ICON = re.compile(r"\b(fas|far|fab|fa-solid|fa-regular|fa-brands|ai)\s+(?:fa|ai)-([a-z0-9-]+)")
SHAPES = {"path": ("d",), "circle": ("cx", "cy", "r"), "rect": ("x", "y", "width", "height", "rx"),
          "polygon": ("points",), "ellipse": ("cx", "cy", "rx", "ry")}


def used_icons():
    files = [p for d in SCAN for p in (ROOT / d).rglob("*") if p.is_file()]
    files += list(ROOT.glob("*.html"))
    found = set()
    for f in files:
        if f.suffix not in (".html", ".md", ".yml", ".js"):
            continue
        for prefix, name in ICON.findall(f.read_text(errors="replace")):
            found.add(f"{SETS[prefix]}/{name}")
    return sorted(found)


def fetch(key):
    family, name = key.split("/")
    real = ALIASES.get(name, name)
    url = AI.format(real) if family == "ai" else FA.format(family, real)
    req = urllib.request.Request(url, headers={"User-Agent": "icon-fetch"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
    # Keep only the shapes: Academicons files also carry Inkscape metadata and titles
    shapes = []
    for parent in root.iter():
        if parent.get("transform") and parent is not root:
            raise SystemExit(f"{url}: transformed group, not supported")
        for el in parent:
            tag = el.tag.split("}")[-1]
            if tag in SHAPES:
                attrs = " ".join(f'{a}="{el.get(a)}"' for a in SHAPES[tag] if el.get(a) is not None)
                shapes.append(f"<{tag} {attrs}/>")
    if not shapes:
        raise SystemExit(f"{url}: no shapes found")
    return {"viewBox": root.get("viewBox"), "body": "".join(shapes)}


def main():
    have = json.loads(OUT.read_text()) if OUT.exists() else {}
    need = used_icons()
    icons = {k: have[k] if k in have else fetch(k) for k in need}
    added = [k for k in need if k not in have]
    dropped = [k for k in have if k not in icons]
    OUT.write_text(json.dumps(icons, indent=1, sort_keys=True) + "\n")
    print(f"{len(icons)} icons in {OUT.relative_to(ROOT)}"
          f" (added {len(added)}: {', '.join(added) or '-'}; dropped {len(dropped)}: {', '.join(dropped) or '-'})")


if __name__ == "__main__":
    main()
