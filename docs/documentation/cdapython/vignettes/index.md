---
title: Vignette Conceptual Overview
---

# Vignette Conceptual Overview

*(Placeholder for the minimal build. The real page explains the spreadsheet metaphor, tables, columns, and endpoints before diving into individual vignettes.)*

This minimal build includes 5 standalone vignettes, each built around a different starting point for the same underlying question -- "is there already data about X?":

1. [Is there anything about X?](01_global_search.ipynb) -- a bare-term global search *(verified against live data)*
2. [Getting oriented before I filter](02_systematic_browsing.ipynb) -- browsing tables/columns/values deliberately before committing to a query *(verified against live data)*
3. [I have subjects, what else exists](03_match_from_file.ipynb) -- checking a list of subjects you already have, using the file you already have *(structure verified, counts pending)*
4. [Reassembling a scattered project](04_cptac_reassembly.ipynb) -- finding every piece of a known project (like CPTAC) that got split across data centers *(structure verified, counts pending)*
5. [Patients with multiple data types](05_multimodal_patients.ipynb) -- finding subjects who have two or more kinds of data for the same condition *(structure verified, counts pending)*

Worth knowing as you read these: only `anatomic_site` and `disease` currently have true ontology-backed rollup behavior in CDA (UBERON and ICD-O-3, respectively) -- those are the only fields where `add_extras` will show something meaningfully new. Most other harmonized fields are fully standardized but conceptually flat (no hierarchy to roll up through, e.g. `sex`, `species`); a handful of fields aren't harmonized yet at all (`stage`, `treatment_type`, and others). Full harmonization status and mappings are public at the [harmonization reference repo](https://github.com/CancerDataAggregator/harmonization_reference/tree/main/value_maps_by_concept).

See also the [visual vignette index prototype](../../../prototypes/vignette_index.html).
