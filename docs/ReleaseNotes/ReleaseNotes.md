

## Release 3.0 6/28/2022
## Datasets & Fields

* All datasets updated as follows
    * GDC: v31.0, 03/17/2022
    * PDC: v2.7, 03/18/2022
    * IDC: v.4.0, 03/09/2022

## Enhanced query functionality

* Added Docker for enabling quickstart
* Enhanced Q functionality to more mimic natural language
* Support for long queries
* Added asynchronous hooks, ability to do searches in parallel
* Unique values and columns return faster than in Release 1


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
        * None
    * Renamed fields (old -> new):
        * None


## Bug fixes

* Fixed problem of unnested items would appear at the top level in the JSON response, resulting in duplication of elements
* Fixed cda-service overwrites query columns with same name
* Added support for the API queries to asynchronous calls.
* Added a unique-values API endpoint for returning distinct values in the cda table
* There is a new status endpoint which will verify that the cda_mvp tables are available.   Please let the dev team know if there is additional info that would be useful from this endpoint in the future.  "total table rows, size of schemas etc"
* Support the ability to query development tables being used for integrating the IDC data with the existing PDC and GDC data. If your jupyter notebooks fail to execute, you will likely have to reload the cda-python into your python virtual environment.


## Known bugs and issues

* `unique_terms` are not sorted when they return
* tumor stages are not harmonized, there are redundant terms (complicates query)
* Days_to_birth should be reformatted (currently negative) or have an example query
* Docker jupyter notebook does not work if a notebook is already open in port 8888

<!-- Footnotes themselves at the bottom. -->

[^1]:
     Information pulled from the PDC API may contain embargoed data.
