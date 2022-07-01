

## Release 3.0-beta 6/28/2022

The beta 3.0 release of CDA searches across data from the Genomics Data Commons (GDC), the Proteomics Data Commons (PDC), and the Imaging Data Commons (IDC) to aggregate and return data to users via a single application programming interface (API). 

## Datasets & Fields

* All datasets updated as follows
    * GDC: v33.1, 06/23/2022
    * PDC: v2.7, 06/23/2022[^1]
    * IDC: v.9.0, 06/24/2022

[^1]:Information pulled from the PDC API may contain embargoed data.

## Enhanced query functionality

* Added support for IN and LIKE SQL statements
* The Subjects query has been simplified to not return file information, instead the new files Q method can be used for files
* Counts function added to Q that gives total counts for each Data Commons given a query
* Filter flag added to Q's run method which allows horizontal filtering of results
* Verbose flag added to Q's run method to hide/show Q actions when running a query
* Query's on text fields are now case insensitive
* Added to_dataframe to Q's Result object that converts the JSON structure to a pandas dataframe
* Added paginator to Q's Result object that allows for pagination through result pages. This also has a flag for paginating as a dataframe.


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

* Fixed issue where queries on list columns that were not lists of json objects (i.e. subject_associated_project) would fail
* Duplicate files should no longer be returned


## Known bugs and issues

* `unique_terms` are not sorted when they return
* tumor stages are not harmonized, there are redundant terms (complicates query)
* Days_to_birth should be reformatted (currently negative) or have an example query
* Docker jupyter notebook does not work if a notebook is already open in port 8888

## Previous Versions

Version 3.0 is a full rewrite of our code and older versions of cda-python are no longer maintained or supported.
If you'd like to see how the project has evolved, you can still access our [2.0](https://cda.readthedocs.io/en/2.0/ReleaseNotes.html) and [2.1](https://cda.readthedocs.io/en/2.1/ReleaseNotes.html) release notes.

<!-- Footnotes themselves at the bottom. -->
