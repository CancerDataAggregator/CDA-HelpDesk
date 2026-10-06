---
title: Prototypes
---

# Prototypes

These are standalone HTML mockups, not yet converted into the site's actual theme. Included here as static pages for preview during this minimal RTD test build.

- [Landing page / audience router](landing_page.html)
- [Dropdown query prototype](dropdown_query.html)
- [Vignette index (card-grid directory, matches the 5 current vignettes)](vignette_index.html)

Note: the dropdown query prototype makes live `fetch()` calls to the CDA API and is
**confirmed still broken** in production testing — CORS/"Failed to fetch" error, even
with RTD's domain allow-listed on the API side. Root cause appears to be an additional
firewall layer, not just a missing CORS header. Not fixable from the HTML/JS side —
deferred until resolved by whoever controls that firewall layer.
