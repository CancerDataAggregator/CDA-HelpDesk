# CDA Extraction Transfer and Load (ETL) Documentation
## Introduction
The goal of this document is to record in greater detail the ETL process which the CDA uses to create the aggregated data tables which the API layer queries. A brief overview of the process to generate an endpoint table is seen below in Fig.1. Data from the Data Commons (DC), [GDC](https://portal.gdc.cancer.gov/) and [PDC](https://pdc.cancer.gov/pdc/), undergo a similar process including extraction using publicly available API’s, and transformation into a structure based on the [CDA model](../Schema/overview_mapping.md). [IDC](https://portal.imaging.datacommons.cancer.gov/) data is queried and transformed using a single BigQuery query. The results of this query are saved and merged with the transformed GDC and PDC data and uploaded to BigQuery as a table that is queried by the CDA API.

## Data extraction and release information
The current version and release dates for each of the database are:

* GDC data version - v34.0, GDC extraction date - 09/29/2022
* PDC data version - v2.10, PDC extraction date - 09/29/2022
* IDC data version - v.10.0, IDC extraction date - 09/29/2022

## R3.1 ETL Achievements
The achievements for R3.0 are outlined as follows:

* Previous table format now called Subjects endpoint
    * Removed all Files lists
* Files endpoint added:
    * Subjects - list of Subject ids associated with the File
    * ResearchSubjects - list of ResearchSubject ids associated with the File
    * Specimens - list of Specimen ids associated with the File
    * PDC files now include some files exclusively available from filesPerStudy query
* Updated all DC data to latest versions available as of 09/29/2022

## R3.1 ETL Process Overview

Data from each DC (GDC, PDC, and IDC) is extracted and transformed independently. The case and file endpoints of GDC and PDC are queried via their publicly available API's to create case and file endpoint extracted data files(GDC case data, GDC file data, PDC case data, and PDC file data). Each extracted data file undergoes a transformation and aggregation step prior to being ready for merger with all of the other DCs transformed and aggregated data. GDC file data does not need to go through the aggregation step. PDC Files require an extra step to ensure that all Files have associated_project information. At this point, all data from GDC and PDC are in the harmonized data schema, and representative of Subject and File endpoints in the CDA data schema. IDC Subjects and Files endpoints data files are created using a single BigQuery query from one of IDC's available tables. The IDC data files do not require additional aggregation prior to being merged with GDC and PDC. All of the Subjects endpoint data files from each DC are then merged into a Subjects endpoint, and all of the Files endpoint files are merged into a Files endpoint. These two files are then uploaded to BigQuery as two separate tables. One for all Subjects and one for all Files. The CDA API can query from these two tables. An overview of the entire process can be seen in Figure 1 and will be described in more detail below.

| ![figure](./ETL_Figures/ETL_Fig1.png) |
|:---:|
| **Figure 1** |

### Current Flow of ETL

The extraction and transformation process for GDC and PDC data are very similar. For this reason, they are lumped together and explained in more detail in the next section. IDC extraction and transformation is a more straightforward process, but different than GDC and PDC. After all DC's have had data extracted and transformed, the relevant endpoint information is merged into two separate tables. A BigQuery schema is generated for each endpoint table since the autodetect feature will miss some fields in the tables, as well as not include field descriptions in the table. The transformed data files and schema files are needed to upload them as tables.

#### GDC/PDC Cases and Files Extraction and Transformation

| ![figure](./ETL_Figures/ETL_Fig2.png) |
|:---:|
| **Figure 2** |

The extraction process for each node and endpoint implements the publicly available APIs exposed by the nodes. All of the information that is used within CDA Release 3.1 for GDC has been obtained from the _cases_ and _files_ endpoints. Information from PDC is pulled from _cases_, _files_, _program_,  and _general_ endpoints. The resulting structure incorporates details about the case along with details about the specimens found within that case. The _files_ endpoints for GDC and PDC are used to get the files information and provide the link from files to associated specimens and cases.  In GDC, there are files that only link to cases, but any file that is linked to a specimen is also linked to the case that the specimen belongs to. In PDC, there are files that are not shown to be direcly associated with specimens or cases. This needs some more exploration but at the very least it looks like they are supplemental publication files associated directly with projects. For now, PDC files with no direct association with specimens or cases are filtered out prior to merging with the other DCs. The data files created by the extraction process are written with one case/**ResearchSubject** or file/**File** per line. These extracted data files are then submitted to the transformation code. The code reads the extracted data files line by line, and transforms each line into the data structure expected in our BigQuery tables.

Since the extracted data file and the output of the transform code are written as one case/**ResearchSubject** per line, whereas our data structure is on a **Subject** by **Subject** basis, further aggregation of the data is needed for the Subjects endpoint. The aggregation code searches for any entries in the transformed data which have identical ids (**Subject** level id) and aggregates those entries together. Currently, for the **Subject** endpoint, the demographic information is coalesced between cases, whereas the **ResearchSubject** records from different cases are appended. For the **File** endpoint, only PDC requires aggregation since Files can be present more than once in the initial extraction. The error logs for the individual DC examine the demographic data of two or more correlating **Subject**/**ResearchSubject** records and logs any discrepancy.

#### IDC Subjects and Files Extraction and Transformation

| ![figure](./ETL_Figures/ETL_Fig3.png) |
|:---:|
| **Figure 3** |

The extraction and transformation process of IDC data takes a more concise approach. One query for the Subjects endpoint is executed to extract all data from IDC and transform it into the CDA Subjects schema. A similar query is run for the creation of the Files endpoint data. Since IDC does not have demographic information, there is no need to do any logging of aggregation errors like that done in GDC and PDC. 



#### Merger of GDC, PDC, and IDC Data

| ![figure](./ETL_Figures/ETL_Fig4.png) |
|:---:|
| **Figure 4** |

The merging of data between GDC, PDC, and IDC is very similar to the aggregation step in the extraction and transformation sub-process for GDC and PDC. For the Subjects endpoint, the merge code searches the GDC, PDC, and IDC Subjects files for matching ids, coalesces the demographic information (GDC taking priority over PDC), and appends **ResearchSubject** and **File** records. An Inter-DC log consisting of discrepancies between GDC and PDC demographic information is created. For the Files endpoint, the merge code reads all of the **Subject** entity information created from the merged Subjects endpoint file just created, and replaces all **Subject** entities within the Files endpoint, with the information found in the merged Subjects endpoint file. The now merged Subjects and Files endpoint files are then uploaded to BigQuery as our Subjets and Files endpoint tables.

## Appendix

### GDC Extraction
#### Cases Endpoint Data
All the fields that are currently available from the GDC _cases_ endpoint ([GDC case fields](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/#case-fields)) are extracted, despite CDA only using a subset of them. The reason for this is that we intend to make full extraction files available to the cloud resources to aid in their own ETL processes. Luckily, all of the fields in the CDA Subjects endpoint are pulled from the _cases_ endpoint, and no cross-talk with the _files_ endpoint is needed. Unfortunately, the length of the query submitted to the GDC API has character length limits, so each page of cases pulled is broken into groups of these fields, and aggregated together

<table>
    <caption><b>Table 2</b>. JSON on the left represents raw data that is pulled from the GDC API using one group of fields from the _files_ endpoint. In the middle, is the raw data that is pulled from the GDC API using the second group of fields from the _files_ endpoint. On the right we can see the final, processed JSON that includes all data extracted for the file. The complete list of fields that are extracted can be found <a href="../../Schema/overview_mapping">here</a>.</caption>
<tr>
<th>GDC _files_ group 1</th>
<th>GDC _files_ group 2</th>
<th>GDC _files_ aggregated</th>
</tr>
<tr>
<td>
<pre>
{
  file_id: ghi,
  ...
  analysis: [...],
  annotation: {...},
  archive: [...],
  associated_entities: [...],
  cases: [...],
}
</pre>
</td>
<td>
<pre>
{
  file_id: ghi,
  center: {...},
  downstream_analysis: [...],
  index_files: [...],
}
</pre>
</td>
<td>
<pre>
{
  file_id: ghi,
  ...
  analysis: [...],
  annotation: {...},
  archive: [...],
  associated_entities: [...],
  cases: [...],
  center: {...},
  downstream_analysis: [...],
  index_files: [...],
}
</pre>
</td>
</tr>
</table>

#### Files Endpoint Data
All the fields that are currently available from the GDC _files_ endpoint ([GDC file fields](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/#file-fields)) are extracted, despite CDA only using a subset of them. The reason for this is that we intend to make full extraction files available to the cloud resources to aid in their own ETL processes. Luckily, all of the fields in the CDA Files endpoint are pulled from the _files_ endpoint, and no cross-talk with the _cases_ endpoint is needed. Unfortunately, the length of the query submitted to the GDC API has character length limits, so each page of file pulled is broken into groups of these fields, and aggregated together.

### PDC Extraction

To get the PDC data, eight graphQL queries were used:

* filesMetadata
* getPaginatedUIFile
* filesPerStudy
* allPrograms
* paginatedCaseDemographicsPerStudy
* paginatedCaseDiagnosesPerStudy
* paginatedCasesSamplesAliquots
* biospecimenPerStudy

Unfortunately there is no easy way to do a bulk extraction of all _cases_ with all wanted information from PDC. The options are to either ping the PDC API for each individual case, or to loop through all programs, projects, and studies, and use a series of queries per study to get information about the cases. We opted for the second option. A similar loop is used when using the filesPerStudy query when extracting PDC _files_. 

#### Extract All _Cases_ Information

The first query – allPrograms – is used to get all the available Programs and Studies. The extraction code loops over all Programs and Studies and performs several queries for each PDC study. Most queries are from the _cases_ endpoint and include paginatedCaseDemographicsPerStudy, paginatedCaseDiagnosesPerStudy, and paginatedCasesSamplesAliquots. They are used to gather the demographics, diagnoses, and specimen records for all cases within the study. The biospecimenPerStudy query is used solely to determine the taxon/species of the cases in the study. Due to extracting case information by PDC study, some case information is duplicated in the extracted file since cases can be seen in more than one PDC study. The result for a single PDC case record looks similar to:


```
{
  case_id: value,
  ...
  demographics: [...],
  diagnoses: [...],
  samples: [
    {
      ...
      aliquots: [
        {
          ...
        }
      ]
    }
  ],
}
```
The complete list of fields that are extracted can be found ##gdc_case_fields.txt in extraction folder <a href="../../Schema/overview_mapping">here</a>.

#### Extract All _Files_ Information
The extraction process for PDC _files_ uses several graphql queries to meet the needs of the cloud resources. For instance ISB-CGC and SevenBridges implement filesMetadata, but ISB-CGC uses filesPerStudy whereas SevenBridges uses getPaginatedUIFile. Due to this need, we implement bulk export of files info using filesMetadata, filesPerStudy, and getPaginatedUIFile. The filesMetadata and getPaginatedUIFile queries are simple paginated downloads of file information, and all fields available through those queries. The information for each query is written to separate output files for the cloud resources to use. The filesPerStudy query goes through a similar procedure as the _cases_ extraction, but only pulls the information from the filesPerStudy query for each study on PDC. This information is also written to a separate output file for the cloud resources to use. The PDC extraction code concatenates the filesMetadata and filesPerStudy output files for later use with CDA transformation.
<table>
    <caption><b>Table 3</b>. JSON on the left represents raw data that is pulled from the PDC API using the filesMetadata query. In the middle, is the raw data that is pulled from the GDC API using the getPaginatedUIFile query. On the right we can see the raw data pulled from the filesPerStudy query.
<tr>
<th>PDC filesMetadata info</th>
<th>PDC getPaginatedUIFile info</th>
<th>PDC filesPerStudy info</th>
</tr>
<tr>
<td>
<pre>
{
  file_id: value,
  file_name: value,
  file_location: value,
  md5sum: value,
  file_size: value,
  file_submitter_id: value,
  data_category: value,
  file_type: value,
  file_format: value,
  experiment_type: value,
  aliquots:[...],
}
</pre>
</td>
<td>
<pre>
{
  file_id: value,
  study_id: value,
  pdc_study_id: value,
  submitter_id_name: value,
  embargo_date: value,
  file_name: value,
  study_run_metadata_submitter_id: value,
  project_name: value,
  data_category: value,
  data_source: value,
  file_type: value,
  downloadable: value,
  access: value,
  md5sum: value,
  file_size: value,
}
</pre>
</td>
<td>
<pre>
{
  study_id: value,
  pdc_study_id: value,
  study_submitter_id: value,
  study_name: value,
  file_id: value,
  file_name: value,
  file_submitter_id: value,
  file_type md5sum: value,
  file_location: value,
  file_size: value,
  data_category: value,
  file_format: value,
  signedUrl: {...}
}
</pre>
</td>
</tr>
</table>

### GDC and PDC Transformation

Transformation in this section can for the most part be broken into two steps. The first transformation step has both structural and simple field name changes to the extracted data files. This first step implements mapping files for GDC _cases_/Subjects endpoint, GDC _files_/Files endpoint, PDC _cases_/Subjects endpoint, and PDC _files_/Files endpoint. The details of this process are slightly different for each DC and endpoint, however the end result is the same. Each entry in the resultant Subjects file still correlates to a case/**ResearchSubject**, but is in an equivalent structure to the final schema where each entry will correspond to a Subject. In this file, Subjects may correspond to multiple entries and must be aggregated together. Each entry in the resultant Files file correlates to a file/**File**. For GDC no aggregation is required at the top level, but for PDC aggregation is needed due to files being returned in both filesMetadata and filesPerStudy queries.

The second step aggregates Subjects together from the same DC. In the Subjects file, for all entries that belong to the same **Subject**, the **ResearchSubject** records are appended underneath the same **Subject** entity. PDC files must also under go a similar aggregation step where any entries that belong to the same **File** are aggregated together. After this step, the data from each DC is in a common data format and ready for merging.

For this section, the DC’s are similar enough that the differences can be shown with the aforementioned mapping from GDC/PDC fields to the common data format found <a href="../../Schema/overview_mapping">here</a>.


##### step 1: Transformation

For GDC and PDC, we iterate over every entry from the extracted data files and make specific changes to that entry. For the Subjects file, these include creating a top **Subject** level of data which correlates to the **Subject** entity. From there, the specific case information is recorded in a **ResearchSubject** entity, and transformations to the fields are changed to align best with the [CDA model](../Schema/overview_mapping.md). At the end of this transformation step, each entry is still representative of a case, now known as a **ResearchSubject**, but has **Subject** level information. A simplified example of an entry is given below in Table 4.

<table>
    <caption><b>Table 4</b></caption>
<tr>
<th>Case Entry 1</th>
<th>Transformed Case Entry 1</th>
</tr>
<tr>
<td>
<pre>
{
  submitter_id: S1
  case_id: C3
  demographics:
    {days_to_birth: 45}
  primary_disease_site: Brain
  samples:
    {sample_id: samp_1
    }
}
</pre>
</td>
<td>
<pre>
{
  id: S1
  days_to_birth: 45
  ResearchSubject:
    {id: C3
    primary_disease_site: Brain
    Specimen:
      {id: samp_1,
      }
    }
}
</pre>
</td>
</tr>
</table>

Much like the Subjects file, the transformation of the Files file includes creating a top **File** level of data which correlates to the **File** entity as defined by the [CDA model](../Schema/overview_mapping.md). At the end of this transformation step, each entry within the **File**, however for PDC some **File** entities are recorded multiple times within the data file. They will require further aggregation.

<table>
    <caption><b>Table 5</b></caption>
<tr>
<th>File Entry 1</th>
<th>Transformed File Entry 1</th>
</tr>
<tr>
<td>
<pre>
{
  file_id: file_1.txt
  cases:
    [
      {case_id: case_1,
       submitter_id: S1,
      },
      {case_id: case_2,
       submitter_id: S1,
      }
    ],
  associated_entities:
    [
      {entity_id: sample1},
      {entity_id: sample2}
    ]
}
</pre>
</td>
<td>
<pre>
{
  id: file_1.txt
  Subjects:
    [ S1 ]
  ResearchSubjects:
    [ case_1, case_2]
  Specimens:[sample1, sample2]
}
</pre>
</td>
</tr>
</table>

##### step 2: Aggregation

At this point for the transformed Subjects file, a list of Subjects and corresponding ResearchSubjects is made, and any **Subject** with multiple **ResearchSubject** records has the **ResearchSubject** records appended (with duplicates removed from **File** (and **ResearchSubject** in PDC)) under a single entry for the **Subject**. A simplified example of this aggregation can be seen in Table 6 below.

<table>
    <caption><b>Table 6</b></caption>
<tr>
<th>Transformed Subject Entry 1</th>
<th>Transformed Subject Entry 2</th>
<th>Aggregated</th>
</tr>
<tr>
<td>
<pre>
{
  id: S1
  days_to_birth: 45
  subject_associated_project: [project1]
  ResearchSubject:
    {id: C3
    primary_disease_site: Brain
    member_of_research_project: project1
    Specimen:
      {id: samp_1,
      }
    }
}
</pre>
</td>
<td>
<pre>
{
  id: S1
  days_to_birth: 45
  subject_associated_project: [project2]
  ResearchSubject:
    {id: C7
    primary_disease_site: Brain
    member_of_research_project: project2
    Specimen:
      {id: samp_4,
      }
    }
}
</pre>
</td>
<td>
<pre>
{
  id: S1
  days_to_birth: 45
  subject_associated_project: [project1, project2]
  ResearchSubject:
    {id: C3
    primary_disease_site: Brain
    member_of_research_project: project1
    Specimen:
      {id: samp_1
      }
    },
    {id: C7
    primary_disease_site: Brain
    member_of_research_project: project2
    Specimen:
      {id: samp_4
      }
    }
}
</pre>
</td>
</tr>
</table>

Transformed Subject Entry 1 and 2 are aggregated in this example. Transformed Subject Entry 1 and 2 both correspond to the **Subject** with the id ‘S1’, but have different **ResearchSubject** records. The aggregated entry appended the **ResearchSubject** records together and appended the subject_associated_project records together. 

Similarly, PDC **Files** must be aggregated. A **File** may appear in both the filesMetadata and filesPerStudy query. A simplified example of this aggregation can be seen in Table 7 below.

<table>
    <caption><b>Table 7</b></caption>
<tr>
<th>Transformed File Entry 1</th>
<th>Transformed File Entry 2</th>
<th>Aggregated</th>
</tr>
<tr>
<td>
<pre>
{
  id: File1
  associated_project: null
  Subjects: [S1, S1, S2],
  ResearchSubjects: [RS2, RS2, RS3],
  Specimens:[samp_1],
}
</pre>
</td>
<td>
<pre>
{
  id: File1
  associated_project: project1
  Subjects: [],
  ResearchSubjects: [],
  Specimens:[],
}
</pre>
</td>
<td>
<pre>
{
  id: File1
  associated_project: project1
  Subjects: [S1, S1, S2],
  ResearchSubjects: [RS2, RS2, RS3],
  Specimens:[samp_1],
}
</pre>
</td>
</tr>
</table>

### IDC Extraction and Transformation

For Release 3.1, the IDC extraction and transformation process are executed using one query. This is possible due to IDC making their data available on BigQuery, as well as other features of BigQuery including temporary functions, array aggregation of structured data, and grouping data by particular fields (id, species, etc.). The queries currently used for the Subjects and Files endpoints are:
```
# Subject Endpoint Query
CREATE TEMP FUNCTION
  idc_species_mapping(x STRING)
  RETURNS STRING AS (CASE x
      WHEN 'Human' THEN 'homo sapiens'
      WHEN 'Canine' THEN 'canis familiaris'
      WHEN 'Mouse' THEN 'mus musculus'
    ELSE
    ''
  END
    );
CREATE TEMP FUNCTION
  idc_researchsubject_id(x STRING,
    y STRING)
  RETURNS STRING AS (CONCAT(x, "__", y));
CREATE TEMP FUNCTION
  idc_label(x STRING)
  RETURNS STRING AS (ARRAY_REVERSE(SPLIT(x, '/'))[
  OFFSET
    (0)]);
CREATE TEMP FUNCTION
  idc_drs_uri(x STRING)
  RETURNS STRING AS (CONCAT("drs://dg.4DFC:", x));
SELECT
  PatientID AS id,
  [STRUCT('IDC' AS system,
    PatientID AS value)] AS identifier,
  idc_species_mapping(tcia_species) AS species,
  STRING(NULL) AS sex,
  STRING(NULL) AS race,
  STRING(NULL) AS ethnicity,
  NULL AS days_to_birth,
  [collection_id] AS subject_associated_project,
  STRING(NULL) AS vital_status,
  NULL AS days_to_death,
  STRING(NULL) AS cause_of_death,
  [STRUCT(idc_researchsubject_id(PatientID,
      collection_id) AS id,
    [STRUCT('IDC' AS system,
      idc_researchsubject_id(PatientID,
        collection_id) AS value)] AS identifier,
    collection_id AS member_of_research_project,
    STRING(NULL) AS primary_diagnosis_condition,
    tcia_tumorLocation AS primary_diagnosis_site)] AS ResearchSubject
FROM
  `bigquery-public-data.idc_v10.dicom_pivot_v10`
GROUP BY
  id,
  species,
  collection_id,
  tcia_tumorLocation
```
```
# File Endpoint Query
CREATE TEMP FUNCTION
  idc_species_mapping(x STRING)
  RETURNS STRING AS (CASE x
      WHEN 'Human' THEN 'homo sapiens'
      WHEN 'Canine' THEN 'canis familiaris'
      WHEN 'Mouse' THEN 'mus musculus'
    ELSE
    ''
  END
    );
CREATE TEMP FUNCTION
  idc_researchsubject_id(x STRING,
    y STRING)
  RETURNS STRING AS (CONCAT(x, "__", y));
CREATE TEMP FUNCTION
  idc_label(x STRING)
  RETURNS STRING AS (ARRAY_REVERSE(SPLIT(x, '/'))[
  OFFSET
    (0)]);
CREATE TEMP FUNCTION
  idc_drs_uri(x STRING)
  RETURNS STRING AS (CONCAT("drs://dg.4DFC:", x));
SELECT
  crdc_instance_uuid AS id,
  [STRUCT('IDC' AS system,
    crdc_instance_uuid AS value)] AS identifier,
  idc_label(gcs_url) AS label,
  'Imaging' AS data_category,
  STRING(NULL) AS data_type,
  'DICOM' AS file_format,
  [collection_id] AS associated_project,
  idc_drs_uri(crdc_instance_uuid) AS drs_uri,
  NULL AS byte_size,
  STRING(NULL) AS checksum,
  'Imaging' AS data_modality,
  Modality AS imaging_modality,
  STRING(NULL) AS dbgap_accession_number,
  crdc_series_uuid AS imaging_series,
  ARRAY_AGG(PatientID) AS Subjects,
  ARRAY_AGG(idc_researchsubject_id(PatientID,
      collection_id)) AS ResearchSubjects,
  ARRAY<STRING>[] AS Specimens
FROM
  `bigquery-public-data.idc_v10.dicom_pivot_v10`
GROUP BY
  id,
  gcs_url,
  Modality,
  collection_id,
  PatientID,
  tcia_species,
  tcia_tumorLocation,
  crdc_series_uuid
```

#### Temp Functions

The temporary functions created include `idc_species_mapping`, `idc_researchsubject_id`, `idc_label`, and `idc_drs_uri`. These functions are used to transform the IDC fields `tcia_species`, `PatientID`, `collection_id`, `gcs_url`, and `crdc_instance_uuid` to the CDA data schema fields `species`, `ResearchSubject.id`/`ResearchSubjects`, `File.label`, and `File.drs_uri`. As more fields become available, and more transformations are necessary, more temporary functions will be added.

#### SELECT ‘x’ AS ‘y’

Due to the nature of the query, all fields desired in the CDA schema must be specified. The query is built using a mapping file similar to the GDC and PDC mapping files. If it is a direct mapping such as `PatientID` to id, then simply `PatientID` AS id works. For fields that require some type of transformation like `File.label` or `species`, the function is added to the query (eg `idc_species_mapping(tcia_species)` AS `species`). For integer type fields that have no mapping to IDC, `NULL` is mapped and for string type fields, `STRING(NULL)` is mapped. Any fields that have a string mapped to a field will be populated by the string listed (eg. 'DICOM' AS `file_format`). The IDC mapping file can be found [here](https://github.com/CancerDataAggregator/transform/blob/integration/IDC_mapping.yml).

#### FROM and GROUP BY

This statement selects which table from IDC to query from, as well as how to aggregate the data. It is grouped by `id` (**Subject** level `identifier`), then `species` and `collection_id` to keep with proper BigQuery formatting.

### Merge
#### Subjects Endpoint Merger
After the data from GDC, PDC, and IDC have been transformed into a common data format, merging the data together can begin. For the Subjects endpoint, **Subject** level info is coalesced, and any data from records in **ResearchSubject** are simply appended underneath the same **Subject**, and the **Subject** Files lists are appended together. A simplified example of the merge between GDC, PDC, and IDC data can be seen in Table 7.

<table>
    <caption><b>Table 7</b>. Simplified example of a merger between GDC, PDC, and IDC</caption>
<tr>
<th>GDC</th>
<th>PDC</th>
<th>IDC</th>
<th>Merged</th>
</tr>
<tr>
<td>
<pre>
{
  id: A
  days_to_birth: 23
  race: None
  sex: M
  subject_associated_project: ['PROJ-A']
  ResearchSubject:
    {id: A1
    ...
    }
    {id: A2
    ...
    }
}
</pre>
</td>
<td>
<pre>
{
  id: A
  days_to_birth: None
  race: Caucasian
  sex: F
  subject_associated_project: ['PROJ-B']
  ResearchSubject:
    {id: B4
    ...
    }
    {id: B5
    ...
    }
}
</pre>
</td>
<td>
<pre>
{
  id: A
  days_to_birth:
  race:
  sex:
  subject_associated_project: ['proj_a']
  ResearchSubject:
    {id: I3
    ...
    }
}
</pre>
</td>
<td>
<pre>
{
  id: A
  days_to_birth: 23
  race: Caucasian
  sex: M
  subject_associated_project: ['PROJ-A', 'PROJ-B','proj_a']
  ResearchSubject:
    {id: A1
    ...
    }
    {id: A2
    ...
    }
    {id: B4
    ...
    }
    {id: B5
    ...
    }
}
</pre>
</td>
</tr>
</table>

##### Subject level merge

The fields at the **Subject** level are merged based on coalescing or appending data. For coalescing, the code looks for values in GDC, then PDC, and then IDC until a value is found. The first value found is used in the merged data. (if there is conflicting data, this is logged). In Figure 2, id under **Subject** must be the same to consider merging data. The example for days_to_birth shows that GDC has a value of 23, whereas PDC and IDC show none. Since GDC has a populated value, the value from GDC is stored as the value for days_to_birth. Similarly, for race, GDC has no recorded value but PDC has a value of ‘Caucasian’. Since GDC is empty, and PDC has a value, the value from PDC is stored. The next example shows conflicting data between GDC and PDC. GDC records sex as ‘M’ whereas PDC records it as ‘F’. Due to conflicting information, this instance is recorded in a log, but the GDC value of ‘M’ is used in the merged data. Finally for the subject_associated_project field, all values from GDC, PDC and IDC are appended into a single list.

##### ResearchSubject level append

Looking at Table 7, in the merged data, all of the records from **ResearchSubject** from GDC and PDC are appended. At this time there is no equivalent **ResearchSubject** entity available for IDC data. Currently no merging happens at this level.

##### File level append

Looking at Table 7, in the merged data, all of the records from **File** from GDC, PDC, and IDC are appended. Currently no merging happens at this level.

For the Subjects endpoint, **Subject** level info is coalesced, and any data from records in **ResearchSubject** are simply appended underneath the same **Subject**, and the **Subject** Files lists are appended together. A simplified example of the merge between GDC, PDC, and IDC data can be seen in Table 7.

<table>
    <caption><b>Table 7</b>. Simplified example of a merger between GDC, PDC, and IDC</caption>
<tr>
<th>GDC</th>
<th>PDC</th>
<th>IDC</th>
<th>Merged</th>
</tr>
<tr>
<td>
<pre>
{
  id: A
  days_to_birth: 23
  race: None
  sex: M
  ResearchSubject:
    {id: A1
    ...
    }
    {id: A2
    ...
    }
  Files: [file_G1.doc]
}
</pre>
</td>
<td>
<pre>
{
  id: A
  days_to_birth: None
  race: Caucasian
  sex: F
  ResearchSubject:
    {id: B4
    ...
    }
    {id: B5
    ...
    }
  Files: [file_P1.doc]
}
</pre>
</td>
<td>
<pre>
{
  id: A
  days_to_birth:
  race:
  sex:
  Files: [file_I1.doc]
}
</pre>
</td>
<td>
<pre>
{
  id: A
  days_to_birth: 23
  race: Caucasian
  sex: M
  ResearchSubject:
    {id: A1
    ...
    }
    {id: A2
    ...
    }
    {id: B4
    ...
    }
    {id: B5
    ...
    }
  Files: [file_G1.doc, file_P1.doc, file_I1.doc]
}
</pre>
</td>
</tr>
</table>

#### Files Endpoint Merger ####

Since there are no shared files between any of the DC's, no top level **File** information can be merged. A simple concatenation of input files is all that is necessary. Hooray!
