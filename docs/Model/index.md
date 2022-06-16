---
title: CDA model
---

The CDA uses a simple model to describe connections between metadata fields. Contents for the metadata fields are taken directly from our data partners and made searchable without transformation or harmonization.

The CDA model is broken into two data schemas to support our six search endpoints. Searches on the `subject`, `researchsubject`, `diagnosis`, `treatment` and `specimen` endpoints use the  Subject Schema. We provide both a user friendly table of [subject fields](subjecttable.md) and the full [subject schema JSON](./subjects_schema.md).

The `file` endpoint uses a file attributes first schema to enable faster search on this much larger dataset. View the [file schema JSON](./files_schema.md) or [file fields table](filetable.md) for more information.

This simplified ER diagram shows the CDA endpoints, and what metadata is directly associated with each.

<div class="container" markdown>

<img src="./cdamodel.png" class="img-fluid" alt="Responsive image">

</div>
