---
title: get_subject_data()
---

# `get_subject_data()`

**NAME**

`get_subject_data` — get CDA subject rows matching user-specified criteria

**SYNOPSIS**

```python
get_subject_data(
    *search_terms,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    collate_results=False,
    include_external_refs=False,
    return_data_as='dataframe',
    output_file='',
    add_extras=None
)
```

**DESCRIPTION**

Get CDA subject rows ("result rows") that match user-specified criteria.

**ARGUMENTS**

- `search_terms` (*zero or more strings, optional*)
  One or more search terms (including phrases), all of which must be associated with each result row. A wildcard `*` at either or both ends of each term enables partial matches to longer values.
  Example: `get_subject_data('kidney', 'adeno*', 'hispanic or latino')`

- `match_all` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings (see **FILTER STRINGS** below), **all** of which must be met by all result rows.

- `match_any` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **at least one** of which must be met by all result rows.

- `match_from_file` (*3-element dictionary of strings, optional*)
  A dictionary with three named elements:
  1. `input_file` — the name of a local TSV file (with column names in its first row)
  2. `input_column` — the name of a column in that TSV
  3. `cda_column_to_match` — the name of a CDA column

  Restricts result rows to those where the value of the given CDA column matches at least one value from the given column in the given TSV file. If matching on native source identifiers (e.g. a GDC case UUID) rather than CDA's own subject IDs, match against `upstream_id` instead of `subject_id`.

- `data_source` (*string or list of strings, optional*)
  Restrict results to those deriving from the given upstream data source(s). Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'IDC'`, `'PDC'`, and `'ICDC'`. Default: no filter.

- `add_columns` (*string or list of strings, optional*)
  One or more columns from a second table to add to result data.

- `exclude_columns` (*string or list of strings, optional*)
  One or more columns to remove from result data.

- `collate_results` (*boolean, optional*)
  If `True`: for each result subject, include a DataFrame collating results linked to that subject from each non-subject table that was queried. Otherwise, for each result subject, include a list of unique values associated with that subject from each non-subject column that was queried. Default: `False`.

- `include_external_refs` (*boolean, optional*)
  If `True`: for each result subject, include a DataFrame called `external_reference_data` that collates references to external resources containing data describing that subject. Default: `False`.

- `return_data_as` (*string, optional: `'dataframe'` or `'tsv'`*)
  Specify how to return results: as a pandas DataFrame, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which tab-delimited results will be written.

- `add_extras` (*string or list of strings, optional*)
  One or more columns of extra metadata to include, to contextualize harmonized CDA column values. Current valid values are `'synonym_terms'`, `'slim_terms'`, `'containing_terms'`, and `'all'` (which includes all of the above). Default: no extras.

**FILTER STRINGS**

Filter strings are expressions of the form `"COLUMN_NAME OP VALUE"` (the whitespace surrounding `OP` is required), where:

- `COLUMN_NAME` is a searchable CDA column (see [`columns()`](columns.md))
- `OP` is one of: `<` `<=` `>` `>=` `=` `!=`
- `VALUE` is a value of whatever data type is stored in `COLUMN_NAME`, or the special keyword `NULL`, indicating the filter should match missing (null) values in `COLUMN_NAME`

`=` and `!=` work on numeric, boolean, and string values. `<` `<=` `>` `>=` work only on numeric values.

Partial matches to string values are supported by adding `*` to either or both ends. Examples:
   diagnosis = duct
   sex = F*

String values need not be quoted inside filter strings:

```python
get_subject_data(match_all=['diagnosis = *duct*', 'sex = F*'])
```

`NULL` matches missing data:

```python
get_subject_data(match_all=['cause_of_death = NULL'])
```

**RETURNS**

(Default) `pandas.DataFrame` containing CDA subject data matching the user-specified filter criteria. The DataFrame's named columns match columns in the `subject` table plus any optional user-added columns from other tables, and each row represents one CDA `subject` row (possibly with related data from other tables appended, according to user directives).

— or —

nothing; results are written to a user-specified TSV file.

**SEE ALSO**

[`get_file_data()`](get_file_data.md), [`summarize_subjects()`](summarize_subjects.md), [`intersect_subject_results()`](intersect_subject_results.md), [`expand_subject_results()`](expand_subject_results.md), [`columns()`](columns.md)
