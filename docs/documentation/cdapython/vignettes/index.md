---
title: Vignette Conceptual Overview
---

# Vignette Conceptual Overview

You can think of the CDA as a really, really enormous spreadsheet full of data. To search this enormous spreadsheet, you'd want to select columns that have data you're interested in, and then filter the rows to only the values you care about.

CDA makes this data searchable in two main endpoints:

- **subject:** a patient entity capturing the study-independent metadata for research subjects. Human research subjects are usually not traceable to a particular person, to protect their privacy.
- **file:** a unit of data about subjects, research subjects, specimens, or their associated information.

If you're looking to build a cohort of distinct individuals who meet some criteria, you'd search using `get_subject_data`, which returns a table with one row per subject -- then use the `add_columns` parameter inside `get_subject_data` to pull in extra information per subject (file details, treatment history, whatever's relevant to what you're building).

## The five vignettes

This minimal build includes 5 standalone vignettes, each built around a different starting point for the same underlying question -- "is there already data about X?":

1. [Is there anything about X?](01_global_search.ipynb) -- a bare-term global search *(verified against live data)*
2. [Getting oriented before I filter](02_systematic_browsing.ipynb) -- browsing tables/columns/values deliberately before committing to a query *(verified against live data)*
3. [I have subjects, what else exists](03_match_from_file.ipynb) -- checking a real GDC case export against what else CDA knows, matching on native `upstream_id`s
4. [Reassembling a scattered project](04_cptac_reassembly.ipynb) -- finding every piece of a known project (like CPTAC) that got split across data centers *(verified against live data)*
5. [Subjects with multiple data types](05_multimodal_patients.ipynb) -- finding subjects who have two or more kinds of data for the same condition

## A note on harmonization and ontologies

Worth knowing as you read these: only `anatomic_site` and `disease` currently have true ontology-backed rollup behavior in CDA (UBERON and ICD-O-3, respectively) -- those are the only fields where `add_extras` will show something meaningfully new. Most other harmonized fields are fully standardized but conceptually flat (no hierarchy to roll up through, e.g. `sex`, `species`); a handful of fields aren't harmonized yet at all (`stage`, `treatment_type`, and others). Full harmonization status and mappings are public at the [harmonization reference repo](https://github.com/CancerDataAggregator/harmonization_reference/tree/main/value_maps_by_concept).

See also the [visual vignette index prototype](../../../prototypes/vignette_index.html).
