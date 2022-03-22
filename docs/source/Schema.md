# Schema and Mapping
## Subjects Endpoint
### Full Schema

The **Subject** entity is the outer most record in the Subjects endpoint. Within the **Subject** record are the fields for the **Subject** (demographic and other subject-specific information), a Files field which lists the id of all files associated with the **Subject**, as well as the record of all **ResearchSubject** records associated with that **Subject**. Each **ResearchSubject** record has fields associated with the **ResearchSubject**, as well as records for the **Diagnosis** and **Specimen** entities associated with that **ResearchSubject**, and so on.
 

| [Subject](#subject_S) |                                 |                              |                               |                            |
| ------- | ------------------------------------------- | ---------------------------- | ----------------------------- | -------------------------- |
|         | id                                          |                              |                               |                            |
|         | identifier.system                           |                              |                               |                            |
|         | identifier.value                            |                              |                               |                            |
|         | species                                     |                              |                               |                            |
|         | sex                                         |                              |                               |                            |
|         | race                                        |                              |                               |                            |
|         | ethnicity                                   |                              |                               |                            |
|         | days\_to\_birth                             |                              |                               |                            |
|         | subject\_associated\_project                |                              |                               |                            |
|         | vital\_status                               |                              |                               |                            |
|         | age\_at\_death                              |                              |                               |                            |
|         | cause\_of\_death                            |                              |                               |                            |
|         | Files                                       |                              |                               |                            |
|         | **[ResearchSubject](#researchsubject_S):**    |                              |                               |                            |
|         |                                             | id                           |                               |                            |
|         |                                             | identifier.system            |                               |                            |
|         |                                             | identifier.value             |                               |                            |
|         |                                             | primary\_diagnosis\_condition|                               |                            |
|         |                                             | primary\_diagnosis\_site     |                               |                            |
|         |                                             | member\_of\_research\_project|                               |                            |
|         |                                             | **[Diagnosis](#diagnosis):** |                               |                            |
|         |                                             |                              | id                            |                            |
|         |                                             |                              | identifier.system             |                            |
|         |                                             |                              | identifier.value              |                            |
|         |                                             |                              | primary\_diagnosis            |                            |
|         |                                             |                              | age\_at\_diagnosis            |                            |
|         |                                             |                              | morphology                    |                            |
|         |                                             |                              | stage                         |                            |
|         |                                             |                              | grade                         |                            |
|         |                                             |                              | method\_of\_diagnosis         |                            |
|         |                                             |                              | **[Treatment](#treatment):**  |                            |
|         |                                             |                              |                               | id                         |
|         |                                             |                              |                               | identifier.system          |
|         |                                             |                              |                               | identifier.value           |
|         |                                             |                              |                               | treatment\_type            |
|         |                                             |                              |                               | treatment\_outcome         |
|         |                                             |                              |                               | days\_to\_treatment\_start |
|         |                                             |                              |                               | days\_to\_treatment\_end   |
|         |                                             |                              |                               | therapeutic\_agent         |
|         |                                             |                              |                               | treatment\_anatomic\_site  |
|         |                                             |                              |                               | treatment\_effect          |
|         |                                             |                              |                               | treatment\_end\_reason     |
|         |                                             |                              |                               | number\_of\_cycles         |
|         |                                             | Files                        |                               |                            |
|         |                                             | **[Specimen](#specimen):**   |                               |                            |
|         |                                             |                              | id                            |                            |
|         |                                             |                              | identifier.system             |                            |
|         |                                             |                              | identifier.value              |                            |
|         |                                             |                              | associated\_project           |                            |
|         |                                             |                              | age\_at\_collection           |                            |
|         |                                             |                              | primary\_disease\_type        |                            |
|         |                                             |                              | anatomical\_site              |                            |
|         |                                             |                              | source\_material\_type        |                            |
|         |                                             |                              | specimen\_type                |                            |
|         |                                             |                              | derived\_from\_specimen       |                            |
|         |                                             |                              | derived\_from\_subject        |                            |
|         |                                             |                              | Files                         |                            |

### Mapping
#### <a name="subject_S"></a>Subject
| Common Data Format (present in CDA) | GDC field name                                                         | PDC field name                     | IDC field name                   |
| ----------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | -------------------------------- |
| id                                  | case.submitter\_id                                                     | cases.case\_submitter\_id          | files.PatientID                  |
| identifier.system                   | GDC                                                                    | PDC                                | IDC                              |
| identifier.value                    | case.submitter\_id                                                     | cases.case\_submitter\_id          | files.PatientID                  |
| species                             | Homo sapiens                                                           | cases.taxon                        | files.tcia\_species              |
| sex                                 | case.demographic.gender                                                | cases.demographics.gender          | No available mapping             |
| race                                | case.demographic.race                                                  | cases.demographics.race            | No available mapping             |
| ethnicity                           | case.demographic.ethnicity                                             | cases.demographics.ethnicity       | No available mapping             |
| days\_to\_birth                     | case.demographic.days\_to\_birth                                       | cases.demographics.days\_to\_birth | No available mapping             |
| subject\_associated\_project        | Create array of all projects for all ResearchSubjects for this Subject |                                    | files.collection\_id             |
| vital\_status	                      | case.demographic.vital\_status	                                        | cases.demographic.vital\_status    | No available mapping             |
| age\_at\_death	                     | case.demographic.days\_to\_death	                                      | cases.demographic.days\_to\_death  | No available mapping             |
| cause\_of\_death	                   | case.demographic.cause\_of\_death	                                     | cases.demographic.cause\_of\_death | No available mapping             |
| Files                               | Create array of all associated File ids for this Subject               |                                    |                                  |
| [ResearchSubject](#researchsubject_F) |                                                                        |                                    | No ResearchSubject entity in IDC |

#### <a name="researchsubject_S"></a>ResearchSubject
| Common Data Format (present in CDA) | GDC field name             | PDC field name               | IDC field name |
| ----------------------------------- | -------------------------- | ---------------------------- | -------------- |
| id                                  | cases.case\_id             | cases.case\_id               | Not Applicable |
| identifier.system                   | GDC                        | PDC                          |                |
| identifier.value                    | cases.case\_id             | cases.case\_id               |                |
| primary\_diagnosis\_condition       | cases.disease\_type        | cases.disease\_type          |                |
| primary\_diagnosis\_site            | cases.primary\_site        | cases.primary\_site          |                |
| member\_of\_research\_project       | cases.project.project\_id  | cases.project\_submitter\_id |                |
| Files                               | Create array of all associated File ids for this ResearchSubject           |
| [Diagnosis](#diagnosis)             |                            |                              |                |
| [Specimen](#specimen)               |                            |                              |                |

#### Diagnosis
| Common Data Format (present in CDA) | GDC field name                       | PDC field name                       | IDC field name |
| ----------------------------------- | ------------------------------------ | ------------------------------------ | -------------- |
| id                                  | cases.diagnoses.diagnosis\_id        | cases.diagnoses.diagnosis\_id        | Not applicable |
| identifier.system                   | GDC                                  | PDC                                  |                |
| identifier.value                    | cases.diagnoses.diagnosis\_id        | cases.diagnoses.diagnosis\_id        |                |
| primary\_diagnosis                  | cases.diagnoses.primary\_diagnosis   | cases.diagnoses.primary\_diagnosis   |                |
| age\_at\_diagnosis                  | cases.diagnoses.age\_at\_diagnosis   | cases.diagnoses.age\_at\_diagnosis   |                |
| morphology                          | cases.diagnoses.morphology           | cases.diagnoses.morphology           |                |
| grade                               | cases.diagnoses.tumor\_grade         | cases.diagnoses.tumor\_grade         |                |
| stage                               | cases.diagnoses.tumor\_stage         | cases.diagnoses.tumor\_stage         |                |
| method\_of\_diagnosis	              | cases.diagnosis.method\_of\_diagnosis|	cases.diagnosis.method\_of\_diagnosis|                |
|                                     |                                      |                                      |                |
| [Treatment](#treatment)             |                                      |                                      |                |

#### Treatment
| Common Data Format (present in CDA) | GDC field name                                      | PDC field name                                        | IDC field name |
| ----------------------------------- | --------------------------------------------------- | ----------------------------------------------------- | -------------- |
| id                                  | cases.diagnoses.treatments.treatment\_id            | cases.diagnoses.treatments.treatment\_id              | Not applicable |
| identifier.system                   | GDC                                                 | PDC                                                   |                |
| identifier.value                    | cases.diagnoses.treatments.treatment\_id            | cases.diagnoses.treatments.treatment\_id              |                |
| treatment\_type                     | cases.diagnoses.treatments.treatment\_type          | cases.diagnoses.treatments.treatment\_type            |                |
| treatment\_outcome                  | cases.diagnoses.treatments.treatment\_outcome       | cases.diagnoses.treatments. treatment\_outcome        |                |
| days\_to\_treatment\_start          | cases.diagnoses.treatments.days\_to\_treatment      | cases.diagnoses.treatments.days\_to\_treatment\_start |                |
| days\_to\_treatment\_end            | cases.diagnoses.treatments.days\_to\_treatment_end  | cases.diagnoses.treatments.days\_to\_treatment\_end   |                |
| therapeutic\_agent	                 | cases.diagnoses.treatments.therapeutic\_agents	     | cases.diagnoses.treatments.therapeutic\_agents        |                |
| treatment\_anatomic\_site	          | cases.diagnoses.treatments.treatment\_anatomic\_site|	cases.diagnoses.treatments.treatment\_anatomic\_site  |                |
| treatment\_effect	                  | cases.diagnoses.treatments.treatment\_effect	       | cases.diagnoses.treatments.treatment\_effect          |                |
| treatment\_end\_reason	             | cases.diagnoses.treatments.reason\_treatment\_ended	| cases.diagnoses.treatments.reason\_treatment\_ended   |                | 
| number\_of\_cycles	                 | cases.diagnoses.treatments.number\_of\_cycles	      | cases.diagnoses.treatments.number\_of\_cycles         |                |

#### Specimen
| Common Data Format (present in CDA) | GDC field name                                       | PDC field name                            | IDC field name |
| ----------------------------------- | ---------------------------------------------------- | ----------------------------------------- | -------------- |
| id                                  | cases.samples.sample\_id                             | cases.samples.sample\_id                  | Not applicable |
|                                     | cases.samples.portions.portion\_id                   | cases.samples.aliquots.aliquot\_id        |                |
|                                     | cases.samples.portions.slide\_id                     |                                           |                |
|                                     | cases.samples.portions.analytes.analyte\_id          |                                           |                |
|                                     | cases.samples.portions.analytes.aliquots.aliquot\_id |                                           |                |
| identifier.system                   | GDC                                                  | PDC                                       |                |
| identifier.value                    | cases.samples.sample\_id                             | cases.samples.sample\_id                  |                |
|                                     | cases.samples.portions.portion\_id                   | cases.samples.aliquots.aliquot\_id        |                |
|                                     | cases.samples.portions.slide\_id                     |                                           |                |
|                                     | cases.samples.portions.analytes.analyte\_id          |                                           |                |
|                                     | cases.samples.portions.analytes.aliquots.aliquot\_id |                                           |                |
| associated\_project                 | cases.project.project\_id                            | cases.project\_submitter\_id              |                |
| age\_at\_collection                 | cases.demographic.days\_to\_birth                    | cases.demographics.days\_to\_birth        |                |
| derived\_from\_subject              | cases.submitter\_id                                  | cases.case\_submitter\_id                 |                |
| primary\_disease\_type              | cases.disease\_type                                  | cases.disease\_type                       |                |
| anatomical\_site                    | cases.samples.biospecimen\_anatomic\_site            | cases.samples.biospecimen\_anatomic\_site |                |
| source\_material\_type              | cases.samples.sample\_type                           | cases.samples.sample\_type                |                |
| specimen\_type                      | sample, portion, slide, analyte, aliquot             | sample, aliquot                           |                |
| derived\_from\_specimen             | cases.samples.sample\_id                             | cases.samples.sample\_id                  |                |
|                                     | cases.samples.portions.portion\_id                   |                                           |                |
|                                     | cases.samples.portions.analytes.analyte\_id          |                                           |                |
| derived\_from\_subject              | cases.submitter\_id                                  | cases.case\_submitter\_id                 |                |
| Files                               | Create array of all associated File ids for this Specimen |                                           |                |

## Files Endpoint
### Full Schema

The **File** entity is the outer most record in the Files endpoint. Within the **File** record are the fields for the **File** (file metadata), as well as the record of all **Subject**, **ResearchSubject**, and **Specimen** records associated with that **File**. Each of the entities previously mentioned has fields associated with those entities.

| [File](#File) |                                 |                              |                               |                            |
| ------- | ------------------------------------------- | ---------------------------- | ----------------------------- | -------------------------- |
|         | id                           |                               |                            |
|         | identifier.system            |                               |                            |
|         | identifier.value             |                               |                            |
|         | label                        |                               |                            |
|         | data\_category               |                               |                            |
|         | data\_type                   |                               |                            |
|         | file\_format                 |                               |                            |
|         | associated\_project          |                               |                            |
|         | drs\_uri                     |                               |                            |
|         | byte\_size                   |                               |                            |
|         | checksum                     |                               |                            |
|         | data\_modality               |                               |                            |
|         | imaging\_modality            |                               |                            |
|         |  dbgap\_accession\_number    |                               |
|         | **[Subject](#subject_F):**   |                               |
|         |                              | id                                          |                              |                               |                            
|         |                              | identifier.system                           |                              |                               |                            
|         |                              | identifier.value                            |                              |                               |                            
|         |                              | species                                     |                              |                               |                            
|         |                              | sex                                         |                              |                               |                            
|         |                              | race                                        |                              |                               |                            
|         |                              | ethnicity                                   |                              |                               |                            
|         |                              | days\_to\_birth                             |                              |                               |                            
|         |                              | subject\_associated\_project                |                              |                               |                            
|         |                              | vital\_status                               |                              |                               |                            
|         |                              | age\_at\_death                              |                              |                               |                            
|         |                              | cause\_of\_death                            |                              |                               |                            
|         | **[ResearchSubject](#researchsubject_F):**  |                              |                               |                            |
|         |                                             | id                           |                               |                            |
|         |                                             | identifier.system            |                               |                            |
|         |                                             | identifier.value             |                               |                            |
|         |                                             | primary\_diagnosis\_condition|                               |                            |
|         |                                             | primary\_diagnosis\_site     |                               |                            |
|         |                                             | member\_of\_research\_project|                               |                            |
|         |                                             | **[Diagnosis](#diagnosis_F):** |                               |                            |
|         |                                             |                              | id                            |                            |
|         |                                             |                              | identifier.system             |                            |
|         |                                             |                              | identifier.value              |                            |
|         |                                             |                              | primary\_diagnosis            |                            |
|         |                                             |                              | age\_at\_diagnosis            |                            |
|         |                                             |                              | morphology                    |                            |
|         |                                             |                              | stage                         |                            |
|         |                                             |                              | grade                         |                            |
|         |                                             |                              | method\_of\_diagnosis         |                            |
|         |                                             |                              | **[Treatment](#treatment_F):**  |                            |
|         |                                             |                              |                               | id                         |
|         |                                             |                              |                               | identifier.system          |
|         |                                             |                              |                               | identifier.value           |
|         |                                             |                              |                               | treatment\_type            |
|         |                                             |                              |                               | treatment\_outcome         |
|         |                                             |                              |                               | days\_to\_treatment\_start |
|         |                                             |                              |                               | days\_to\_treatment\_end   |
|         |                                             |                              |                               | therapeutic\_agent         |
|         |                                             |                              |                               | treatment\_anatomic\_site  |
|         |                                             |                              |                               | treatment\_effect          |
|         |                                             |                              |                               | treatment\_end\_reason     |
|         |                                             |                              |                               | number\_of\_cycles         |
|         |**[Specimen](#specimen_F):**                 |                              |                               |                            |
|         |                                             | id                           |                               |
|         |                                             | dentifier.system             |                              |
|         |                                             | identifier.value             |                            |
|         |                                             | associated\_project          |                            |
|         |                                             | age\_at\_collection          |                            |
|         |                                             | primary\_disease\_type       |                            |
|         |                                             | anatomical\_site             |                            |
|         |                                             | source\_material\_type       |                            |
|         |                                             | specimen\_type               |                            |
|         |                                             | derived\_from\_specimen      |                            |
|         |                                             | derived\_from\_subject       |                            |
  
### Mapping
#### File
#### <a name="subject_F"></a>Subject
| Common Data Format (present in CDA) | GDC field name                                                         | PDC field name                     | IDC field name                   |
| ----------------------------------- | ---------------------------------------------------------------------- | ---------------------------------- | -------------------------------- |
| id                                  | file.case.submitter\_id                                                | files.cases.case\_submitter\_id    | files.PatientID                  |
| identifier.system                   | GDC                                                                    | PDC                                | IDC                              |
| identifier.value                    | file.case.submitter\_id                                                | files.cases.case\_submitter\_id          | files.PatientID                  |
| species                             | Homo sapiens                                                           | cases.taxon                        | files.tcia\_species              |
| sex                                 | file.case.demographic.gender                                           | cases.demographics.gender          | No available mapping             |
| race                                | file.case.demographic.race                                             | cases.demographics.race            | No available mapping             |
| ethnicity                           | file.case.demographic.ethnicity                                        | cases.demographics.ethnicity       | No available mapping             |
| days\_to\_birth                     | file.case.demographic.days\_to\_birth                                  | cases.demographics.days\_to\_birth | No available mapping             |
| subject\_associated\_project        | Create array of all projects for all ResearchSubjects for this Subject |                                    | files.collection\_id             |
| vital\_status	                      | file.case.demographic.vital\_status	                                   | cases.demographic.vital\_status    | No available mapping             |
| age\_at\_death	                     | file.case.demographic.days\_to\_death	                                 | cases.demographic.days\_to\_death  | No available mapping             |
| cause\_of\_death	                   | file.case.demographic.cause\_of\_death	                                | cases.demographic.cause\_of\_death | No available mapping             |

#### <a name="researchsubject_F"></a>ResearchSubject
| Common Data Format (present in CDA) | GDC field name             | PDC field name               | IDC field name |
| ----------------------------------- | -------------------------- | ---------------------------- | -------------- |
| id                                  | file.cases.case\_id        | files.cases.case\_id         | Not Applicable |
| identifier.system                   | GDC                        | PDC                          |                |
| identifier.value                    | file.cases.case\_id        | files.cases.case\_id         |                |
| primary\_diagnosis\_condition       | file.cases.disease\_type   | cases.disease\_type          |                |
| primary\_diagnosis\_site            | file.cases.primary\_site   | cases.primary\_site          |                |
| member\_of\_research\_project       | file.cases.project.project\_id | cases.project\_submitter\_id |                |
| [Diagnosis](#diagnosis_F)           |                            |                              |                |

#### <a name="diagnosis_F"></a>Diagnosis
| Common Data Format (present in CDA) | GDC field name                       | PDC field name                       | IDC field name |
| ----------------------------------- | ------------------------------------ | ------------------------------------ | -------------- |
| id                                  | file.cases.diagnoses.diagnosis\_id   | cases.diagnoses.diagnosis\_id        | Not applicable |
| identifier.system                   | GDC                                  | PDC                                  |                |
| identifier.value                    | file.cases.diagnoses.diagnosis\_id        | cases.diagnoses.diagnosis\_id        |                |
| primary\_diagnosis                  | file.cases.diagnoses.primary\_diagnosis   | cases.diagnoses.primary\_diagnosis   |                |
| age\_at\_diagnosis                  | file.cases.diagnoses.age\_at\_diagnosis   | cases.diagnoses.age\_at\_diagnosis   |                |
| morphology                          | file.cases.diagnoses.morphology           | cases.diagnoses.morphology           |                |
| grade                               | file.cases.diagnoses.tumor\_grade         | cases.diagnoses.tumor\_grade         |                |
| stage                               | file.cases.diagnoses.tumor\_stage         | cases.diagnoses.tumor\_stage         |                |
| method\_of\_diagnosis	              | file.cases.diagnosis.method\_of\_diagnosis|	cases.diagnosis.method\_of\_diagnosis|                |
| [Treatment](#treatment_F)           |                                      |                                      |                |

#### <a name="treatment_F"></a>Treatment
| Common Data Format (present in CDA) | GDC field name                                      | PDC field name                                        | IDC field name |
| ----------------------------------- | --------------------------------------------------- | ----------------------------------------------------- | -------------- |
| id                                  | cases.diagnoses.treatments.treatment\_id            | cases.diagnoses.treatments.treatment\_id              | Not applicable |
| identifier.system                   | GDC                                                 | PDC                                                   |                |
| identifier.value                    | cases.diagnoses.treatments.treatment\_id            | cases.diagnoses.treatments.treatment\_id              |                |
| treatment\_type                     | cases.diagnoses.treatments.treatment\_type          | cases.diagnoses.treatments.treatment\_type            |                |
| treatment\_outcome                  | cases.diagnoses.treatments.treatment\_outcome       | cases.diagnoses.treatments. treatment\_outcome        |                |
| days\_to\_treatment\_start          | cases.diagnoses.treatments.days\_to\_treatment      | cases.diagnoses.treatments.days\_to\_treatment\_start |                |
| days\_to\_treatment\_end            | cases.diagnoses.treatments.days\_to\_treatment_end  | cases.diagnoses.treatments.days\_to\_treatment\_end   |                |
| therapeutic\_agent	                 | cases.diagnoses.treatments.therapeutic\_agents	     | cases.diagnoses.treatments.therapeutic\_agents        |                |
| treatment\_anatomic\_site	          | cases.diagnoses.treatments.treatment\_anatomic\_site|	cases.diagnoses.treatments.treatment\_anatomic\_site  |                |
| treatment\_effect	                  | cases.diagnoses.treatments.treatment\_effect	       | cases.diagnoses.treatments.treatment\_effect          |                |
| treatment\_end\_reason	             | cases.diagnoses.treatments.reason\_treatment\_ended	| cases.diagnoses.treatments.reason\_treatment\_ended   |                | 
| number\_of\_cycles	                 | cases.diagnoses.treatments.number\_of\_cycles	      | cases.diagnoses.treatments.number\_of\_cycles         |                |

#### <a name="specimen_F"></a>Specimen

