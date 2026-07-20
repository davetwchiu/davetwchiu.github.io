from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))

class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.titles = 0
        self.h1 = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "title": self.titles += 1
        if tag == "h1": self.h1 += 1

errors: list[str] = []
for file in HTML_FILES:
    text = file.read_text(encoding="utf-8")
    parser = Parser(); parser.feed(text)
    if parser.titles != 1: errors.append(f"{file.name}: expected one title")
    if parser.h1 != 1: errors.append(f"{file.name}: expected one h1")
    if re.search(r"Reservation Number|Confirmation #|25210885", text, re.I):
        errors.append(f"{file.name}: sensitive reservation data found")
    for href in parser.links:
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = href.split("#", 1)[0]
        if target and not (ROOT / target).exists():
            errors.append(f"{file.name}: broken local link {href}")

required = {"index.html","daily.html","culture.html","museums.html","food.html","maps.html"}
missing = required - {f.name for f in HTML_FILES}
if missing: errors.append(f"missing pages: {sorted(missing)}")
if not (ROOT / "assets/style.css").exists(): errors.append("missing stylesheet")
if not (ROOT / "assets/app.js").exists(): errors.append("missing script")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)
print(f"VALIDATION OK: {len(HTML_FILES)} pages, no broken local links or sensitive reservation data")
