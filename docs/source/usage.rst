=====
Usage
=====


We will now show you the basic structure of `CDA python` through the use of the most commands:

- ``columns()``: show all available columns in the table,
- ``unique_terms()``: for a given column show all unique terms,
- ``Q()``: Executes this query on the public CDA server,
- ``query()`` : allows you to write long form Q statments with out chaining, and
- ``Q.sql()``: allows you to enter SQL style queries.

**To begin we will first load all of the library and it's methods:**

>>> from cdapython import Q, columns, unique_terms, query

  
columns()
-----
``columns(version = 'all_v1', host = None, limit = 100, table = 'integration')``

displays all of the fields that can be queried using the ``Q`` or ``query`` (e.g. ethnicity, tumor stage, disease type, etc.)

**Parameters:**
   - version : str [Optional]
       - version allows you to select different version of SQL (BigQuery) tables to runs querys on; default = 'all_v1'
   - host : str [Optional]
       - host allows you to change the server in which you queries run; default = None (Board Institute)
   - limit : int [Optional]
       - limit allows you to set the number of values that ``columns`` returns; default = 100
   - table : str [Optional]
        table allows you to select with BigQuery table is being searched; default = 'integration'
**Returns:**
    list
**Example:**

>>> columns() # List column names eg:
['id',
 'identifier',
 'identifier.system',
 'identifier.value',
 'sex',
 'race',
 'ethnicity',
 'days_to_birth',
 'subject_associated_project',
 'File',
 'File.id',
 'File.identifier',
 'File.identifier.system',
 'File.identifier.value',
 'File.label',
 'File.data_category',
 'File.data_type',
 'File.file_format',
 'File.associated_project',
 'File.drs_uri',
 'File.byte_size',
 'File.checksum',
 'ResearchSubject',
 'ResearchSubject.id',
 'ResearchSubject.identifier',
 'ResearchSubject.identifier.system',
 'ResearchSubject.identifier.value',
 'ResearchSubject.associated_project',
 'ResearchSubject.primary_disease_type',
 'ResearchSubject.primary_disease_site',
 'ResearchSubject.Diagnosis',
 'ResearchSubject.Diagnosis.id',
 'ResearchSubject.Diagnosis.identifier',
 'ResearchSubject.Diagnosis.identifier.system',
 'ResearchSubject.Diagnosis.identifier.value',
 'ResearchSubject.Diagnosis.primary_diagnosis',
 'ResearchSubject.Diagnosis.age_at_diagnosis',
 'ResearchSubject.Diagnosis.morphology',
 'ResearchSubject.Diagnosis.stage',
 'ResearchSubject.Diagnosis.grade',
 'ResearchSubject.Diagnosis.Treatment',
 'ResearchSubject.Diagnosis.Treatment.id',
 'ResearchSubject.Diagnosis.Treatment.identifier',
 'ResearchSubject.Diagnosis.Treatment.identifier.system',
 'ResearchSubject.Diagnosis.Treatment.identifier.value',
 'ResearchSubject.Diagnosis.Treatment.treatment_type',
 'ResearchSubject.Diagnosis.Treatment.treatment_outcome',
 'ResearchSubject.Diagnosis.Treatment.days_to_treatment_start',
 'ResearchSubject.Diagnosis.Treatment.days_treatment_end',
 'ResearchSubject.File',
 'ResearchSubject.File.id',
 'ResearchSubject.File.identifier',
 'ResearchSubject.File.identifier.system',
 'ResearchSubject.File.identifier.value',
 'ResearchSubject.File.label',
 'ResearchSubject.File.data_category',
 'ResearchSubject.File.data_type',
 'ResearchSubject.File.file_format',
 'ResearchSubject.File.associated_project',
 'ResearchSubject.File.drs_uri',
 'ResearchSubject.File.byte_size',
 'ResearchSubject.File.checksum',
 'ResearchSubject.Specimen',
 'ResearchSubject.Specimen.id',
 'ResearchSubject.Specimen.identifier',
 'ResearchSubject.Specimen.identifier.system',
 'ResearchSubject.Specimen.identifier.value',
 'ResearchSubject.Specimen.associated_project',
 'ResearchSubject.Specimen.age_at_collection',
 'ResearchSubject.Specimen.primary_disease_type',
 'ResearchSubject.Specimen.anatomical_site',
 'ResearchSubject.Specimen.source_material_type',
 'ResearchSubject.Specimen.specimen_type',
 'ResearchSubject.Specimen.derived_from_specimen',
 'ResearchSubject.Specimen.derived_from_subject',
 'ResearchSubject.Specimen.File',
 'ResearchSubject.Specimen.File.id',
 'ResearchSubject.Specimen.File.identifier',
 'ResearchSubject.Specimen.File.identifier.system',
 'ResearchSubject.Specimen.File.identifier.value',
 'ResearchSubject.Specimen.File.label',
 'ResearchSubject.Specimen.File.data_category',
 'ResearchSubject.Specimen.File.data_type',
 'ResearchSubject.Specimen.File.file_format',
 'ResearchSubject.Specimen.File.associated_project',
 'ResearchSubject.Specimen.File.drs_uri',
 'ResearchSubject.Specimen.File.byte_size',
 'ResearchSubject.Specimen.File.checksum']
 

All of the above fields are what describes the highest entity in the data structure hierarchy – ``Subject`` entity. The first five fields represent ``Subject`` demographic information, while the ``ResearchSubject`` entity contains details that we are used to seeing within the nodes' ``Case`` record.

One of the contributions of the CDA is aggregated ``ResearchSubject`` information. This means that all ``ResearchSubject`` records coming from the same subject are now gathered under the Subject entity. As we know, certain specimens are studied in multiple projects (being part of a single data node or multiple nodes) as different ``ResearchSubject`` entries. Those ``ResearchSubject`` entries are collected as a list under the ``ResearchSubject`` entity. One example of this is the subject record with ``id = TCGA-E2-A10A`` which contains two ``ResearchSubject`` entries, one from GDC and the other from PDC.

.. note::

  Note that the ``ResearchSubject`` entity is a list of records, as many other entities above are. **There are certain considerations that should be made when  creating the queries by using the fields that come from lists, but more about that will follow in examples below**.

The names in the list may look familiar to you, but they may have been renamed or restructured in the CDA. For more information about the field name mappings you can look into :doc:`ETL` . A more direct way to explore and understand the fields is to use the ``unique_terms()`` function:
 
 
unique_terms()
-------
``unique_terms(col_name: str, system: str = '', limit: int = 100, host: Optional[str] = None, table: Optional[str] = None)``

displays all non-numeric values that can be searched in a query for a given column.

**Parameters:**
    - col_name : str
        - col_name is the value from the ``columns()`` that you would like a list of searchable terms from (e.g. 'ResearchSubject.primary_disease_site')
    - system : str [Optional]
        - system allows you to determine which data common you would like to search (GDC, PDC, or IDC; see :ref:`limit`)
    - limit : int [Optional]
        - limit allows you to set the number of values that ``columns`` returns; default = 100   
    - host : str [Optional]
        - host allows you to change the server in which you queries run; default = None (Board Institute)
    - table : str [Optional] 
        - table allows you to select with Big Query table is being searched; default = 'integration'
**Returns:**
    list
**Example:**



For each searchable field there are set values that can be searched (excluding numeric), to determine these values the ``unique_terms()`` command is used. For example if we were interested in searchable disease types at the ResearchSubject level were would type the following:

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

.. note::
  The results of ``unique_terms()`` may not be the same a different level (Subject vs ResearchSubject vs Specimen), so ``unique_terms()`` most be searched at the same level you plan to run your query.

Additionally, you can specify a particular data node by using the ``system`` argument. For more information on data nodes/data commons see :ref:`ETL`.

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

.. warning::
  Some columns are nested array datatypes consisting of sub-columns/arrays and do not have ``unique_terms``. Arrays columns contain multiple values; an example of this would be ``File.identifier`` which as  comprised of ``system`` (which data common the information is from) and ``value`` (the id for a given file). 
  
  .. code-block:: json
  
   {'File': [{'label': '0012f466-075a-4d47-b1d7-e8e63e8b9c99.vep.vcf.gz',
     'associated_project': ['TCGA-BRCA'],
     'drs_uri': 'drs://dg.4DFC:0012f466-075a-4d47-b1d7-e8e63e8b9c99',
     **'identifier': [{'system': 'GDC', 'value': '0012f466-075a-4d47-b1d7-e8e63e8b9c99'}]**
     ...

  Below is the list of column values that do not have ``unique_terms``. Additionally, these columns should not be used in a query.
  
 - 'File',
 - 'File.identifier',
 - 'identifier',
 - 'ResearchSubject',
 - 'ResearchSubject.Diagnosis',
 - 'ResearchSubject.Diagnosis.Treatment',
 - 'ResearchSubject.Specimen',
 - 'ResearchSubject.Specimen.File',
 - 'ResearchSubject.Specimen.File.identifier',
 - 'ResearchSubject.Specimen.identifier',
 - 'ResearchSubject.identifier',
 - 'subject_associated_project',
 - 'ResearchSubject.Diagnosis.identifier',
 - 'ResearchSubject.Diagnosis.Treatment.identifier',
 - 'ResearchSubject.File',
 - 'ResearchSubject.File.identifier'

Q()
----
``Q(query)``

Q lang is Language used to send query to the cda service

**Parameters:**
    - query : str
        - a query string containing a value from ``columns()`` with an comparison operator (=, !=, <, >) and a numeric/boolean/unique value form ``unique_terms``. 
**Returns:**
    cda python Q data type
    
``Q().run``

run(offset = 0, limit = 100, version = 'all_v1', host = None, dry_run = False, table = 'gdc-bq-sample.integration', async_call = False)

**Parameters:**
    - async_call : bool
        - async_call allows for queries to run async
    - table : str
        - table allows you to select with BigQuery table is being searched; default = ‘integration’
    - offset : int [optional] 
        - [description]. Defaults to 0.
    - limit : int, optional):
        - limit allows you to set the number of values that returns per page; default = 100
    - host : URL, [optional]
        - host allows you to change the server in which you queries run; default = None (Board Institute)
    - dry_run : bool, [optional] 
        - [description]. Defaults to False.
**Returns:**
    cda python Q data type
    
Q Comparison operators
+++++++

The following comparsion operators can be used with the `Q` or `query` command: 

+----------+---------------------------------------------------+---------------+
| operator |Description                                        |Q.sql required?|
+==========+===================================================+===============+
| =        | condition equals                                  |     no        |
+----------+---------------------------------------------------+---------------+
| !=       | condition is not equal                            |     no        |
+----------+---------------------------------------------------+---------------+
| <        | condition is less than                            |     no        |
+----------+---------------------------------------------------+---------------+
| >        | condition is greater than                         |     no        |
+----------+---------------------------------------------------+---------------+
| <=       | condition is less than or equal to                |     no        |
+----------+---------------------------------------------------+---------------+
| >=       | condition is less than or equal to                |     no        |
+----------+---------------------------------------------------+---------------+
| like     | similar to = but always wildcards ('%', '_', etc) |    yes        |
+----------+---------------------------------------------------+---------------+
| in       | compares to a set                                 |    yes        |
+----------+---------------------------------------------------+---------------+

additionally, more complex SQL can be used with the `Q.sql()`_ command. 

**Example:**

.. note::

  Any given part of a query is expressed as a string of three parts separated by spaces. **Therefore, there must be a space on both sides of the comparsion operator**. The first part of the query is interpreted as a **column name**, the second as a **comparator operator** and the third part as a **value**. If the value is a string, it needs to be put in double quotes.

Now, let's dive into the querying!

We can start by getting the record for ``id = TCGA-E2-A10A`` that we mentioned earlier:

>>> q = Q('id = "TCGA-E2-A10A"') # note the double quotes for the string value
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

We've discussed ``Q`` but not the ``.run()`` method; ``.run()`` must be called to actually process your query. After calling ``print()`` on the query result variable we see that we've got a single Subject record as a result, which is what we expect.

Let's take a look at the results:


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

The values represent ResearchSubject IDs and are equivalent to case_id values in data commons.

.. warning::
  In some instances the results will return multiple pages, if this is the case you must include ``next_page()`` in you loop. An example of looping with ``next_page()`` can be found here.

Now that we can create a query with ``Q()`` function, let's see how we can combine multiple conditions.

And, Or and From operators
++++
There are three operators available:
 * ``And()``
 * ``Or()``
 * ``From()``

The following examples show how those operators work in practice.


Example Query 1: And
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


Example Query 2: And continued
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
 
 
 Getting results from database
 
 Total execution time: 9604 ms
 
 QueryID: 2cd1f165-f6f5-49e4-b699-b4df191a540f
 Query: SELECT v3.* FROM gdc-bq-sample.cda_mvp.v3 AS v3, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Specimen) AS _Specimen, UNNEST(_ResearchSubject.Diagnosis) AS _Diagnosis, UNNEST(_Specimen.identifier) AS _identifier WHERE ((_Specimen.primary_disease_type = 'Nevi and Melanomas') AND ((_Diagnosis.age_at_diagnosis < 30*365) AND (_identifier.system = 'GDC')))
 Offset: 0
 Count: 647
 Total Row Count: 647
 More pages: False


By comparing the ``Count`` value of the two results we can see that all the Subjects returned in the initial query are coming from the GDC.

To explore the results further, we can fetch the Subject JSON objects by iterating through the results:

.. code-block:: python

 >>> projects = set()
 
 >>> for subject in r:
 >>>     research_subjects = subject['ResearchSubject']
 >>>     for rs in research_subjects:
 >>>         projects.add(rs['associated_project'])
 
 >>> print(projects)
 {'FM-AD', 'TCGA-UVM', 'TCGA-SKCM'}


The output shows the projects where Nevi and Melanomas cases appear.

Example Query 3: Or
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

  >>> r = q.run(offset=1000)
  >>> print(r)


Example Query 4: From
+++++

**Find data for donors with "Ovarian Serous Cystadenocarcinoma" with proteomic and genomic data.**

.. note::
  **Disease type values denoting the same disease groups can be completely different within different systems. This is where CDA features come into play.** We first start by exploring the values available for this particular field in both systems.

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

As you can see, this is achieved by utilizing ``From`` operator. The ``From`` operator allows us to create queries from results of other queries. This is particularly useful when working with conditions that involve a single field which can take multiple different values for different items in a list that is being part of, e.g. we need ``ResearchSubject.identifier.system`` to be both “PDC” and “GDC” for a single Subject. In such cases, ``And`` operator can’t help because it will return those entries where the field takes both values, which is zero entries.


Example Query 5: From continued (IDC)
+++++

**Find data for donors with "Ovarian Serous Cystadenocarcinoma" with proteomic and imaging data.**

So now we would like to repeat the previouse query but this time identify cases that are also in IDC. As noted before disease type value denoting the same disease groups can be completely different within different systems. So let's explore the values available for this particular field in IDC.

>>> unique_terms('ResearchSubject.primary_disease_type', system="IDC",limit=10)
[]

Oh no! looks like we have an empty set. This is because IDC does not have `ResearchSubject` (or Specimen) intities, only Subject intities (see .. ref:: here `ETL` for more information). So, let try the same code as `Example Query 4: From`_ but change the ``ResearchSubject.identifier.system`` to **IDC** instead of **GDC**. 

.. code-block:: python

  q1 = Q('ResearchSubject.primary_disease_type = "Ovarian Serous Cystadenocarcinoma"')
  q2 = Q('ResearchSubject.identifier.system = "PDC"')
  q3 = Q('ResearchSubject.identifier.system = "IDC"')
  
  q = q3.From(q1.And(q2))
  r = q.run()
  
  print(r)
  
  Getting results from database
  
  Total execution time: 7810 ms
  
  QueryID: 664b226e-babc-462b-a826-448b8ab551a7
  Query: SELECT all_v1.* FROM (SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE ((_ResearchSubject.primary_disease_type = 'Ovarian Serous Cystadenocarcinoma') AND (_identifier.system = 'PDC'))) AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE (_identifier.system = 'IDC')
  Offset: 0
  Count: 0
  Total Row Count: 0
  More pages: False


Hmm, zero results. Looks like we made a similar mistake and once again included `ResearchSubject`. If we look at the available searchable fields again using ``columns()``, we will see that there is another field named ``identifier.system`` at the Subject level. So, let's try that:

.. code-block:: python

  q1 = Q('ResearchSubject.primary_disease_type = "Ovarian Serous Cystadenocarcinoma"')
  q2 = Q('ResearchSubject.identifier.system = "PDC"')
  q3 = Q('identifier.system = "IDC"')
  
  q = q3.From(q1.And(q2))
  r = q.run()
  
  print(r)
  
  Getting results from database
  
  Total execution time: 7281 ms
  
  QueryID: 2baf2b96-8424-440b-8765-6d44cf098feb
  Query: SELECT all_v1.* FROM (SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE ((_ResearchSubject.primary_disease_type = 'Ovarian Serous Cystadenocarcinoma') AND (_identifier.system = 'PDC'))) AS all_v1, UNNEST(identifier) AS _identifier WHERE (_identifier.system = 'IDC')
  Offset: 0
  Count: 37
  Total Row Count: 37
  More pages: False


After a quick fix we now have 37 cases.

Example query 6: Return all data
++++

In some instances you may want to return all of the data to build/process your own database. This can be done by queries for data in any of the Data Commons using the ``identifier.system`` columns and ``OR`` operator.

.. code-block:: python

  q = query('identifier.system = "GDC" OR identifier.system = "PDC" OR identifier.system = "IDC"')
  r = q.run()
  r
  
  Getting results from database
  
  Total execution time: 25049 ms
  
  QueryID: 211bf374-62bd-477e-8bc6-5c7954eb587f
  Query: SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(identifier) AS _identifier WHERE (((_identifier.system = 'GDC') OR (_identifier.system = 'PDC')) OR (_identifier.system = 'IDC'))
  Offset: 0
  Count: 100
  Total Row Count: 104731
  More pages: True

query()
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

Q.sql()
-----

In some cases more complex queries are required, and for that purpose we have implimented ``Q.sql()`` which takes in a SQL style query

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

Test queries
----

Test query 1
+++++

**Find data from all Subjects who have been treated with "Radiation Therapy, NOS" and have both genomic and proteomic data.**

.. toggle-header::

  :header: Example 1 **Show/Hide Code**
    
    .. code-block:: python
    
      q1 = Q('ResearchSubject.Diagnosis.Treatment.treatment_type = "Radiation Therapy, NOS"')
      q2 = Q('ResearchSubject.identifier.system = "PDC"')
      q3 = Q('ResearchSubject.identifier.system = "GDC"')
      
      q = q2.From(q1.And(q3))
      r = q.run()
      
      print(r)
      
      Getting results from database
      
      Total execution time: 27414 ms
      
      QueryID: a8eabfc7-7258-45cb-8570-763ec4d1926c
      Query: SELECT all_v1.* FROM (SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Diagnosis) AS _Diagnosis, UNNEST(_Diagnosis.Treatment) AS _Treatment, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE ((_Treatment.treatment_type = 'Radiation Therapy, NOS') AND (_identifier.system = 'GDC'))) AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE (_identifier.system = 'PDC')
      Offset: 0
      Count: 100
      Total Row Count: 369
      More pages: True


Test query 2
+++++

**Find data from TCGA-BRCA project, with donors over the age of 50 with imaging data**

.. code-block:: python
  q1 = Q('ResearchSubject.associated_project = "TCGA-BRCA"')
  q2 = Q('days_to_birth > -50*365')
  q3 = Q('identifier.system = "IDC"')
  
  q = q3.From(q1.And(q2))
  r = q.run()
  
  print(r)
  
  Getting results from database
  
  Total execution time: 24125 ms
  
  QueryID: a5de2545-2b5e-476c-9e92-b768d058f603
  Query: SELECT all_v1.* FROM (SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject WHERE ((_ResearchSubject.associated_project = 'TCGA-BRCA') AND (all_v1.days_to_birth < -50*365))) AS all_v1, UNNEST(identifier) AS _identifier WHERE (_identifier.system = 'IDC')
  Offset: 0
  Count: 88
  Total Row Count: 88
  More pages: False


Pointing to a custom CDA instance
----

``.run()`` will execute the query on the public `CDA API <https://cda.cda-dev.broadinstitute.org/api/cda/v1/>_.

``.run("http://localhost:8080")`` will execute the query on a CDA server running at
``http://localhost:8080``.

Quick Explanation on UNNEST usage in BigQuery
----

Using Q in the CDA client will echo the generated SQL statement that may contain multiple `UNNEST` inclusions
when including a dot(.) structure which may need a quick explanation.
UNNEST is similar to unwind in which embedded data structures must be flattend to appear in a table or Excel file.
Note; The following call using the SQL endpoint is not the preferred method to execute a nested attribute query in BigQuery.
The Q language DSL abstracts the required unnesting that exists in a Record. In BigQuery, structures must be represented in an UNNEST syntax such that:
``A.B.C.D`` must be unwound to ``SELECT (_C.D)`` in the following fashion: 

```
SELECT (_C.D) 
from TABLE, UNNEST(A) AS _A, UNNEST(_A.B) as _B, UNNEST(_B.C) as _C
```

``ResearchSubject.Specimen.source_material_type`` represents a complex record that needs to unwound in SQL syntax to be queried on properly when using SQL.

```
SELECT DISTINCT(_Specimen.source_material_type) 
FROM gdc-bq-sample.cda_mvp.v3, 
UNNEST(ResearchSubject) AS _ResearchSubject,
UNNEST(_ResearchSubject.Specimen) AS _Specimen
```

Test query answers
----

Test query 1
+++++
**Find data from all Subjects who have been treated with "Radiation Therapy, NOS" and have both genomic and proteomic data.**

.. code-block:: python

  q1 = Q('ResearchSubject.Diagnosis.Treatment.treatment_type = "Radiation Therapy, NOS"')
  q2 = Q('ResearchSubject.identifier.system = "PDC"')
  q3 = Q('ResearchSubject.identifier.system = "GDC"')
  
  q = q2.From(q1.And(q3))
  r = q.run()
  
  print(r)
  
  Getting results from database
  
  Total execution time: 27414 ms
  
  QueryID: a8eabfc7-7258-45cb-8570-763ec4d1926c
  Query: SELECT all_v1.* FROM (SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.Diagnosis) AS _Diagnosis, UNNEST(_Diagnosis.Treatment) AS _Treatment, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE ((_Treatment.treatment_type = 'Radiation Therapy, NOS') AND (_identifier.system = 'GDC'))) AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject, UNNEST(_ResearchSubject.identifier) AS _identifier WHERE (_identifier.system = 'PDC')
  Offset: 0
  Count: 100
  Total Row Count: 369
  More pages: True


Test query 2
+++++

**Find data from TCGA-BRCA project, with donors over the age of 50 with imaging data**

.. code-block:: python

  q1 = Q('ResearchSubject.associated_project = "TCGA-BRCA"')
  q2 = Q('days_to_birth > -50*365')
  q3 = Q('identifier.system = "IDC"')
  
  q = q3.From(q1.And(q2))
  r = q.run()
  
  print(r)
  
  Getting results from database
  
  Total execution time: 24125 ms
  
  QueryID: a5de2545-2b5e-476c-9e92-b768d058f603
  Query: SELECT all_v1.* FROM (SELECT all_v1.* FROM gdc-bq-sample.integration.all_v1 AS all_v1, UNNEST(ResearchSubject) AS _ResearchSubject WHERE ((_ResearchSubject.associated_project = 'TCGA-BRCA') AND (all_v1.days_to_birth < -50*365))) AS all_v1, UNNEST(identifier) AS _identifier WHERE (_identifier.system = 'IDC')
  Offset: 0
  Count: 88
  Total Row Count: 88
  More pages: False
