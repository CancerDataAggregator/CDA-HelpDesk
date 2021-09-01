Basics Usage
============

.. _Usage:
We will now show you the basic structure of `CDA python` through the use of the most commands:

- ``columns()``: show all available columns in the table,
- ``unique_terms()``: for a given column show all unique terms,
- ``Q``: Executes this query on the public CDA server, and
- ``Q.sql``: allows you to enter SQL style queries.
- ``single_operator_parser`` : allows you to write long form Q statments with out chaining

colums
-------

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
 ...
 
 
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
