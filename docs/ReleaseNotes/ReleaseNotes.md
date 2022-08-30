
CDA python has a new release the ~second week of each month


## Release 3.1-beta

Available September 2022. We recommend updating to take advantage of improvements to our query language

The beta 3.1 release of CDA now includes search for a limited set of genes.

## Datasets & Fields

* All datasets updated as follows
    * GDC: 
    * PDC: [^1]
    * IDC: 

[^1]:Information pulled from the PDC API may contain embargoed data.

## Enhanced query functionality

- Searches no longer require full path names for columns, e.g. 'ResearchSubject.Diagnosis.Treatment.treatment_anatomic_site' is now 'treatment_anatomic_site'
- 'id' columns have been made unique, e.g. ''ResearchSubject.Diagnosis.Treatment.id' is now 'treatment_id'
- New `join_as_str` function allows users to use results from one Q search as input to another
- New option for `filter` allows users to dynamically rename columns in search results
- New `auto_paginator` function has been added that does not require the user to loop through results
- `paginator` and `auto_paginator` now display a progress bar 
- Query return details has been simplified
- `to_list` can now do both fuzzy and exact matching
- `unique_terms` can now optionally show counts of term usage
- `columns` can now display descriptions
- Code optimization to improve search speed and performance

## Metadata Changes

* See [CDA Schema Field Mapping](../Schema/overview_mapping.md)

## Bug fixes

- Files associated with cancer or normal tissue specimens are now properly attributed as cancer or normal
- `filters` option in `to_list` function is now case-insensitive
- Various error message and handling improvements


## Known bugs and issues - these will be fixed in an upcoming release

- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- math is broken?

# Previous Versions


## Release 3.0-beta

Available as of 7/11/22

The beta 3.0 release of CDA searches across data from the Genomics Data Commons (GDC), the Proteomics Data Commons (PDC), and the Imaging Data Commons (IDC) to aggregate and return data to users via a single application programming interface (API).

## Datasets & Fields

* All datasets updated as follows
    * GDC: v33.1, 06/23/2022
    * PDC: v2.7, 06/23/2022[^1]
    * IDC: v.9.0, 06/24/2022

[^1]:Information pulled from the PDC API may contain embargoed data.

## Enhanced query functionality

* Added support for the following SQL operators: IN, LIKE, NOT IN, IS NOT, IS
* Q now comes with a better query parser that allows for writing full AND/OR logic into a single Q object
    - Example: `Q("ResearchSubject.primary_diagnosis_site = 'kidney' AND ResearchSubject.Diagnosis.stage = 'Stage II')`
* Methods for data retrieval were split into multiple entities as opposed to returning one large nested structure
    - To support this, method chaining was added to allow for querying each of the specific entities (e.g. `Q('[query here]').subject.run()`)
    - Entities supported: `subject`, `researchsubject`, `specimen`, `diagnosis`, `treatment`, `file`
    - Along with this also comes files and counts for each entity (e.g. `subject.file`, `subject.count`)
* Counts functionality added, giving total counts for entities and per DCC depending on usage
    - `Q("ResearchSubject.primary_diagnosis_site = 'kidney'").count.run()` would return total counts for each entity and DCC
    - `Q("ResearchSubject.primary_diagnosis_site = 'kidney'").subject.count.run()` would give a more generalized breakdown of specific fields in subject (e.g. number of records per distinct value for `sex`, `ethnicity`, `cause_of_death` or `identifier.system`)
    - `Q("ResearchSubject.primary_diagnosis_site = 'kidney'").subject.file.count.run()` would give a breakdown of distinct fields for subject files such as `data_type` or `file_format`
* Filter flag added to Q's run method which allows horizontal filtering of results
* Verbose flag added to Q's run method to hide/show Q actions when running a query
* Queries on text fields are now case insensitive
* Added to_dataframe to Q's Result object that converts the JSON structure to a pandas dataframe
* Added paginator to Q's Result object that allows for pagination through result pages. This also has a flag for paginating as a dataframe.
* Added table formatting to count results objects for easier reading


## Metadata Changes

* See [CDA Schema Field Mapping](../Schema/overview_mapping.md)

* Summary
    * Previous table format now called Subjects endpoint
        * Replaced all File entities with Files - a list of file ids associated with the entity that the list is located in. e.g
            * File -> Files
            * ResearchSubject.File -> ResearchSubject.Files
            * ResearchSubject.Specimen.File -> ResearchSubject.Specimen.Files
    * Files endpoint added:
        * Endpoint oriented around File information
        * Includes all information regarding the file's associated entities(Subject, ResearchSubject, and Specimen)
    * Newly available fields:
        * vital_status
        * days_to_death
        * cause_of_death
        * ResearchSubject.Diagnosis.morphology
        * ResearchSubject.Diagnosis.method_of_diagnosis
        * File.data_modality
        * File.dbgap_accession_number
        * File.imaging_modality
        * File.imaging_series
        * ResearchSubject.Diagnosis.Treatment.therapeutic_agent
        * ResearchSubject.Diagnosis.Treatment.treatment_anatomic_site
        * ResearchSubject.Diagnosis.Treatment.treatment_effect
        * ResearchSubject.Diagnosis.Treatment.treatment_end_reason
        * ResearchSubject.Diagnosis.Treatment.number_of_cycles
    * Renamed fields (old -> new):
        * ResearchSubject.associated_project -> ResearchSubject.member_of_research_project
        * ResearchSubject.primary_disease_site -> ResearchSubject.primary_diagnosis_site
        * ResearchSubject.primary_disease_type -> ResearchSubject.primary_disease_type
        * ResearchSubject.Specimen.age_at_collection -> ResearchSubject.Specimen.days_to_collection


## Bug fixes

* Fixed issue where queries on list columns that were not lists of json objects (i.e. subject_associated_project) would fail
* Fixed issue where integer fields were being returned as strings


## Known bugs and issues - these will be fixed in an upcoming release

* `unique_terms` are not sorted when they return
* tumor stages are not harmonized, there are redundant terms (complicates query)
* Days_to_birth should be reformatted (currently negative) or have an example query
* Docker jupyter notebook does not work if a notebook is already open in port 8888
* Searches on the subject endpoint incorrectly count files. Please use the file counts for the same query from the files endpoint
* Some PDC files are incorrectly labeled at the specimen level, for e.g. a file may be inappropriately labeled as both cancer and normal.

## 2.X

Version 3.0 is a full rewrite of our code and older versions of cda-python are no longer maintained or supported.
If you'd like to see how the project has evolved, you can still access the their documentation here:

- [2.0](https://cda.readthedocs.io/en/2.0/ReleaseNotes.html)
- [2.1](https://cda.readthedocs.io/en/2.1/ReleaseNotes.html)

<!-- Footnotes themselves at the bottom. -->
