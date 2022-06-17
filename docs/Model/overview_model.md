---
title: CDA Model Overview
---

The CDA uses a simple model to describe connections between metadata fields. Contents for the metadata fields are taken directly from our data partners and made searchable without transformation or harmonization.

The CDA model is broken into two data schemas to support our six search endpoints. Searches on the `subject`, `researchsubject`, `diagnosis`, `treatment` and `specimen` endpoints use the  Subject Schema. We provide both a user friendly table of [subject fields](fields_subject.md) and the full [subject schema JSON](./schema_subject.md).

The `file` endpoint uses a file attributes first schema to enable faster search on this much larger dataset. View the [file schema JSON](./schema_file.md) or [file fields table](fields_file.md) for more information.

This simplified ER diagram shows the CDA endpoints, and what metadata is directly associated with each.

<div class="container" markdown>

<img src="../images/cdamodel.png" class="img-fluid" alt="Responsive image">

</div>
