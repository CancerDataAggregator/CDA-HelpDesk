---
title:  Data Updates
status: new
---

# Public releases

## Available March 31, 2024


# beta versions

## Available September, 12 2023.



#### Data extraction and release information


- GDC data version 38.0 (extraction date 9/1/2023)
- PDC data version 3.4 (extraction date 8/24/2023)
- IDC data version 15 (extraction date 7/19/2023)
- CDS data version 3.0 (extraction date 8/31/2023)

Data from Cancer Data Services (CDS) is now available!


## Available June 13, 2023.



#### Data extraction and release information

- GDC data version 37.0 (extraction date 6/1/2023)
- PDC data version 3.0 (extraction date 6/5/2023)
- IDC data version 14 (extraction date 6/7/2023)

IDC data now contains ethnicity data

## Available May 4, 2023.



### Datasets & Fields

#### Data extraction and release information

The current version and release dates for each of the database are:

* GDC data version 37, extraction date - 4/5/2023
* PDC data version 2.16, extraction date - 2/9/2023
* IDC data version 13, extraction date - 4/4/2023



## Available November 3, 2022.

### Datasets & Fields

#### Data extraction and release information
The current version and release dates for each of the database are:

* GDC data version - v34.0, GDC extraction date - 09/29/2022
* PDC data version - v2.10, PDC extraction date - 09/29/2022
* IDC data version - v.10.0, IDC extraction date - 09/29/2022


## Available September 2022.

### Datasets & Fields

* Versions:
    * GDC: v33.1, 06/23/2022
    * PDC: v2.7, 06/23/2022[^1]
    * IDC: v.9.0, 06/24/2022

[^1]:Information pulled from the PDC API may contain embargoed data.

---

# Early alphas

## Available as of 7/11/22.


The beta 3.0 release of CDA searches across data from the Genomics Data Commons (GDC), the Proteomics Data Commons (PDC), and the Imaging Data Commons (IDC) to aggregate and return data to users via a single application programming interface (API).

### Datasets & Fields

* All datasets updated as follows
    * GDC: v33.1, 06/23/2022
    * PDC: v2.7, 06/23/2022[^1]
    * IDC: v.9.0, 06/24/2022

[^1]:Information pulled from the PDC API may contain embargoed data.


### Metadata Changes

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



## Known bugs and issues - these will be fixed in an upcoming release

* tumor stages are not harmonized, there are redundant terms (complicates query)
* Searches on the subject endpoint incorrectly count files. Please use the file counts for the same query from the files endpoint
* Some PDC files are incorrectly labeled at the specimen level, for e.g. a file may be inappropriately labeled as both cancer and normal.

## 2.X

Version 3.0 is a full rewrite of our code and older versions of cda-python are no longer maintained or supported.
If you'd like to see how the project has evolved, you can still access the their documentation here:

- [2.0](https://cda.readthedocs.io/en/2.0/ReleaseNotes.html)
- [2.1](https://cda.readthedocs.io/en/2.1/ReleaseNotes.html)

<!-- Footnotes themselves at the bottom. -->