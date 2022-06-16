---
title: subject fields
---

The subject endpoint uses a subject attributes first schema, where all metadata is nested under subject values.

Column names that have a `.` between words denote that the term after the `.` is a nested field. Nesting structure can be more easily browsed in the [subject JSON schema](./subjects_schema.md)

{{ read_csv('docs/Model/subjecttable.csv') }}
