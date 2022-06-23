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
        "description": " ",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "data_type",
        "description": " ",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "file_format",
        "description": "String to identify the full file extension including compression extensions.",
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
        "description": "",
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
        "description": " ",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "data_modality",
        "description": "",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "imaging_modality",
        "description": "",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "dbgap_accession_number",
        "description": "",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "crdc_series_uuid",
        "description": "",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Subject",
        "description": "A patient entity captures the study-independent metadata for research subjects. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.",
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
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "sex",
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "race",
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "ethnicity",
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "days_to_birth",
                "description": "Per GDC Dictionary, number of days between the date used for index and the date from a person's date of birth represented as a calculated negative number of days.",
                "mode": "NULLABLE",
                "type": "INTEGER"
            },
            {
                "name": "subject_associated_project",
                "description": "",
                "mode": "REPEATED",
                "type": "STRING"
            },
            {
                "name": "vital_status",
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "age_at_death",
                "description": "",
                "mode": "NULLABLE",
                "type": "INTEGER"
            },
            {
                "name": "cause_of_death",
                "description": "",
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
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "primary_diagnosis_condition",
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "primary_diagnosis_site",
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "Diagnosis",
                "description": "",
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
                        "description": "",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "age_at_diagnosis",
                        "description": "",
                        "mode": "NULLABLE",
                        "type": "INTEGER"
                    },
                    {
                        "name": "morphology",
                        "description": "",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "stage",
                        "description": "",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "grade",
                        "description": "",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "method_of_diagnosis",
                        "description": "",
                        "mode": "NULLABLE",
                        "type": "STRING"
                    },
                    {
                        "name": "Treatment",
                        "description": "",
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
                                "description": "Text name for treatment type; this will ultimately be defined by a common vocabulary",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_outcome",
                                "description": "Text name for treatment outcome; this will ultimately be defined by a common vocabulary",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "days_to_treatment_start",
                                "description": "The date and optionally time that the treatment was started in integer.",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            },
                            {
                                "name": "days_to_treatment_end",
                                "description": "",
                                "mode": "NULLABLE",
                                "type": "INTEGER"
                            },
                            {
                                "name": "therapeutic_agent",
                                "description": "",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_anatomic_site",
                                "description": "",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_effect",
                                "description": "",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "treatment_end_reason",
                                "description": "",
                                "mode": "NULLABLE",
                                "type": "STRING"
                            },
                            {
                                "name": "number_of_cycles",
                                "description": "",
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
                "description": "",
                "mode": "NULLABLE",
                "type": "STRING"
            },
            {
                "name": "age_at_collection",
                "description": "The age of the Patient when this sample was taken.",
                "mode": "NULLABLE",
                "type": "INTEGER"
            },
            {
                "name": "primary_disease_type",
                "description": "",
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
                "description": "The high-level type of the specimen, based on its how it has been derived from the original extracted sample. \n",
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
                "description": "The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.",
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
