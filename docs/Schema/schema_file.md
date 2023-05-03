---
title: File schema
---

The **File** entity is the outer most record in the Files endpoint. Within the **File** record are the fields for the **File** (file metadata), as well as the record of all **Subject**, **ResearchSubject**, and **Specimen** records associated with that **File**. Each of the entities previously mentioned has fields associated with those entities.

You can download this JSON directly on our [Github page.](https://raw.githubusercontent.com/CancerDataAggregator/readthedocs/main/docs/Schema/schema_file.md)

Use the "+" and "-" icons to expand and collapse sections of the schema.

<div class="container">
<div id="test">

<script type="text/javascript" src="../../javascripts/renderjson.js"></script>
<script>
renderjson.set_show_to_level(2).set_icons('+', '-');


var example = [
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
    "name": "label",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Short name or abbreviation for dataset. Maps to rdfs:label.",
    "fields": []
  },
  {
    "name": "data_category",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Broad categorization of the contents of the data file.",
    "fields": []
  },
  {
    "name": "data_type",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Specific content type of the data file.",
    "fields": []
  },
  {
    "name": "file_format",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Format of the data files.",
    "fields": []
  },
  {
    "name": "associated_project",
    "mode": "REPEATED",
    "type": "STRING",
    "description": "A reference to the Project(s) of which this ResearchSubject is a member. The associated_project may be embedded using the $ref definition or may be a reference to the id for the Project - or a URI expressed as a string to an existing entity.",
    "fields": []
  },
  {
    "name": "drs_uri",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "A string of characters used to identify a resource on the Data Repo Service(DRS).",
    "fields": []
  },
  {
    "name": "byte_size",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Size of the file in bytes. Maps to dcat:byteSize.",
    "fields": []
  },
  {
    "name": "checksum",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "A digit representing the sum of the correct digits in a piece of stored or transmitted digital data, against which later comparisons can be made to detect errors in the data.",
    "fields": []
  },
  {
    "name": "data_modality",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Data modality describes the biological nature of the information gathered as the result of an Activity, independent of the technology or methods used to produce the information.",
    "fields": []
  },
  {
    "name": "imaging_modality",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "An imaging modality describes the imaging equipment and/or method used to acquire certain structural or functional information about the body. These include but are not limited to computed tomography (CT) and magnetic resonance imaging (MRI). Taken from the DICOM standard.",
    "fields": []
  },
  {
    "name": "dbgap_accession_number",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The dbgap accession number for the project.",
    "fields": []
  },
  {
    "name": "imaging_series",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The 'logical' identifier of the series or grouping of imaging files in the system of record which the file is a part of.",
    "fields": []
  },
  {
    "name": "Subjects",
    "mode": "REPEATED",
    "type": "STRING",
    "description": "List of ids of Subject entities associated with the File",
    "fields": []
  },
  {
    "name": "ResearchSubjects",
    "mode": "REPEATED",
    "type": "STRING",
    "description": "List of ids of ResearchSubject entities associated with the File",
    "fields": []
  },
  {
    "name": "Specimens",
    "mode": "REPEATED",
    "type": "STRING",
    "description": "List of ids of Specimen entities associated with the File",
    "fields": []
  }
];
    document.getElementById("test").appendChild(renderjson(example));
</script>
</div></div>
