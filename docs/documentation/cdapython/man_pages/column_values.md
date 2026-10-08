---
title: column_values()
---

# `column_values()`

**NAME**

`column_values` — show all distinct values present in a column, with occurrence counts

**SYNOPSIS**

````python
column_values(
    column='',
    *,
    return_data_as='',
    output_file='',
    sort_by='',
    filters=None,
    data_source=None,
    force=False
)
````

**DESCRIPTION**

Show all distinct values present in `column`, along with a count of occurrences for each value.

**ARGUMENTS**

- `column` (*string, required*)
  The column to fetch values from.

- `return_data_as` (*string, optional: `'dataframe'`, `'list'`, or `'tsv'`*)
  Specify how `column_values()` should return results: as a pandas DataFrame, a Python list, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which `column_values()` will write tab-delimited results.

- `sort_by` (*string, optional: `'count'` (default for `return_data_as='dataframe'` and `'tsv'`), `'value'` (default for `return_data_as='list'`), `'count:desc'`, `'value:desc'`, `'count:asc'`, or `'value:asc'`*)
  Specify the primary field to sort when preparing result data: on values, or on counts of values.

  A field name with a suffix of `:desc` appended to it will be sorted in reverse order; adding `:asc` will ensure ascending sort order. Example: `sort_by='value:desc'`

  Secondary sort order is automatic: if results are primarily sorted by count, they are also (alphabetically) sorted by value within each group of values sharing the same count. If results are primarily sorted by value, there is no secondary sort — each value is unique by design, so there are no same-value groups with differing counts to further arrange.

- `filters` (*string or list of strings, optional*)
  Restrict returned values to those matching any of the given strings. A wildcard (`*`) at either or both ends of each string allows partial matches. Case is ignored. Specify an empty filter string `''` to match and count missing (null) values.

- `data_source` (*string, optional*)
  Restrict returned values to the given upstream data source. Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'PDC'`, `'IDC'`, and `'ICDC'`. Defaults to `None` (no filter).

- `force` (*boolean, optional*)
  Force execution of high-overhead queries on columns (like IDs) flagged as having large numbers of values. Defaults to `False`, in which case attempts to retrieve values for flagged columns result in a warning.

**RETURNS**

`pandas.DataFrame` — or — `list` — or — nothing; results are written to a user-specified TSV file.

**SEE ALSO**

[`columns()`](columns.md), [`tables()`](tables.md), [`cda_functions()`](cda_functions.md)
