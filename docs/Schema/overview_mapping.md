---
title: Mapping Overview
comments: true
---

CDA currently collects data from three data sources:

- [The Genomic Data Commons (GDC)](https://portal.gdc.cancer.gov/)
- [The Proteomic Data Commons (PDC)](https://pdc.cancer.gov/pdc/)
- [The Imaging Data Commons (IDC)](https://portal.imaging.datacommons.cancer.gov/)


The CDA uses a simple model to describe common data descriptors and the connections between them. Contents for the metadata fields are taken directly from the data sources and made searchable without transformation or harmonization. See individual breakouts of the tables below under Mapping in the left side bar.

All GDC, PDC, and IDC field names use a 'dot' notation to specify the paths. The first word denotes the endpoints that the field is taken from, such as "file(s)" or "case(s)". The rest of the field name is as seen in GDC and PDC documentation for those endpoints. Since we extract all IDC data from one pivot table which is written oriented around files, we use "files" as the endpoint for all fields from IDC.

Mutations are not yet harmonized to our other endpoints.
