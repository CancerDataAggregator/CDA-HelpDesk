---
title: summarize_subjects()
---

# `summarize_subjects()`

**NAME**

`summarize_subjects` — get a value-count report profiling a filtered set of CDA subject rows

**SYNOPSIS**

````python
summarize_subjects(
    *search_terms,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    return_data_as='',
    output_file='',
    add_extras=None
)
````

**DESCRIPTION**

For a set of CDA subject rows that all match a user-specified set of filters — "result rows" — get a report showing counts of values present in that set of rows, profiled across (user-modifiable) columns of interest.

**ARGUMENTS**

- `search_terms` (*zero or more strings, optional*)
  One or more search terms (including phrases), all of which must be associated with each result row. A wildcard `*` at either or both ends of each term enables partial matches to longer values.
  Example: `summarize_subjects('kidney', 'adeno*', 'hispanic or latino')`

- `match_all` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings (see **FILTER STRINGS** below), **all** of which must be met by all result rows.

- `match_any` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **at least one** of which must be met by all result rows.

- `match_from_file` (*3-element dictionary of strings, optional*)
  A dictionary with three named elements:
  1. `input_file` — the name of a local TSV file (with column names in its first row)
  2. `input_column` — the name of a column in that TSV
  3. `cda_column_to_match` — the name of a CDA column

  Restricts result rows to those where the value of the given CDA column matches at least one value from the given column in the given TSV file.

- `data_source` (*string or list of strings, optional*)
  Restrict results to those deriving from the given upstream data source(s). Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'IDC'`, `'PDC'`, and `'ICDC'`. Default: no filter.

- `add_columns` (*string or list of strings, optional*)
  One or more columns from a second table to add to summary output.

- `exclude_columns` (*string or list of strings, optional*)
  One or more columns to remove from summary output.

- `return_data_as` (*string, optional: `'dataframe_list'`, `'dict'`, or `'json'`*)
  Specify how to return results: as a list of pandas DataFrames, as a Python dictionary, or as output written to a JSON file named by the user. If omitted, for each DataFrame that would have been returned by `'dataframe_list'`, a table is instead pretty-printed to standard output (and nothing is returned).

- `output_file` (*string, optional*)
  If `return_data_as='json'` is specified, `output_file` should contain a resolvable path to a file into which JSON-formatted results will be written.

- `add_extras` (*string or list of strings, optional*)
  One or more columns of extra metadata to include, to contextualize harmonized CDA column values. Current valid values are `'synonym_terms'`, `'slim_terms'`, `'containing_terms'`, and `'all'` (which includes all of the above). Default: no extras.

**FILTER STRINGS**

Filter strings are expressions of the form `"COLUMN_NAME OP VALUE"` (the whitespace surrounding `OP` is required), where:

- `COLUMN_NAME` is a searchable CDA column (see [`columns()`](columns.md))
- `OP` is one of: `<` `<=` `>` `>=` `=` `!=`
- `VALUE` is a value of whatever data type is stored in `COLUMN_NAME`, or the special keyword `NULL`, indicating the filter should match missing (null) values in `COLUMN_NAME`

`=` and `!=` work on numeric, boolean, and string values. `<` `<=` `>` `>=` work only on numeric values.

Partial matches to string values are supported by adding `*` to either or both ends. Examples:
