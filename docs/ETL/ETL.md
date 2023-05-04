# ETL

## Overview of Extraction Transfer and Load (ETL)

CDA extracts essential research metadata from public APIs at three CRDC Data Commons:
GDC (via their REST API), PDC (via their GraphQL API) and IDC (via the Google BigQuery API).
Incoming metadata is mapped from each DC's data model to CDA's harmonized search model,
and a small amount of harmonizing transformation is conservatively applied to values from
select fields during ingest processing. Current examples of these transformations include
replacing the phrase "Not reported" with a null value (only in cases where that doesn't
lead to loss of usable data) and adding "Homo sapiens" to IDC Patient record metadata
for all records where that's known implicitly to be the default species, despite a lack
of explicit documentation in the source data.

Whenever possible during ingest processing, clinical metadata describing a single subject,
but deriving from multiple records coming from multiple DCs, is merged into a single
aggregated CDA record describing that subject, which retains provenance details indicating
the original DC records from which its data was extracted and aggregated.

Code and accompanying documents [can be found on our github](https://github.com/CancerDataAggregator/transform)

# Data sources

CDA currently collects data from 3 sources:

- [GDC](https://portal.gdc.cancer.gov/)
- [PDC](https://pdc.cancer.gov/pdc/)
- [IDC](https://portal.imaging.datacommons.cancer.gov/)



## Near future enhancements

- CDA to add CRDC CDS as a data source
- Harmonization and QC transformations on incoming data to be expanded (policies to be developed in close coordination with CRDC DSS)
- CDA to begin merging specimen metadata across multiple DCs, as is currently done with subjects
- CDA model upgrades (to be developed in close coordination with CRDC DSS)
