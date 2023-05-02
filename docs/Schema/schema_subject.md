---
title: Subject schema
---

The **Subject** entity is the outer most record in the Subjects endpoint. Within the **Subject** record are the fields for the **Subject** (demographic and other subject-specific information), a Files field which lists the id of all files associated with the **Subject**, as well as the record of all **ResearchSubject** records associated with that **Subject**. Each **ResearchSubject** record has fields associated with the **ResearchSubject**, as well as records for the **Diagnosis** and **Specimen** entities associated with that **ResearchSubject**, and so on.

You can download this JSON directly on our [Github page.](https://raw.githubusercontent.com/CancerDataAggregator/readthedocs/main/docs/Schema/schema_subject.md)


Use the "+" and "-" icons to expand and collapse sections of the schema.

<div class="container">
<div id="test">

<script type="text/javascript" src="../../javascripts/renderjson.js"></script>
<script>
renderjson.set_show_to_level(2).set_icons('+', '-');

var example = [
[
  {
    "name": "id",
    "mode": "REQUIRED",
    "type": "STRING",
    "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
    "fields": []
  },
  {
    "name": "identifier",
    "mode": "REPEATED",
    "type": "RECORD",
    "description": "A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier - or a URI expressed as a string to an existing entity. ",
    "fields": [
      {
        "name": "system",
        "mode": "NULLABLE",
        "type": "STRING",
        "description": "The system or namespace that defines the identifier.",
        "fields": []
      },
      {
        "name": "field_name",
        "mode": "NULLABLE",
        "type": "STRING",
        "description": "The name of the data object in the originating namespace from which the identifier was loaded.",
        "fields": []
      },
      {
        "name": "value",
        "mode": "NULLABLE",
        "type": "STRING",
        "description": "The value of the identifier, as defined by the system.",
        "fields": []
      }
    ]
  },
  {
    "name": "species",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The taxonomic group (e.g. species) of the patient. For MVP, since taxonomy vocabulary is consistent between GDC and PDC, using text.  Ultimately, this will be a term returned by the vocabulary service.",
    "fields": []
  },
  {
    "name": "sex",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The biologic character or quality that distinguishes male and female from one another as expressed by analysis of the person's gonadal, morphologic (internal and external), chromosomal, and hormonal characteristics.",
    "fields": []
  },
  {
    "name": "race",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.",
    "fields": []
  },
  {
    "name": "ethnicity",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.",
    "fields": []
  },
  {
    "name": "days_to_birth",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Number of days between the date used for index and the date from a person's date of birth represented as a calculated negative number of days.",
    "fields": []
  },
  {
    "name": "subject_associated_project",
    "mode": "REPEATED",
    "type": "STRING",
    "description": "The list of Projects associated with the Subject.",
    "fields": []
  },
  {
    "name": "vital_status",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Coded value indicating the state or condition of being living or deceased; also includes the case where the vital status is unknown.",
    "fields": []
  },
  {
    "name": "days_to_death",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Number of days between the date used for index and the date from a person's date of death represented as a calculated number of days.",
    "fields": []
  },
  {
    "name": "cause_of_death",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Coded value indicating the circumstance or condition that results in the death of the subject.",
    "fields": []
  },
  {
    "name": "ResearchSubject",
    "mode": "REPEATED",
    "type": "RECORD",
    "description": "A research subject is the entity of interest in a specific research study or project, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.  This entity plays the role of the case_id in existing data.",
    "fields": [
      {
        "name": "id",
        "mode": "REQUIRED",
        "type": "STRING",
        "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system. For CDA, this is case_id.",
        "fields": []
      },
      {
        "name": "identifier",
        "mode": "REPEATED",
        "type": "RECORD",
        "description": "A 'business' identifier for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). Uses a specialized, complex 'Identifier' data type to capture information about the source of the business identifier - or a URI expressed as a string to an existing entity. ",
        "fields": [
          {
            "name": "system",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The system or namespace that defines the identifier.",
            "fields": []
          },
          {
            "name": "field_name",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The name of the data object in the originating namespace from which the identifier was loaded.",
            "fields": []
          },
          {
            "name": "value",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The value of the identifier, as defined by the system.",
            "fields": []
          }
        ]
      },
      {
        "name": "member_of_research_project",
        "mode": "NULLABLE",
        "type": "STRING",
        "description": "A reference to the Study(s) of which this ResearchSubject is a member.",
        "fields": []
      },
      {
        "name": "primary_diagnosis_condition",
        "mode": "NULLABLE",
        "type": "STRING",
        "description": "The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).   This attribute represents the disease that qualified the subject for inclusion on the ResearchProject.",
        "fields": []
      },
      {
        "name": "primary_diagnosis_site",
        "mode": "NULLABLE",
        "type": "STRING",
        "description": "The text term used to describe the primary site of disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O). This categorization groups cases into general categories.  This attribute represents the primary site of disease that qualified the subject for inclusion on the ResearchProject.",
        "fields": []
      },
      {
        "name": "Diagnosis",
        "mode": "REPEATED",
        "type": "RECORD",
        "description": "A collection of characteristics that describe an abnormal condition of the body as assessed at a point in time. May be used to capture information about neoplastic and non-neoplastic conditions.",
        "fields": [
          {
            "name": "id",
            "mode": "REQUIRED",
            "type": "STRING",
            "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
            "fields": []
          },
          {
            "name": "identifier",
            "mode": "REPEATED",
            "type": "RECORD",
            "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
            "fields": [
              {
                "name": "system",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The system or namespace that defines the identifier.",
                "fields": []
              },
              {
                "name": "field_name",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The name of the data object in the originating namespace from which the identifier was loaded.",
                "fields": []
              },
              {
                "name": "value",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The value of the identifier, as defined by the system.",
                "fields": []
              }
            ]
          },
          {
            "name": "primary_diagnosis",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The diagnosis instance that qualified a subject for inclusion on a ResearchProject.",
            "fields": []
          },
          {
            "name": "age_at_diagnosis",
            "mode": "NULLABLE",
            "type": "INTEGER",
            "description": "The age in days of the individual at the time of diagnosis.",
            "fields": []
          },
          {
            "name": "morphology",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "Code that represents the histology of the disease using the third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries for coding the site (topography) and the histology (morphology) of neoplasms.",
            "fields": []
          },
          {
            "name": "stage",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The extent of a cancer in the body. Staging is usually based on the size of the tumor, whether lymph nodes contain cancer, and whether the cancer has spread from the original site to other parts of the body.",
            "fields": []
          },
          {
            "name": "grade",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The degree of abnormality of cancer cells, a measure of differentiation, the extent to which cancer cells are similar in appearance and function to healthy cells of the same tissue type. The degree of differentiation often relates to the clinical behavior of the particular tumor. Based on the microscopic findings, tumor grade is commonly described by one of four degrees of severity. Histopathologic grade of a tumor may be used to plan treatment and estimate the future course, outcome, and overall prognosis of disease. Certain types of cancers, such as soft tissue sarcoma, primary brain tumors, lymphomas, and breast have special grading systems.",
            "fields": []
          },
          {
            "name": "method_of_diagnosis",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The method used to confirm the subjects malignant diagnosis.",
            "fields": []
          },
          {
            "name": "Treatment",
            "mode": "REPEATED",
            "type": "RECORD",
            "description": "Represent medication administration or other treatment types.",
            "fields": [
              {
                "name": "id",
                "mode": "REQUIRED",
                "type": "STRING",
                "description": "The 'logical' identifier of the entity in the repository, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
                "fields": []
              },
              {
                "name": "identifier",
                "mode": "REPEATED",
                "type": "RECORD",
                "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
                "fields": [
                  {
                    "name": "system",
                    "mode": "NULLABLE",
                    "type": "STRING",
                    "description": "The system or namespace that defines the identifier.",
                    "fields": []
                  },
                  {
                    "name": "field_name",
                    "mode": "NULLABLE",
                    "type": "STRING",
                    "description": "The name of the data object in the originating namespace from which the identifier was loaded.",
                    "fields": []
                  },
                  {
                    "name": "value",
                    "mode": "NULLABLE",
                    "type": "STRING",
                    "description": "The value of the identifier, as defined by the system.",
                    "fields": []
                  }
                ]
              },
              {
                "name": "treatment_type",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The treatment type including medication/therapeutics or other procedures.",
                "fields": []
              },
              {
                "name": "treatment_outcome",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The final outcome of the treatment.",
                "fields": []
              },
              {
                "name": "days_to_treatment_start",
                "mode": "NULLABLE",
                "type": "INTEGER",
                "description": "The timepoint at which the treatment started.",
                "fields": []
              },
              {
                "name": "days_to_treatment_end",
                "mode": "NULLABLE",
                "type": "INTEGER",
                "description": " The timepoint at which the treatment ended.",
                "fields": []
              },
              {
                "name": "therapeutic_agent",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "One or more therapeutic agents as part of this treatment.",
                "fields": []
              },
              {
                "name": "treatment_anatomic_site",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The anatomical site that the treatment targets.",
                "fields": []
              },
              {
                "name": "treatment_effect",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The effect of a treatment on the diagnosis or tumor.",
                "fields": []
              },
              {
                "name": "treatment_end_reason",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The reason the treatment ended.",
                "fields": []
              },
              {
                "name": "number_of_cycles",
                "mode": "NULLABLE",
                "type": "INTEGER",
                "description": "The number of treatment cycles the subject received.",
                "fields": []
              }
            ]
          }
        ]
      },
      {
        "name": "Specimen",
        "mode": "REPEATED",
        "type": "RECORD",
        "description": "Any material taken as a sample from a biological entity (living or dead), or from a physical object or the environment. Specimens are usually collected as an example of their kind, often for use in some investigation.",
        "fields": [
          {
            "name": "id",
            "mode": "REQUIRED",
            "type": "STRING",
            "description": "The 'logical' identifier of the entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system.",
            "fields": []
          },
          {
            "name": "identifier",
            "mode": "REPEATED",
            "type": "RECORD",
            "description": "A 'business' identifier  or accession number for the entity, typically as provided by an external system or authority, that persists across implementing systems  (i.e. a  'logical' identifier). ",
            "fields": [
              {
                "name": "system",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The system or namespace that defines the identifier.",
                "fields": []
              },
              {
                "name": "field_name",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The name of the data object in the originating namespace from which the identifier was loaded.",
                "fields": []
              },
              {
                "name": "value",
                "mode": "NULLABLE",
                "type": "STRING",
                "description": "The value of the identifier, as defined by the system.",
                "fields": []
              }
            ]
          },
          {
            "name": "associated_project",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The Project associated with the specimen.",
            "fields": []
          },
          {
            "name": "days_to_collection",
            "mode": "NULLABLE",
            "type": "INTEGER",
            "description": "The number of days from the index date to either the date a sample was collected for a specific study or project, or the date a subject underwent a procedure (e.g. surgical resection) yielding a sample that was eventually used for research.",
            "fields": []
          },
          {
            "name": "primary_disease_type",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The text term used to describe the type of malignant disease, as categorized by the World Health Organization's (WHO) International Classification of Diseases for Oncology (ICD-O).   This attribute represents the disease that qualified the subject for inclusion on the ResearchProject.",
            "fields": []
          },
          {
            "name": "anatomical_site",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "Per GDC Dictionary, the text term that represents the name of the primary disease site of the submitted tumor sample; recommend dropping tumor; biospecimen_anatomic_site.",
            "fields": []
          },
          {
            "name": "source_material_type",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The general kind of material from which the specimen was derived, indicating the physical nature of the source material. ",
            "fields": []
          },
          {
            "name": "specimen_type",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The high-level type of the specimen, based on its how it has been derived from the original extracted sample. \n",
            "fields": []
          },
          {
            "name": "derived_from_specimen",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "A source/parent specimen from which this one was directly derived.",
            "fields": []
          },
          {
            "name": "derived_from_subject",
            "mode": "NULLABLE",
            "type": "STRING",
            "description": "The Patient/ResearchSubject, or Biologically Derived Materal (e.g. a cell line, tissue culture, organoid) from which the specimen was directly or indirectly derived.",
            "fields": []
          }
        ]
      }
    ]
  }
]
];
    document.getElementById("test").appendChild(renderjson(example));
</script>
</div></div>
