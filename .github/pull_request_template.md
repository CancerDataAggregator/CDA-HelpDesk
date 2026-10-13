## Release type
<!-- Delete whichever doesn't apply, or keep multiple if this PR is mixed -->
- [ ] Code release (cdapython)
- [ ] Data release (CDA dataset)
- [ ] Maintenance / fix (no new release — bug fix, broken link, styling, nav, typo, etc.)

---

## 🐍 Code release checklist
*(skip this section entirely if this PR is data-only or maintenance-only)*

- [ ] **`docs/_data/release_status.yml`** — update `cdapython_release`:
  - [ ] `date_display` matches the new entry's date in [CHANGELOG.md](https://github.com/CancerDataAggregator/cdapython/blob/develop/CHANGELOG.md)
  - [ ] `highlight` describes the change in plain language (not just copy-pasted changelog shorthand — e.g. turn `v2.2.1: fix help text typo for column_values()` into something a non-engineer skimming the homepage would understand, if the raw line is too terse)
- [ ] **`docs/release_notes/cdapython.md`** — add a new dated entry at the top, matching the existing format (version, API version if relevant, Highlights/Known Issues structure)
- [ ] **Function Reference man pages** (`docs/documentation/cdapython/man_pages/*.md`) — if this release changed any function's parameters, defaults, or return values, update the corresponding page(s). Check:
  - [ ] New or renamed parameters reflected in **SYNOPSIS**
  - [ ] New parameters documented in **ARGUMENTS**
  - [ ] **RETURNS** still accurate
  - [ ] **SEE ALSO** links still correct if any functions were added/removed
- [ ] **Valid `data_source` values** — if this release changed which values are accepted (e.g. a source renamed, like CDS → GC previously, or a new source added), update every man page that lists valid values: `column_values()`, `summarize_subjects()`, `summarize_files()`, `get_subject_data()`, `get_file_data()`
- [ ] **Known Issues sections** — skim `cdapython.md`'s existing Known Issues entries from prior releases; remove/strike any this release actually fixed, so stale "known" issues don't linger indefinitely
- [ ] **Vignette notebooks** — if any vignette's example code uses a function/parameter that changed behavior or was removed, update that notebook (vignettes execute live at build time, so broken calls will fail the build — but silently-changed-meaning calls won't, so a manual skim still matters)

---

## 📦 Data release checklist
*(skip this section entirely if this PR is code-only or maintenance-only)*

- [ ] **`docs/_data/release_status.yml`** — update `cda_data_release`:
  - [ ] `date_display` matches this release's date
  - [ ] `highlight` — only write a real highlight if something is genuinely notable this release (new source added, major version jump, a source removed). For routine refreshes with nothing distinctive, leave empty rather than inventing filler text — the per-source table already shows what changed.
- [ ] **`docs/_data/release_status.yml`** — update the `sources:` list:
  - [ ] Correct `release` version for every data center that changed this cycle
  - [ ] Correct `api` version for every data center that changed this cycle
  - [ ] Correct `extracted` date for every data center that changed this cycle
  - [ ] **New data center added?** Add a full new entry (name, release, api, extracted, link)
  - [ ] **Data center hasn't assigned a version yet** (like CTDC currently) — use `"unassigned"` as the release value, not a guess or placeholder number
- [ ] **`docs/release_notes/data_updates.md`** — add a new dated entry at the top, one bullet per source, matching existing format
- [ ] **New data source added?** — if yes, a few more things need real content, not just data entry:
  - [ ] **`docs/about_us/ourdata.md`** — add a new blurb describing the source, matching the existing per-source structure and tone
  - [ ] **Logo image** — confirm a real logo asset exists for the new source (don't reference a placeholder path; this repo has previously shipped pages referencing logo files that didn't actually exist — check before merging, don't assume)
  - [ ] **`docs/interactive.ipynb`** — the "Data sources" list is a hardcoded markdown list of links; add the new source there too
  - [ ] **Man pages** — see "Valid `data_source` values" above; new sources need to be added to the same set of function docs

---

## 🔧 Maintenance / fix checklist
*(skip this section entirely if this PR is a code or data release with no incidental fixes)*

- [ ] **Describe the actual problem being fixed, not just the symptom.** ("Button 404'd" is a symptom; "`main_cards.md` used an absolute href that skipped RTD's `/en/<version>/` prefix on preview builds" is the problem.) Future-you, or whoever's doing the next sweep like this, benefits far more from the real cause than from "fixed the button."
- [ ] **Check every place the fixed thing is referenced, not just the one you found.** Several past fixes here only patched one of multiple cross-links to the same page (e.g. a changed notebook path referenced from both a card and a video page) — grep for the old path/value site-wide before considering this closed.
- [ ] **If this is a CSS fix:** confirm the exact winning selector via dev tools (Styles panel, not a guess) before writing an override. A plausible-looking selector with lower specificity than the real culprit will silently do nothing — inspect the actual computed styles and match or exceed the real rule's specificity.
- [ ] **If this is a broken-link/path fix:** verify the fix against the real file tree (`ls`/repo browser), not against what a nav config or an old handoff doc *says* the structure should be — those can drift out of sync with what's actually on disk.
- [ ] **If this touches a notebook:** confirm `execute: true` is actually on for the build you're testing against — a notebook can look fine in a build that silently isn't executing it.
- [ ] **If this removes a "draft" / "unverified" marker:** confirm the underlying content was actually run against the live API and confirmed, not just that it reads cleanly. A draft banner should come off *because* it's verified, not because it's inconvenient to leave on.
- [ ] Rebuild and visually confirm the fix on the actual rendered page — not just that the diff looks correct.

---

## ⚠️ Known-incomplete content currently live
*(use this if something shipped to prod before it was fully ready, so it doesn't quietly get forgotten — add a line per item, remove once resolved)*

- [ ] _Example: "What's New" video page is live with a placeholder video embed (`[PLACEHOLDER_VIDEO_ID]`) — real video not yet recorded/uploaded as of this PR._
- [ ]

---

## ✅ Shared checks (any PR type)
- [ ] Vignette notebooks still execute cleanly end-to-end (`mkdocs-jupyter` runs with `execute: true, allow_errors: false`, so a broken call fails the whole build — but confirm locally before pushing, not just hoping CI catches it)
- [ ] Spot-check vignette **prose** against freshly-executed counts — numbers are always live at build time, but if a count shifted a lot (e.g. a new source adding thousands of subjects), the surrounding narrative sentences that reference specific old numbers may now read oddly and could use a rewrite, not just a number swap
- [ ] Homepage (`docs/index.md`) renders both release cards correctly after any YAML changes — check locally, don't assume the macro handled missing/malformed fields gracefully
- [ ] No dead links introduced (new source links, new changelog links, path changes from a fix, etc.)
