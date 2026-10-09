---
title:  cdapython releases
status: new
---

# Public releases

## Available October 1, 2026

cdapython version 2.2.1

### Highlights

- Fixed a typo in the help text for `column_values()`. No functional change — this release only corrects documentation shown when you run `help(column_values)`.

---

## Available August 25, 2026

cdapython version 2.2.0

### Highlights

Added support for retrieving harmonized controlled-vocabulary metadata alongside your search results — specifically synonym terms, ontology "slim" terms, and containing terms. This builds on the `add_extras` option already available in `get_subject_data()`, `get_file_data()`, `summarize_subjects()`, and `summarize_files()`: previously `add_extras` could show you *that* a value matched through harmonization, and now it can also show you the specific synonym, slim, or containing terms involved.

See the help text for the `add_extras` parameter in any of those four functions for the full list of accepted values.

## Available December 9, 2025

cdapython version 2.0.14

### Highlights

Added an early, experimental ("proof-of-concept") `include_disease_slims` option to `get_subject_data()` / `get_file_data()`, with a same-day follow-up fix to sort the returned `disease_slims` column consistently.

**Note:** this proof-of-concept was later superseded — see the April 7, 2026 entry above, where full `search_terms` support replaced it.

---

## Available October 31, 2025

cdapython version 2.0.12

### Highlights

- Standardized internal debug logging for generated SQL queries
- Fixed `column_values()` to handle a few known edge cases in its input more gracefully

---

## Available October 27, 2025

cdapython version 2.0.10

### Highlights

- `column_values()` parameter validation now shares the same validation logic used elsewhere in the library, for more consistent error messages
- `column_values(data_source=...)` now accepts a list of sources, not just a single source string
- Same-day follow-up fix for an issue introduced by the above change

---

## Available October 22, 2025

cdapython version 2.0.9

### Highlights

- Internal cleanup to how `column_values()` checks its `data_source` argument (no user-facing behavior change)

---

## Available October 20, 2025

cdapython version 2.0.8

### Highlights

**Breaking change:** `CDS` has been renamed to `GC` as a `data_source` value throughout cdapython. If your code passes `data_source='CDS'` to any function, update it to `data_source='GC'`.

---

## Available October 8, 2025

cdapython version 2.0.7

### Highlights

- Fixed an issue with column metadata lookup inside `get_subject_data()` / `get_file_data()` when using `collate_results=True`

---

## Available September 17, 2025

cdapython version 2.0.6

### Highlights

- Expanded support for numeric range filters (e.g. `60 < age_at_observation <= 70`) to match the latest API syntax

---

## Available August 18, 2025

cdapython version 2.0.0

### Highlights

- Initial public release of `cdapython` on PyPI
- 2.0.1: corrected the default API URL
- 2.0.2: updated a build dependency (PyYAML) — no user-facing change
## Available April 7, 2026

cdapython version 2.1.0
Global keyword search is now available on 'summarize_subjects', 'summarize_files', 'get_subject_data',
and 'get_file_data'. See `documentation/cdapython/vignettes/01_global_search.ipynb`

## Available August 18, 2025

New API: Streamlined, object-based query API that supports complex filter sets
Improved cdapython with easier to read, subject and file based results tables, more intuitive query language, and support for joining data across multiple results

`cdapython` is now available on PyPI -- install with `pip install cdapython` instead of installing from GitHub.

### Known Issues

- `upstream_source` results are incorrectly linking some records. We recommend not using this field until the fix is implemented in our next code release


## Available July 16, 2024

cdapython version 2024.1.4
API version 2024.1.2

### Highlights:

- Hotfix to resolve issues when querying against BIGINT typed columns. 


We discovered a problem when attempting to apply filters against BIGINT typed columns (ex. file byte_size). This was resolved and all queries not noted in the previous known issues should be runnable. 

### Known Issues

- The generated query string returned from the API will always show the filter value in quotes even if it is not a quoted value (ex. " byte_size > 20 " will be presented as " byte_size < '20' "). This is just an issue presenting the values in the query as a string and not what is actually queried to the database.


## Available July 11, 2024

cdapython version 2024.1.4
API version 2024.1.1

### Highlights:

- Hotfix to resolve issues when using the summary_counts() function with the mutation table


We discovered a problem when attempting to use the summary_counts() function with the mutation table. Attempting this would always result in an error. This was caused by an oversight in the code when we made the change from somatic_mutation to mutation in the previous release. The issue has been resolved.


## Available June 26, 2024

cdapython version 2024.1.3
API version 2024.1.1

### Highlights:

- Fixed issue where somatic_mutation query was returning incorrect results
- Fixed some performance issues with somatic_mutation queries
- Renamed somatic_mutation table to mutation


We discovered incorrect results coming from queries involving the somatic_mutation table. This was caused by the table not having its own id/primary key, instead relying on the subject_alias. This was a deviation from how every other data table was structured, therefore certain queries would fall apart. Changes were made to the data model to structure the newly named "mutation" table to mirror every other table. Due to this change, we needed to simply remove certain code from the API that was added in an attempt handle quirks with the original somatic_mutation table as well as update a few things within the cdapython client.


## Available May 29, 2024

- Summary value data has been reformatted for easier reading
  
- null data has been disambiguated
  
- Users can now submit a tab separated file (tsv) of identifiers or any other set of values to search using the `match_from_file` parameter in fetch_rows. See [this vignette](../documentation/cdapython/vignettes/03_match_from_file.ipynb) for an example.

### Known issues

- `match_from_file` cannot handle very large lists of values (greater than ~10,000)

- the cdapython update is not currently available in pypi, please install using `pip install git+https://github.com/CancerDataAggregator/cdapython.git`. It should be available in pypi soon.

- Some complex joins will return more data than `summary_counts` or the `count_only` parameter report. This is due to miscounting of the join structure.

- Not all errors are handled gracefully, as we haven't found them all yet. If you experience one, please let us know.

- help text for individual functions (and an error message, if you try to use an unavailable value) is currently the only way to obtain a valid list of data_source labels (DC names) for queries. Current list is GDC, PDC, IDC, and CDS.

- column_values endpoint won't process more than one system (i.e. data_source/DC) filter per query.

- the mutations endpoint gives wrong counts (but correct results)
ex.: filtering by hugo_symbol='DOK1' reports 85 results, when the correct number of matching records (and the number of records that is actually returned) is 95.

-Certain queries can pass back large amounts of data which can timeout or fill memory restrictions in colab, mybinder, and other low-memory systems.


## Available April 5, 2024

cdapython has had a complete rewrite to simplify the code. 

### Known Issues:

- the cdapython update is not currently available in pypi, please install using `pip install git+https://github.com/CancerDataAggregator/cdapython.git`. It should be available in pypi soon.

- Impossible joins need better error handling, e.g. `fetch_rows( table='subject', link_to_table='subject' )`.

- Some complex joins will return more data than `summary_counts` or the `count_only` parameter report. This is due to miscounting of the join structure.

- Not all errors are handled gracefully, as we haven't found them all yet. If you experience one, please let us know.

- Developers using the API may experience query problems when building calls that are technically correctly formatted, but do not fit our style guide. ex.: file_associated_project and subject_associated_project currently only work as filters when applied from their home-entity endpoint. ex.: using SELECTVALUES at the mutations endpoint without including the case_barcode column will break. These will be resolved in our upcoming API update. Until then, please contact us directly for assistance.

- help text for individual functions (and an error message, if you try to use an unavailable value) is currently the only way to obtain a valid list of data_source labels (DC names) for queries. Current list is GDC, PDC, IDC, and CDS.

- column_values endpoint won't process more than one system (i.e. data_source/DC) filter per query.

- the mutations endpoint gives wrong counts (but correct results)
ex.: filtering by hugo_symbol='DOK1' reports 85 results, when the correct number of matching records (and the number of records that is actually returned) is 95.

- the mutations endpoint exposes internal record alias info in API results (attaching example)
front end presently strips them out.

- Using the API directly (not through cdapython), it is possible to max out the Java heap space with certain queries.

-Certain queries can pass back large amounts of data which can timeout or fill memory restrictions in colab, readthedocs, and low-memory systems.


# beta versions

## Available August 22, 2023.

### Updates

- get_all has been expanded to work on unique_terms

### Bug fixes

- A visual bug where get_all was displaying multiple progress bars has been fixed
- A bug in the code base model relationships has been fixed that was causing some queries to fail, or to not return all related results.
- Improved linking between mutation table and everything else

### Known bugs and issues - these will be fixed in an upcoming release

- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.


## Available May 4, 2023.

### Updates

- Data extraction process completely rewritten with improved mappings
- Parsing language completely rewritten to increase query speed and flexibility
- `get_all` function replaces `auto_paginator`
- New `.offset()` operator
- New `.limit()` operator 
- Dropped support for python 3.7

### Bug fixes

- 'treatment_anatomic_site', 'treatment_type', 'method_of_diagnosis' and others are now properly filled

### Known bugs and issues - these will be fixed in an upcoming release

- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- mutation endpoint is not harmonized to other endpoints
- progress bars are duplicated



## Available December 21, 2022.

### Updates

- cdapython can now take subject/patient identifier lists from txt, csv, and tsv files as input for search
- The unique_terms function now returns a count of null values along with the term counts

### Bug fixes
- Fixed error where / character was causing some urls to break
- Fixed error where some columns could be counted, but not enumerated

### Known bugs and issues - these will be fixed in an upcoming release

- 'treatment_anatomic_site', 'treatment_type', and 'method_of_diagnosis' are missing data
- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- mutation endpoint is not harmonized to other endpoints



## Available November 3, 2022.

### Updates

- users can now search for subjects that have data from multiple data centers using the `FROM` function
- users can search within dataframes
- dataframe results can be ordered by any column
- `columns` now has information about what endpoint each column lives in, as well as what type of data it is (number, word, etc) and whether it's a required field

### Known bugs and issues - these will be fixed in an upcoming release

- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- mutation endpoint is not harmonized to other endpoints

## Available September 2022.

 We recommend updating to take advantage of improvements to our query language

The beta 3.1 release of CDA now includes search for a gene and mutation information from TCGA


### Updates

- New `mutation` endpoint allows search for gene and mutation information by HUGO gene name, subject, specimen and file
- Searches no longer require full path names for columns, e.g. 'ResearchSubject.Diagnosis.Treatment.treatment_anatomic_site' is now 'treatment_anatomic_site'
- 'id' columns have been made unique, e.g. ''ResearchSubject.Diagnosis.Treatment.id' is now 'treatment_id'
- New `join_as_str` function allows users to use results from one Q search as input to another
- `filter` function in `run` renamed to `include` and now includes flag to allow users to dynamically rename columns in search results
- New `auto_paginator` function has been added that does not require the user to loop through results
- `paginator` and `auto_paginator` now display a progress bar
-  `limit` flag in paginators renamed to `page_size`
- Query return details has been simplified
- `to_list` can now do both fuzzy and exact matching
- `unique_terms` can now optionally show counts of term usage
- `columns` can now display descriptions
- `Q` can now accept arbitrarily complex math as part of a query, e.g.: 
 
         Q('days_to_birth >= 50 * -365 AND days_to_birth <= 20 + -365').specimen.run().to_dataframe()
- Code optimization to improve search speed and performance


### Bug fixes

- Files associated with cancer or normal tissue specimens are now properly attributed as cancer or normal
- `filters` option in `to_list` function is now case-insensitive
- Various error message and handling improvements


### Known bugs and issues - these will be fixed in an upcoming release

- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.


---

# Early alphas

## Available as of 7/11/22

The beta 3.0 release of CDA searches across data from the Genomics Data Commons (GDC), the Proteomics Data Commons (PDC), and the Imaging Data Commons (IDC) to aggregate and return data to users via a single application programming interface (API).


## Updates

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
* Queries on text fields are now case-insensitive
* Added to_dataframe to Q's Result object that converts the JSON structure to a pandas dataframe
* Added paginator to Q's Result object that allows for pagination through result pages. This also has a flag for paginating as a dataframe.
* Added table formatting to count results objects for easier reading

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

Version 3.0 is a full rewrite of our code and older versions of cdapython are no longer maintained or supported.
If you'd like to see how the project has evolved, you can still access the their documentation here:

- [2.0](https://github.com/CancerDataAggregator/CDA-HelpDesk/blob/2.0/docs/source/ReleaseNotes.md)
- [2.1](https://github.com/CancerDataAggregator/CDA-HelpDesk/blob/2.1/docs/source/ReleaseNotes.md)

<!-- Footnotes themselves at the bottom. -->
