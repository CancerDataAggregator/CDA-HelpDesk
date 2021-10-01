=====
Usage
=====

.. _usage:

We will now show you the basic structure of `CDA python` through the use of the most commands:

- ``columns()``: show all available columns in the table,
- ``unique_terms()``: for a given column show all unique terms,
- ``Q``: Executes this query on the public CDA server,
- ``query`` : allows you to write long form Q statments with out chaining, and
- ``Q.sql``: allows you to enter SQL style queries.


columns
-----

``columns()`` displays all of the fields that can be queried using the ``Q`` or ``single_operator_parser`` (e.g. ethnicity, tumor stage, disease type, etc.)

>>> from cdapython import Q, columns, unique_terms
>>> columns() # List column names eg:
['days_to_birth',
 'race',
 'sex',
 'ethnicity',
 'id',
 'ResearchSubject',
 'ResearchSubject.Diagnosis',
 'ResearchSubject.Diagnosis.morphology',
 'ResearchSubject.Diagnosis.tumor_stage',
 'ResearchSubject.Diagnosis.tumor_grade',
 'ResearchSubject.Diagnosis.Treatment',
 'ResearchSubject.Diagnosis.Treatment.type',
 'ResearchSubject.Diagnosis.Treatment.outcome',
 'ResearchSubject.Diagnosis.id',
 'ResearchSubject.Diagnosis.primary_diagnosis',
 'ResearchSubject.Diagnosis.age_at_diagnosis',
 'ResearchSubject.Specimen',
 'ResearchSubject.Specimen.File',
 'ResearchSubject.Specimen.File.label',
 'ResearchSubject.Specimen.File.associated_project',
 'ResearchSubject.Specimen.File.drs_uri',
 'ResearchSubject.Specimen.File.identifier',
 'ResearchSubject.Specimen.File.identifier.system',
 'ResearchSubject.Specimen.File.identifier.value',
 'ResearchSubject.Specimen.File.data_category',
 'ResearchSubject.Specimen.File.byte_size',
 'ResearchSubject.Specimen.File.type',
 'ResearchSubject.Specimen.File.file_format',
 'ResearchSubject.Specimen.File.checksum',
 'ResearchSubject.Specimen.File.id',
 'ResearchSubject.Specimen.File.data_type',
 'ResearchSubject.Specimen.derived_from_specimen',
 'ResearchSubject.Specimen.associated_project',
 'ResearchSubject.Specimen.age_at_collection',
 'ResearchSubject.Specimen.anatomical_site',
 'ResearchSubject.Specimen.source_material_type',
 'ResearchSubject.Specimen.derived_from_subject',
 'ResearchSubject.Specimen.specimen_type',
 'ResearchSubject.Specimen.id',
 'ResearchSubject.Specimen.primary_disease_type',
 'ResearchSubject.Specimen.identifier',
 'ResearchSubject.Specimen.identifier.system',
 'ResearchSubject.Specimen.identifier.value',
 'ResearchSubject.associated_project',
 'ResearchSubject.id',
 'ResearchSubject.primary_disease_type',
 'ResearchSubject.identifier',
 'ResearchSubject.identifier.system',
 'ResearchSubject.identifier.value',
 'ResearchSubject.primary_disease_site']
 

All of the above fields are what describes the highest entity in the data structure hierarchy – ``Patient`` entity. The first five fields represent ``Patient`` demographic information, while the ``ResearchSubject`` entity contains details that we are used to seeing within the nodes' ``Case`` record.

One of the contributions of the CDA is aggregated ``ResearchSubject`` information. This means that all ``ResearchSubject`` records coming from the same subject are now gathered under the Patient entity. As we know, certain specimens are studied in multiple projects (being part of a single data node or multiple nodes) as different ``ResearchSubject`` entries. Those ``ResearchSubject`` entries are collected as a list under the ``ResearchSubject`` entity. One example of this is the patient record with ``id = TCGA-E2-A10A`` which contains two ``ResearchSubject`` entries, one from GDC and the other from PDC.

Note that the ``ResearchSubject`` entity is a list of records, as many other entities above are. **There are certain considerations that should be made when creating the queries by using the fields that come from lists, but more about that will follow in examples below**.

The names in the list may look familiar to you, but they may have been renamed or restructured in the CDA. The field name mappings are described in the _CDA Schema Field Mapping_ document that is linked in the _Testing Guide_. A more direct way to explore and understand the fields is to use the ``unique_terms()`` function:
 
 
unique_terms
-------

For each searchable field there are set values that can be searched (excluding numberic), to determine these vaues the ``unique_terms()`` command is used. For example if we were interested in searchable disease types were would type the following:

>>> unique_terms("ResearchSubject.primary_disease_type")
[None,
 'Acinar Cell Neoplasms',
 'Adenomas and Adenocarcinomas',
 'Adnexal and Skin Appendage Neoplasms',
 'Basal Cell Neoplasms',
 'Blood Vessel Tumors',
 'Breast Invasive Carcinoma',
 'Chromophobe Renal Cell Carcinoma',
 'Chronic Myeloproliferative Disorders',
 'Clear Cell Renal Cell Carcinoma',
 'Colon Adenocarcinoma',
...

Additionally, you can specify a particular data node by using the ``system`` argument:

>>> unique_terms("ResearchSubject.Specimen.source_material_type", system="PDC")
['Solid Tissue Normal',
 'Primary Tumor',
 'Tumor',
 'Normal',
 'Not Reported',
 'Xenograft Tissue',
 'Cell Lines',
 'Normal Adjacent Tissue',
 'Xenograft']
 

Q
----

Now, let's dive into the querying!

We can start by getting the record for ``id = TCGA-E2-A10A`` that we mentioned earlier:

>>> q = query('id = "TCGA-E2-A10A"') # note the double quotes for the string value
>>> r = q.run()
>>> print(r)
Getting results from database
Total execution time: 1304 ms
QueryID: 243b307b-776b-4427-a8b3-eacb9a87b8d6
Query: SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3 WHERE (v3.id = 'TCGA-E2-A10A')
Offset: 0
Count: 1
Total Row Count: 1
More pages: False

We see that we've got a single patient record as a result, which is what we expect.

Let's see how the result looks like:


>>> r[0]
{'days_to_birth': '-15085',
 'race': 'white',
 'sex': 'female',
 'ethnicity': 'not hispanic or latino',
 'id': 'TCGA-E2-A10A',
 'ResearchSubject': [{'Diagnosis': [{'morphology': '8500/3',
     'tumor_stage': 'stage iib',
     'tumor_grade': 'not reported',
     'Treatment': [{'type': 'Pharmaceutical Therapy, NOS', 'outcome': None},
      {'type': 'Radiation Therapy, NOS', 'outcome': None}],
     'id': 'a84accf0-2294-550d-9825-22625f09f989',
     'primary_diagnosis': 'Infiltrating duct carcinoma, NOS',
     'age_at_diagnosis': '15085'}],
   'Specimen': [{'File': [{'label': 'TCGA-E2-A10A-01Z-00-DX1.98B19EF1-0DAE-4DC6-8B0E-963CFABC6724.svs',
       'associated_project': ['TCGA-BRCA'],
       'drs_uri': 'drs://dg.4DFC:99a00a9f-c4bf-49ca-9c3d-435f0a207644',
       'identifier': [{'system': 'GDC',
         'value': '99a00a9f-c4bf-49ca-9c3d-435f0a207644'}],
       'data_category': 'Biospecimen',
       'byte_size': '1341476123',
       'type': None,
       'file_format': None,
       'checksum': 'ca82c81a4e33e89ee50f69855053b001',
       'id': '99a00a9f-c4bf-49ca-9c3d-435f0a207644',
       'data_type': 'Slide Image'}],
     'derived_from_specimen': 'Initial sample',
     'associated_project': 'TCGA-BRCA',
     'age_at_collection': None,
     'anatomical_site': None,
     'source_material_type': 'Primary Tumor',
     'derived_from_subject': 'TCGA-E2-A10A',
     'specimen_type': 'sample',
     'id': 'd2900212-b6bd-423a-9968-6b35df0e98aa',
     'primary_disease_type': 'Ductal and Lobular Neoplasms',
     'identifier': [{'system': 'GDC',
       'value': 'd2900212-b6bd-423a-9968-6b35df0e98aa'}]},
    {'File': [{'label': '0012f466-075a-4d47-b1d7-e8e63e8b9c99.vep.vcf.gz',
       'associated_project': ['TCGA-BRCA'],
       'drs_uri': 'drs://dg.4DFC:0012f466-075a-4d47-b1d7-e8e63e8b9c99',
       'identifier': [{'system': 'GDC',
         'value': '0012f466-075a-4d47-b1d7-e8e63e8b9c99'}],
       'data_category': 'Simple Nucleotide Variation',
       'byte_size': '927367',
       'type': None,
       'file_format': None,
       'checksum': '82fa7202b77fd1f95c8cea7dd7e12ab2',
       'id': '0012f466-075a-4d47-b1d7-e8e63e8b9c99',
       'data_type': 'Annotated Somatic Mutation'},
      {'label': 'TCGA.BRCA.mutect.053f01ed-3154-4aea-9e7f-932c435034b3.DR-10.0.protected.maf.gz',
       'associated_project': ['TCGA-BRCA'],
       'drs_uri': 'drs://dg.4DFC:053f01ed-3154-4aea-9e7f-932c435034b3',
       'identifier': [{'system': 'GDC',
         'value': '053f01ed-3154-4aea-9e7f-932c435034b3'}],
       'data_category': 'Simple Nucleotide Variation',
       'byte_size': '1882061658',
       'type': None,
       'file_format': None,
       'checksum': 'ae12bbce7abcc03eff228935fa8d3d22',
       'id': '053f01ed-3154-4aea-9e7f-932c435034b3',
       'data_type': 'Aggregated Somatic Mutation'},
      ...
  {'Diagnosis': [{'morphology': '8500/3',
     'tumor_stage': 'Stage IIB',
     'tumor_grade': 'Not Reported',
     'Treatment': [],
     'id': 'ff312994-70ca-11e8-bcf1-0a2705229b82',
     'primary_diagnosis': 'Infiltrating duct carcinoma, NOS',
     'age_at_diagnosis': '15085'}],
   'Specimen': [{'File': [{'label': 'TCGA_E2-A10A_BH-A18Q_C8-A130_117C_W_BI_20130222_H-PM_f02.mzML.gz',
       'associated_project': ['CPTAC-TCGA'],
       'drs_uri': 'drs://dg.4DFC:00974c40-6abd-11e9-884a-005056921935',
       'identifier': [{'system': 'PDC',
         'value': '00974c40-6abd-11e9-884a-005056921935'}],
       'data_category': 'Processed Mass Spectra',
       'byte_size': '162469862',
       'type': None,
       'file_format': 'mzML',
       'checksum': '3016d34ed65209ddd36a2ac1216dbd9e',
       'id': '00974c40-6abd-11e9-884a-005056921935',
       'data_type': 'Open Standard'},
      {'label': 'TCGA_E2-A10A_BH-A18Q_C8-A130_117C_W_BI_20130222_H-PM_f03.mzML.gz',
       'associated_project': ['CPTAC-TCGA'],
       'drs_uri': 'drs://dg.4DFC:01fc9b08-6abd-11e9-884a-005056921935',
       'identifier': [{'system': 'PDC',
         'value': '01fc9b08-6abd-11e9-884a-005056921935'}],
       'data_category': 'Processed Mass Spectra',
       'byte_size': '166687764',
       'type': None,
       'file_format': 'mzML',
       'checksum': '76f5e76138aacb2997f54c6b25fd4d87',
       'id': '01fc9b08-6abd-11e9-884a-005056921935',
       'data_type': 'Open Standard'},
      ...
   'associated_project': 'CPTAC-TCGA',
   'id': '010df72d-63d9-11e8-bcf1-0a2705229b82',
   'primary_disease_type': 'Breast Invasive Carcinoma',
   'identifier': [{'system': 'PDC',
     'value': '010df72d-63d9-11e8-bcf1-0a2705229b82'}],
   'primary_disease_site': 'Breast'}]}
   
The record is pretty large, so we'll print out identifier values for each ResearchSubject to confirm that we have one ResearchSubject that comes from GDC, and one that comes from PDC:

>>> for research_subject in r[0]['ResearchSubject']:
>>>     print(research_subject['identifier'])
[{'system': 'GDC', 'value': '4da7abaf-ac7a-41c0-8033-5780a398545c'}]
[{'system': 'PDC', 'value': '010df72d-63d9-11e8-bcf1-0a2705229b82'}]

The values represent ResearchSubject IDs and are equivalent to case_id values in data nodes.

Now that we can create a query with ``Q()`` function, let's see how we can combine multiple conditions.

There are three operators available:
 * ``And()``
 * ``Or()``
 * ``From()``

The following examples show how those operators work in practice.


Query 1
+++++++
**Find data for subjects who were diagnosed after the age of 50 and who were investigated as part of the TCGA-OV project.**

.. code-block:: python

 
 >>> q1 = Q('ResearchSubject.Diagnosis.age_at_diagnosis > 50*365')
 >>> q2 = Q('ResearchSubject.associated_project = "TCGA-OV"')
 
 >>> q = q1.And(q2)
 >>> r = q.run()
 
 >>> print(r)
 
 Getting results from database
 
 Total execution time: 10550 ms
 
 QueryID: d43dd6bc-cab5-43c0-a683-ff32c5a6f621
 Query: SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Diagnosis) AS _Diagnosis WHERE ((_Diagnosis.age_at_diagnosis > 50*365) AND (_ResearchSubject.associated_project = 'TCGA-OV'))
 Offset: 0
 Count: 461
 Total Row Count: 461
 More pages: False


Query 2
+++++++
**Find data for donors with melanoma (Nevi and Melanomas) diagnosis and who were diagnosed before the age of 30.**

.. code-block:: python

 >>> q1 = Q('ResearchSubject.Specimen.primary_disease_type = "Nevi and Melanomas"')
 >>> q2 = Q('ResearchSubject.Diagnosis.age_at_diagnosis < 30*365')
 
 >>> q = q1.And(q2)
 >>> r = q.run()
 
 >>> print(r)
 
 Getting results from database
 
 Total execution time: 11287 ms
 
 QueryID: 02c118d4-08ac-442f-bc79-71b794bab6bc
 Query: SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Specimen) AS _Specimen, UNNEST(_ResearchSubject.Diagnosis) AS _Diagnosis WHERE ((_Specimen.primary_disease_type = 'Nevi and Melanomas') AND (_Diagnosis.age_at_diagnosis < 30*365))
 Offset: 0
 Count: 647
 Total Row Count: 647
 More pages: False


In addition, we can check how many records come from particular systems by adding one more condition to the query:

.. code-block:: python

 >>> q1 = Q('ResearchSubject.Specimen.primary_disease_type = "Nevi and Melanomas"')
 >>> q2 = Q('ResearchSubject.Diagnosis.age_at_diagnosis < 30*365')
 >>> q3 = Q('ResearchSubject.Specimen.identifier.system = "GDC"')
 
 >>> q = q1.And(q2.And(q3))
 >>> r = q.run()
 
 >>> print(r)
 
 >>> q1 = Q('ResearchSubject.primary_disease_type = "Adenomas and Adenocarcinomas"')
 >>> r = q1.run()                                 # Executes this query on the public CDA server
 
 Getting results from database
 
 Total execution time: 9604 ms
 
 QueryID: 2cd1f165-f6f5-49e4-b699-b4df191a540f
 Query: SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Specimen) AS _Specimen, UNNEST(_ResearchSubject.Diagnosis) AS _Diagnosis, UNNEST(_Specimen.identifier) AS _identifier WHERE ((_Specimen.primary_disease_type = 'Nevi and Melanomas') AND ((_Diagnosis.age_at_diagnosis < 30*365) AND (_identifier.system = 'GDC')))
 Offset: 0
 Count: 647
 Total Row Count: 647
 More pages: False


By comparing the ``Count`` value of the two results we can see that all the patients returned in the initial query are coming from the GDC.

To explore the results further, we can fetch the patient JSON objects by iterating through the results:

.. code-block:: python

 >>> projects = set()
 
 >>> for patient in r:
 >>>     research_subjects = patient['ResearchSubject']
 >>>     for rs in research_subjects:
 >>>         projects.add(rs['associated_project'])
 
 >>> print(projects)
 {'FM-AD', 'TCGA-UVM', 'TCGA-SKCM'}


The output shows the projects where Nevi and Melanomas cases appear.

Query 3
+++++++

**Identify all samples that meet the following conditions:**

* **Sample is from primary tumor**
* **Disease is ovarian or breast cancer**
* **Subjects are females under the age of 60 years**

.. code-block:: python

 >>> tumor_type = Q('ResearchSubject.Specimen.source_material_type = "Primary Tumor"')
 >>> disease1 = Q('ResearchSubject.primary_disease_site = "Ovary"')
 >>> disease2 = Q('ResearchSubject.primary_disease_site = "Breast"')
 >>> demographics1 = Q('sex = "female"')
 >>> demographics2 = Q('days_to_birth > -60*365') # note that days_to_birth is a negative value
 
 >>> q1 = tumor_type.And(demographics1.And(demographics2))
 >>> q2 = disease1.Or(disease2)
 >>> q = q1.And(q2)
 
 >>> r = q.run()
 >>> print(r)
 
 Getting results from database
 
 Total execution time: 20529 ms
 
 QueryID: 2b325482-f764-4675-aebe-43f7e8d4004a
 Query: SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Specimen) AS _Specimen WHERE (((_Specimen.source_material_type = 'Primary Tumor') AND ((v3.sex = 'female') AND (v3.days_to_birth > -60*365))) AND ((_ResearchSubject.primary_disease_site = 'Ovary') OR (_ResearchSubject.primary_disease_site = 'Breast')))
 Offset: 0
 Count: 1000
 Total Row Count: 27284
 More pages: True


In this case, we have a result that contains more than 1000 records which is the default page size. To load the next 1000 records, we can use the ``next_page()`` method:

.. code-block:: python

 >>> r2 = r.next_page()
 
 >>> print(r2)


Alternatively, we can use the ``offset`` argument to specify the record to start from:

.. code-block:: python
 ...
 >>> r = q.run(offset=1000)
 >>> print(r)


Query 4
+++++

**Find data for donors with "Ovarian Serous Cystadenocarcinoma" with proteomic and genomic data.**

**Note that disease type value denoting the same disease groups can be completely different within different systems. This is where CDA features come into play.** We first start by exploring the values available for this particular field in both systems.

>>> unique_terms('ResearchSubject.primary_disease_type', system="GDC",limit=10)
['Osseous and Chondromatous Neoplasms',
 'Not Applicable',
 'Lymphoid Leukemias',
 'Myeloid Leukemias',
 'Not Reported',
 'Cystic, Mucinous and Serous Neoplasms',
 'Adenomas and Adenocarcinomas',
 'Gliomas',
 'Ductal and Lobular Neoplasms',
 'Germ Cell Neoplasms']
 
 
Since “Ovarian Serous Cystadenocarcinoma” doesn’t appear in GDC values we decide to look into the PDC:

>>> unique_terms('ResearchSubject.primary_disease_type', system="PDC")
['Other',
 'Lung Squamous Cell Carcinoma',
 'Head and Neck Squamous Cell Carcinoma',
 'Lung Adenocarcinoma',
 'Colon Adenocarcinoma',
 'Rectum Adenocarcinoma',
 'Clear Cell Renal Cell Carcinoma',
 'Uterine Corpus Endometrial Carcinoma',
 'Ovarian Serous Cystadenocarcinoma',
 'Breast Invasive Carcinoma',
 'Pancreatic Ductal Adenocarcinoma',
 'Pediatric/AYA Brain Tumors',
 'Glioblastoma',
 'Hepatocellular Carcinoma ',
 'Early Onset Gastric Cancer',
 'Chromophobe Renal Cell Carcinoma',
 'Papillary Renal Cell Carcinoma',
 'Oral Squamous Cell Carcinoma']
 
After examining the output, we see that it does come from the PDC. Hence, if we could first identify the data that has research subjects found within the PDC that have this particular disease type, and then further narrow down the results to include only the portion of the data that is present in GDC, we could get the records that we are looking for.

.. code-block:: python

 >>> q1 = Q('ResearchSubject.primary_disease_type = "Ovarian Serous Cystadenocarcinoma"')
 >>> q2 = Q('ResearchSubject.identifier.system = "PDC"')
 >>> q3 = Q('ResearchSubject.identifier.system = "GDC"')
 
 >>> q = q3.From(q1.And(q2))
 >>> r = q.run()
 
 >>> print(r)
 Getting results from database
 
 Total execution time: 11682 ms
 
 QueryID: 9755ed03-e8de-4e26-9ea8-de8a9b3a0c94
 Query: SELECT v3.* FROM (SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE ((_ResearchSubject.primary_disease_type = 'Ovarian Serous Cystadenocarcinoma') AND (_identifier.system = 'PDC'))) AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE (_identifier.system = 'GDC')
 Offset: 0
 Count: 275
 Total Row Count: 275
 More pages: False

As you can see, this is achieved by utilizing ``From`` operator. The ``From`` operator allows us to create queries from results of other queries. This is particularly useful when working with conditions that involve a single field which can take multiple different values for different items in a list that is being part of, e.g. we need ``ResearchSubject.identifier.system`` to be both “PDC” and “GDC” for a single patient. In such cases, ``And`` operator can’t help because it will return those entries where the field takes both values, which is zero entries.


.. code-block:: python

 >>> r = q1.run(host="http://localhost:8080")   # Executes on local instance of CDA server
 >>> r = q1.run(limit=2)                        # Limit to two results per page
 
 >>> r.sql   # Return SQL string used to generate the query e.g.
 "SELECT * FROM gdc-bq-sample.cda_mvp.v1, UNNEST(ResearchSubject) AS _ResearchSubject WHERE (_ResearchSubject.primary_disease_type = 'Adenomas and Adenocarcinomas')"
 
 >>> print(r) # Prints some brief information about the result page eg:
 Query: SELECT * FROM gdc-bq-sample.cda_mvp.v1, UNNEST(ResearchSubject) AS _ResearchSubject WHERE (_ResearchSubject.# primary_disease_type = 'Adenomas and Adenocarcinomas')
 Offset: 0
 Limit: 2
 Count: 2
 More pages: Yes
 
 >>> r[0] # Returns nth result of this page as a Python dict e.g.
 {'days_to_birth': None,
  'race': None,
  'sex': None,
  'ethnicity': None,
  'id': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3',
  'ResearchSubject': [{'Diagnosis': [],
    'Specimen': [],
    'associated_project': 'CGCI-HTMCP-CC',
    'id': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3',
    'primary_disease_type': 'Adenomas and Adenocarcinomas',
    'identifier': [{'system': 'GDC',
      'value': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3'}],
    'primary_disease_site': 'Cervix uteri'}],
  'Diagnosis': [],
  'Specimen': [],
  'associated_project': 'CGCI-HTMCP-CC',
  'primary_disease_type': 'Adenomas and Adenocarcinomas',
  'identifier': [{'system': 'GDC',
    'value': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3'}],
  'primary_disease_site': 'Cervix uteri'}
  
 >>> r.pretty_print(0) # Prints the nth result nicely
 { 'Diagnosis': [],
   'ResearchSubject': [ { 'Diagnosis': [],
                          'Specimen': [],
                          'associated_project': 'CGCI-HTMCP-CC',
                          'id': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3',
                          'identifier': [ { 'system': 'GDC',
                                            'value': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3'}],
                          'primary_disease_site': 'Cervix uteri',
                          'primary_disease_type': 'Adenomas and '
                                                  'Adenocarcinomas'}],
   'Specimen': [],
   'associated_project': 'CGCI-HTMCP-CC',
   'days_to_birth': None,
   'ethnicity': None,
   'id': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3',
   'identifier': [ { 'system': 'GDC',
                     'value': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3'}],
   'primary_disease_site': 'Cervix uteri',
   'primary_disease_type': 'Adenomas and Adenocarcinomas',
   'race': None,
   'sex': None}
   
 >>> r2 = r.next_page()  # Fetches the next page of results
 >>> print(r2)
 Query: SELECT * FROM gdc-bq-sample.cda_mvp.v1, UNNEST(ResearchSubject) AS _ResearchSubject WHERE (_ResearchSubject.# primary_disease_type = 'Adenomas and Adenocarcinomas')
 Offset: 2
 Limit: 2
 Count: 2
 More pages: Yes


query
-----

To ease the query writing process, we have also implimented ``query`` which allows ``AND``, ``OR`` and ``FROM`` to be included in the query string without the need of an additional step to use operators. The following `Q` query:

.. code-block:: python
 
 >>> q1 = Q('ResearchSubject.Specimen.primary_disease_type = "Nevi and Melanomas"')
 >>> q2 = Q('ResearchSubject.Diagnosis.age_at_diagnosis < 30*365')
 >>> q3 = Q('ResearchSubject.Specimen.identifier.system = "GDC"')
 
 >>> q = q1.And(q2.And(q3))
 
can be rewritten using the `query` function:

>>> query('ResearchSubject.Specimen.primary_disease_type = "Nevi and Melanomas" AND ResearchSubject.Diagnosis.age_at_diagnosis < 30*365 AND ResearchSubject.identifier.system = "GDC"')
>>> result = q1.run()

Q.sql
-----

In some cases

.. code-block:: python

 r1 = Q.sql("""
 SELECT
 *
 FROM gdc-bq-sample.cda_mvp.v1, UNNEST(ResearchSubject) AS _ResearchSubject
 WHERE (_ResearchSubject.primary_disease_type = 'Adenomas and Adenocarcinomas')
 """)
 
 >>> r1.pretty_print(0)
 { 'Diagnosis': [],
  'ResearchSubject': [ { 'Diagnosis': [],
                         'Specimen': [],
                         'associated_project': 'CGCI-HTMCP-CC',
                         'id': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3',
                         'identifier': [ { 'system': 'GDC',
                                           'value': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3'}],
                         'primary_disease_site': 'Cervix uteri',
                         'primary_disease_type': 'Adenomas and '
                                                 'Adenocarcinomas'}],
  'Specimen': [],
  'associated_project': 'CGCI-HTMCP-CC',
  'days_to_birth': None,
  'ethnicity': None,
  'id': 'HTMCP-03-06-02177',
  'id_1': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3',
  'identifier': [ { 'system': 'GDC',
                    'value': '4d54f72c-e8ac-44a7-8ab9-9f20001750b3'}],
  'primary_disease_site': 'Cervix uteri',
  'primary_disease_type': 'Adenomas and Adenocarcinomas',
  'race': None,
  'sex': None}
