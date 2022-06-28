---
title: File schema
---

The **File** entity is the outer most record in the Files endpoint. Within the **File** record are the fields for the **File** (file metadata), as well as the record of all **Subject**, **ResearchSubject**, and **Specimen** records associated with that **File**. Each of the entities previously mentioned has fields associated with those entities.

Use the "+" and "-" icons to expand and collapse sections of the schema.

<div class="container">
<div id="test">

<script type="text/javascript" src="../../javascripts/renderjson.js"></script>
<script>
renderjson.set_show_to_level(2).set_icons('+', '-');


var example = [

    {
        "name": "id",
        "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
        "mode": "REQUIRED",
        "type": "STRING"
    },
    {
        "name": "identifier",
        "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
        "fields": [
            {
                "name": "system",
                "description": "The system or namespace that defines the identifier.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "value",
                "description": "The value of the identifier, as defined by the system.",
                "mode": "NULLABLE",
                "type": "STRING"
            }
        ],
        "mode": "REPEATED",
        "type": "RECORD"
    },
    {
        "name": "label",
        "description": "Short name or abbreviation for dataset. Maps to rdfs:label.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "data_category",
        "description": "Broad categorization of the contents of the data file.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "data_type",
        "description": "Specific content type of the data file.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "file_format",
        "description": "Format of the data files.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "associated_project",
        "description": "A reference to the Project(s) of which this ResearchSubject is a member. The associated_project may be embedded using the $ref definition or may be a reference to the id for the Project - or a URI expressed as a string to an existing entity.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "drs_uri",
        "description": "A string of characters used to identify a resource on the Data Repo Service(DRS).",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "byte_size",
        "description": "Size of the file in bytes. Maps to dcat:byteSize.",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "checksum",
        "description": "A digit representing the sum of the correct digits in a piece of stored or transmitted digital data, against which later comparisons can be made to detect errors in the data.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "data_modality",
        "description": "Data modality describes the biological nature of the information gathered as the result of an Activity, independent of the technology or methods used to produce the information.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "imaging_modality",
        "description": "An imaging modality describes the imaging equipment and/or method used to acquire certain structural or functional information about the body. These include but are not limited to computed tomography (CT) and magnetic resonance imaging (MRI). Taken from the DICOM standard.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "dbgap_accession_number",
        "description": "The dbgap accession number for the project.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "imaging_series",
        "description": "The 'logical' identifier of the series or grouping of imaging files in the system of record which the file is a part of.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Subject",
        "description": "A subject entity captures the study-independent metadata for research subjects. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.",
        "fields": [
            {
                "name": "id",
                "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                "mode": "REQUIRED",
                "type": "STRING"
            },
            {
                "name": "identifier",
                "description": "A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier - or a URI expressed as a string to an existing entity. ",
                "fields": [
                    {
                        "name": "system",
                        "description": "The system or namespace that defines the identifier.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "value",
                        "description": "The value of the identifier, as defined by the system.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    }
                ],
                "mode": "REPEATED",
                "type": "RECORD"
            },
            {
                "name": "species",
                "description": "The taxonomic group (e.g. species) of the subject. For MVP, since taxonomy vocabulary is consistent between GDC and PDC, using text.  Ultimately, this will be a term returned by the vocabulary service.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "sex",
                "description": "The biologic character or quality that distinguishes male and female from one another as expressed by analysis of the person's gonadal, morphologic (internal and external), chromosomal, and hormonal characteristics.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "race",
                "description": "An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "ethnicity",
                "description": "An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "days_to_birth",
                "description": "Number of days between the date used for index and the date from a person's date of birth represented as a calculated negative number of days.",
                "mode": "NULLABLE",
                "type": "INTEGER"
            },
            {
                "name": "subject_associated_project",
                "description": "The list of Projects associated with the Subject.",
                "mode": "REPEATED",
                "type": "STRING"
            },
            {
                "name": "vital_status",
                "description": "Coded value indicating the state or condition of being living or deceased; also includes the case where the vital status is unknown.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "days_to_death",
                "description": "Number of days between the date used for index and the date from a person's date of death represented as a calculated number of days.",
                "mode": "NULLABLE",
                "type": "INTEGER"
            },
            {
                "name": "cause_of_death",
                "description": "Coded value indicating the circumstance or condition that results in the death of the subject.",
                "mode": "NULLABLE",
                "type": "STRING"
            }
        ],
        "mode": "REPEATED",
        "type": "RECORD"
    },
    {
        "name": "ResearchSubject",
        "description": "A research subject is the entity of interest in a specific research study or project, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.  This entity plays the role of the case_id in existing data.",
        "fields": [
            {
                "name": "id",
                "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system. For CDA, this is case_id.",
                "mode": "REQUIRED",
                "type": "STRING"
            },
            {
                "name": "identifier",
                "description": "A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier - or a URI expressed as a string to an existing entity. ",
                "fields": [
                    {
                        "name": "system",
                        "description": "The system or namespace that defines the identifier.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "value",
                        "description": "The value of the identifier, as defined by the system.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    }
                ],
                "mode": "REPEATED",
                "type": "RECORD"
            },
            {
                "name": "member_of_research_project",
                "description": "A reference to the Study(s) of which this ResearchSubject is a member.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "primary_diagnosis_condition",
                "description": "The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).   This attribute represents the disease that qualified the subject for inclusion on the ResearchProject.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "primary_diagnosis_site",
                "description": "The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general categories.  This attribute represents the primary site of disease that qualified the subject for inclusion on the ResearchProject.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "Diagnosis",
                "description": "A collection of characteristics that describe an abnormal condition of the body as assessed at a point in time. May be used to capture information about neoplastic and non-neoplastic conditions.",
                "fields": [
                    {
                        "name": "id",
                        "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                        "mode": "REQUIRED",
                        "type": "STRING"
                    },
                    {
                        "name": "identifier",
                        "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                        "fields": [
                            {
                                "name": "system",
                                "description": "The system or namespace that defines the identifier.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "value",
                                "description": "The value of the identifier, as defined by the system.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            }
                        ],
                        "mode": "REPEATED",
                        "type": "RECORD"
                    },
                    {
                        "name": "primary_diagnosis",
                        "description": "The diagnosis instance that qualified a subject for inclusion on a ResearchProject.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "age_at_diagnosis",
                        "description": "The age in days of the individual at the time of diagnosis.",
                        "mode": "NULLABLE",
                        "type": "INTEGER"
                    },
                    {
                        "name": "morphology",
                        "description": "Code that represents the histology of the disease using the third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries for coding the site (topography) and the histology (morphology) of neoplasms.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "stage",
                        "description": "The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "grade",
                        "description": "The degree of abnormality of cancer cells, a measure of differentiation, the extent to which cancer cells are similar in appearance and function to healthy cells of the same tissue type. The degree of differentiation often relates to the clinical behavior of the particular tumor. Based on the microscopic findings, tumor grade is commonly described by one of four degrees of severity. Histopathologic grade of a tumor may be used to plan treatment and estimate the future course, outcome, and overall prognosis of disease. Certain types of cancers, such as soft tissue sarcoma, primary brain tumors, lymphomas, and breast have special grading systems.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "method_of_diagnosis",
                        "description": "The method used to confirm the subjects malignant diagnosis.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "Treatment",
                        "description": "Represent medication administration or other treatment types.",
                        "fields": [
                            {
                                "name": "id",
                                "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                                "mode": "REQUIRED",
                                "type": "STRING"
                            },
                            {
                                "name": "identifier",
                                "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                                "fields": [
                                    {
                                        "name": "system",
                                        "description": "The system or namespace that defines the identifier.",
                                        "mode": "NULLABLE",
                                        "type": "STRING"
                                    },
                                    {
                                        "name": "value",
                                        "description": "The value of the identifier, as defined by the system.",
                                        "mode": "NULLABLE",
                                        "type": "STRING"
                                    }
                                ],
                                "mode": "REPEATED",
                                "type": "RECORD"
                            },
                            {
                                "name": "treatment_type",
                                "description": "The treatment type including medication/therapeutics or other procedures.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_outcome",
                                "description": "The final outcome of the treatment.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "days_to_treatment_start",
                                "description": "The timepoint at which the treatment started.",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            },
                            {
                                "name": "days_to_treatment_end",
                                "description": " The timepoint at which the treatment ended.",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            },
                            {
                                "name": "therapeutic_agent",
                                "description": "One or more therapeutic agents as part of this treatment.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_anatomic_site",
                                "description": "The anatomical site that the treatment targets.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_effect",
                                "description": "The effect of a treatment on the diagnosis or tumor.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_end_reason",
                                "description": "The reason the treatment ended.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "number_of_cycles",
                                "description": "The number of treatment cycles the subject received.",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            }
                        ],
                        "mode": "REPEATED",
                        "type": "RECORD"
                    }
                ],
                "mode": "REPEATED",
                "type": "RECORD"
            }
        ],
        "mode": "REPEATED",
        "type": "RECORD"
    },
    {
        "name": "Specimen",
        "description": "Any material taken as a sample from a biological entity (living or dead), or from a physical object or the environment. Specimens are usually collected as an example of their kind, often for use in some investigation.",
        "fields": [
            {
                "name": "id",
                "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                "mode": "REQUIRED",
                "type": "STRING"
            },
            {
                "name": "identifier",
                "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                "fields": [
                    {
                        "name": "system",
                        "description": "The system or namespace that defines the identifier.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "value",
                        "description": "The value of the identifier, as defined by the system.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    }
                ],
                "mode": "REPEATED",
                "type": "RECORD"
            },
            {
                "name": "associated_project",
                "description": "The Project associated with the specimen.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "days_to_collection",
                "description": "The number of days from the index date to either the date a sample was collected for a specific study or project, or the date a subject underwent a procedure (e.g. surgical resection) yielding a sample that was eventually used for research.",
                "mode": "NULLABLE",
                "type": "INTEGER"
            },
            {
                "name": "primary_disease_type",
                "description": "The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).   This attribute represents the disease that qualified the subject for inclusion on the ResearchProject.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "anatomical_site",
                "description": "Per GDC Dictionary, the text term that represents the name of the primary disease site of the submitted tumor sample; recommend dropping tumor; biospecimen_anatomic_site.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "source_material_type",
                "description": "The general kind of material from which the specimen was derived, indicating the physical nature of the source material. ",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "specimen_type",
                "description": "The high-level type of the specimen, based on its how it has been derived from the original extracted sample.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "derived_from_specimen",
                "description": "A source/parent specimen from which this one was directly derived.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "derived_from_subject",
                "description": "The subject/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.",
                "mode": "NULLABLE",
                "type": "STRING"
            }
        ],
        "mode": "REPEATED",
        "type": "RECORD"
    }



];
    document.getElementById("test").appendChild(renderjson(example));
</script>
</div></div>
