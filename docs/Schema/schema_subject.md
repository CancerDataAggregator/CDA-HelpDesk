---
title: Subject schema
---

The **Subject** entity is the outer most record in the Subjects endpoint. Within the **Subject** record are the fields for the **Subject** (demographic and other subject-specific information), a Files field which lists the id of all files associated with the **Subject**, as well as the record of all **ResearchSubject** records associated with that **Subject**. Each **ResearchSubject** record has fields associated with the **ResearchSubject**, as well as records for the **Diagnosis** and **Specimen** entities associated with that **ResearchSubject**, and so on.

Use the "+" and "-" icons to expand and collapse sections of the schema.

<div class="container">
<div id="test">

<script type="text/javascript" src="../../javascripts/renderjson.js"></script>
<script>
renderjson.set_show_to_level(2).set_icons('+', '-');

var example = [


    {
        "1name": "id",
        "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
        "mode": "REQUIRED",
        "type": "STRING"
    },
    {
        "1name": "identifier",
        "description": "A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier - or a URI expressed as a string to an existing entity. ",
        "fields": [
            {
                "1name": "system",
                "description": "The system or namespace that defines the identifier.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "1name": "value",
                "description": "The value of the identifier, as defined by the system.",
                "mode": "NULLABLE",
                "type": "STRING"
            }
        ],
        "mode": "REPEATED",
        "type": "RECORD"
    },
    {
        "1name": "species",
        "description": "The taxonomic group (e.g. species) of the patient. For MVP, since taxonomy vocabulary is consistent between GDC and PDC, using text.  Ultimately, this will be a term returned by the vocabulary service.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "1name": "sex",
        "description": "The biologic character or quality that distinguishes male and female from one another as expressed by analysis of the person's gonadal, morphologic (internal and external), chromosomal, and hormonal characteristics.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "1name": "race",
        "description": "An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "1name": "ethnicity",
        "description": "An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "1name": "days_to_birth",
        "description": "Number of days between the date used for index and the date from a person's date of birth represented as a calculated negative number of days.",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "1name": "subject_associated_project",
        "description": "The list of Projects associated with the Subject.",
        "mode": "REPEATED",
        "type": "STRING"
    },
    {
        "1name": "vital_status",
        "description": "Coded value indicating the state or condition of being living or deceased; also includes the case where the vital status is unknown.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "1name": "days_to_death",
        "description": "Number of days between the date used for index and the date from a person's date of death represented as a calculated number of days.",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "1name": "cause_of_death",
        "description": "Coded value indicating the circumstance or condition that results in the death of the subject.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "1name": "Files",
        "description": "List of ids of File entities associated with the Patient",
        "mode": "REPEATED",
        "type": "STRING"
    },
    {
        "1name": "ResearchSubject",
        "description": "A research subject is the entity of interest in a specific research study or project, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.  This entity plays the role of the case_id in existing data.",
        "fields": [
            {
                "1name": "id",
                "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system. For CDA, this is case_id.",
                "mode": "REQUIRED",
                "type": "STRING"
            },
            {
                "1name": "identifier",
                "description": "A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier - or a URI expressed as a string to an existing entity. ",
                "fields": [
                    {
                        "1name": "system",
                        "description": "The system or namespace that defines the identifier.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "value",
                        "description": "The value of the identifier, as defined by the system.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    }
                ],
                "mode": "REPEATED",
                "type": "RECORD"
            },
            {
                "1name": "member_of_research_project",
                "description": "A reference to the Study(s) of which this ResearchSubject is a member.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "1name": "primary_diagnosis_condition",
                "description": "The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).   This attribute represents the disease that qualified the subject for inclusion on the ResearchProject.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "1name": "primary_diagnosis_site",
                "description": "The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general categories.  This attribute represents the primary site of disease that qualified the subject for inclusion on the ResearchProject.",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "1name": "Files",
                "description": "List of ids of File entities associated with the ResearchSubject",
                "mode": "REPEATED",
                "type": "STRING"
            },
            {
                "1name": "Diagnosis",
                "description": "A collection of characteristics that describe an abnormal condition of the body as assessed at a point in time. May be used to capture information about neoplastic and non-neoplastic conditions.",
                "fields": [
                    {
                        "1name": "id",
                        "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                        "mode": "REQUIRED",
                        "type": "STRING"
                    },
                    {
                        "1name": "identifier",
                        "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                        "fields": [
                            {
                                "1name": "system",
                                "description": "The system or namespace that defines the identifier.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "value",
                                "description": "The value of the identifier, as defined by the system.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            }
                        ],
                        "mode": "REPEATED",
                        "type": "RECORD"
                    },
                    {
                        "1name": "primary_diagnosis",
                        "description": "The diagnosis instance that qualified a subject for inclusion on a ResearchProject",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "age_at_diagnosis",
                        "description": "The age in days of the individual at the time of diagnosis",
                        "mode": "NULLABLE",
                        "type": "INTEGER"
                    },
                    {
                        "1name": "morphology",
                        "description": "Code that represents the histology of the disease using the third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registri",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "stage",
                        "description": "The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "grade",
                        "description": "The degree of abnormality of cancer cells, a measure of differentiation, the extent to which cancer cells are similar in appearance and function to healthy cells of the same tissue type. The degree of differentiation often relates to the clinical behavior of the particular tumor. Based on the microscopic findings, tumor grade is commonly described by one of four degrees of severity. Histopathologic grade of a tumor may be used to plan treatment and estimate the future course, outcome, and overall prognosis of disease. Certain types of cancers, such as soft tissue sarcoma, primary brain tumors, lymphomas, and breast have special grading systems.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "method_of_diagnosis",
                        "description": "The method used to confirm the patients malignant diagnosis",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "Treatment",
                        "description": "Represent medication administration or other treatment types.",
                        "fields": [
                            {
                                "1name": "id",
                                "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                                "mode": "REQUIRED",
                                "type": "STRING"
                            },
                            {
                                "1name": "identifier",
                                "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                                "fields": [
                                    {
                                        "1name": "system",
                                        "description": "The system or namespace that defines the identifier.",
                                        "mode": "NULLABLE",
                                        "type": "STRING"
                                    },
                                    {
                                        "1name": "value",
                                        "description": "The value of the identifier, as defined by the system.",
                                        "mode": "NULLABLE",
                                        "type": "STRING"
                                    }
                                ],
                                "mode": "REPEATED",
                                "type": "RECORD"
                            },
                            {
                                "1name": "treatment_type",
                                "description": "The treatment type including medication/therapeutics or other procedures.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "treatment_outcome",
                                "description": "The final outcome of the treatment.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "days_to_treatment_start",
                                "description": "The timepoint at which the treatment started.",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            },
                            {
                                "1name": "days_to_treatment_end",
                                "description": " The timepoint at which the treatment ended.",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            },
                            {
                                "1name": "therapeutic_agent",
                                "description": "One or more therapeutic agents as part of this treatment.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "treatment_anatomic_site",
                                "description": "The anatomical site that the treatment targets.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "treatment_effect",
                                "description": "The effect of a treatment on the diagnosis or tumor.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "treatment_end_reason",
                                "description": "The reason the treatment ended.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "number_of_cycles",
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
            },
            {
                "1name": "Specimen",
                "description": "Any material taken as a sample from a biological entity (living or dead), or from a physical object or the environment. Specimens are usually collected as an example of their kind, often for use in some investigation.",
                "fields": [
                    {
                        "1name": "id",
                        "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                        "mode": "REQUIRED",
                        "type": "STRING"
                    },
                    {
                        "1name": "identifier",
                        "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                        "fields": [
                            {
                                "1name": "system",
                                "description": "The system or namespace that defines the identifier.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "1name": "value",
                                "description": "The value of the identifier, as defined by the system.",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            }
                        ],
                        "mode": "REPEATED",
                        "type": "RECORD"
                    },
                    {
                        "1name": "associated_project",
                        "description": "The Project associated with the specimen.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "days_to_collection",
                        "description": "The number of days from the index date to either the date a sample was collected for a specific study or project, or the date a patient underwent a procedure (e.g. surgical resection) yielding a sample that was eventually used for research.",
                        "mode": "NULLABLE",
                        "type": "INTEGER"
                    },
                    {
                        "1name": "primary_disease_type",
                        "description": "The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).   This attribute represents the disease that qualified the subject for inclusion on the ResearchProject.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "anatomical_site",
                        "description": "Per GDC Dictionary, the text term that represents the name of the primary disease site of the submitted tumor sample; recommend dropping tumor; biospecimen_anatomic_site.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "source_material_type",
                        "description": "The general kind of material from which the specimen was derived, indicating the physical nature of the source material. ",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "specimen_type",
                        "description": "The high-level type of the specimen, based on its how it has been derived from the original extracted sample. \n",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "derived_from_specimen",
                        "description": "A source/parent specimen from which this one was directly derived.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "derived_from_subject",
                        "description": "The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "1name": "Files",
                        "description": "List of ids of File entities associated with the Specimen",
                        "mode": "REPEATED",
                        "type": "STRING"
                    }
                ],
                "mode": "REPEATED",
                "type": "RECORD"
            }
        ],
        "mode": "REPEATED",
        "type": "RECORD"
    }


];
    document.getElementById("test").appendChild(renderjson(example));
</script>
</div></div>
