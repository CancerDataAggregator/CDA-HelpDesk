---
title:  cdapython releases
status: new
---

# Public releases
<div id="fornews" markdown="1">

## Available May 29, 2024

- Summary value data has been reformatted for easier reading
  
- null data has been disambiguated
  
- Users can now submit a tab separated file (tsv) of identifiers or any other set of values to search using the `match_from_file` parameter in fetch_rows. See this vignette for an example.

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

cdapython has had a complete rewrite to simplify the code. If you are an existing user [we have a guide for updating your existing code](../documentation/cdapython/code_update.md)

### Known Issues:

- the cdapython update is not currently available in pypi, please install using `pip install git+https://github.com/CancerDataAggregator/cdapython.git`. It should be available in pypi soon.

- Impossible joins need better error handling, e.g. `fetch_rows( table='subject', link_to_table='subject' )`.

- Some complex joins will return more data than `summary_counts` or the `count_only` parameter report. This is due to miscounting of the join structure.

- Not all errors are handled gracefully, as we haven't found them all yet. ff you experience one, please let us know.

- Developers using the API may experience query problems when building calls that are technically correctly formatted, but do not fit our style guide. ex.: file_associated_project and subject_associated_project currently only work as filters when applied from their home-entity endpoint. ex.: using SELECTVALUES at the mutations endpoint without including the case_barcode column will break. These will be resolved in our upcoming API update. Until then, please contact us directly for assistance.

- help text for individual functions (and an error message, if you try to use an unavailable value) is currently the only way to obtain a valid list of data_source labels (DC names) for queries. Current list is GDC, PDC, IDC, and CDS.

- column_values endpoint won't process more than one system (i.e. data_source/DC) filter per query.

- the mutations endpoint gives wrong counts (but correct results)
ex.: filtering by hugo_symbol='DOK1' reports 85 results, when the correct number of matching records (and the number of records that is actually returned) is 95.

- the mutations endpoint exposes internal record alias info in API results (attaching example)
front end presently strips them out.

- Using the API directly (not through cdapython), it is possible to max out the Java heap space with certain queries.

-Certain queries can pass back large amounts of data which can timeout or fill memory restrictions in colab, readthedocs, and low-memory systems.

</div>
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
* Queries on text fields are now case insensitive
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

- [2.0](https://cda.readthedocs.io/en/2.0/ReleaseNotes.html)
- [2.1](https://cda.readthedocs.io/en/2.1/ReleaseNotes.html)

<!-- Footnotes themselves at the bottom. -->
