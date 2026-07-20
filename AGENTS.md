# AGENTS.md

## Purpose
Maintain a static, mobile-first travel website for the 2026 Osaka-based late-summer trip.

## Source of truth
- Structured itinerary: `data/itinerary.json`
- Generated pages: root `*.html`
- Do not expose reservation numbers, confirmation numbers, personal names, or private calendar URLs.

## Controlled execution loop
For every substantial change:
1. Inspect the current data, generated pages, and affected links.
2. State machine-checkable acceptance criteria.
3. Update the structured data or templates; do not hand-edit generated HTML unless repairing the generator.
4. Run `python3 scripts/build.py`.
5. Run targeted checks, then `python3 scripts/validate_site.py`.
6. Review the diff for factual drift, privacy leaks, broken links, mobile regressions, and duplicated text.
7. Repair and re-test. Stop after three no-progress repair cycles and report the exact blocker.

## Content rules
- Traditional Chinese, with Japanese names retained where useful.
- Prefer official venue sources for hours, closures, exhibitions, and route restrictions.
- Mark time-sensitive facts with the verification date.
- Preserve meal and museum buffers; do not silently compress the itinerary.

## Completion evidence
Report changed files, validation output, branch/commit/PR, and any unresolved time-sensitive facts.
