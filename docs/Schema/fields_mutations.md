---
title: Mutation Endpoint fields
---

The mutation endpoint contains data from TCGA about genes and mutations

Column names that have a `.` between words denote that the term after the `.` is a nested field. Nesting structure can be more easily browsed in the [file JSON schema](./schema_file.md)

{{ read_csv('docs/Schema/csvs/fields_mutation.csv') }}
