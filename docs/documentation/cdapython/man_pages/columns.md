---
title: columns()
---

# `columns()`

## NAME

`columns` — get structured metadata describing searchable CDA columns

## SYNOPSIS

```python
columns(*, return_data_as='', output_file='', sort_by='', **filter_arguments)
```

## DESCRIPTION

Get structured metadata describing searchable CDA columns.

## ARGUMENTS

- `return_data_as` (*string, optional: `'dataframe'`, `'list'`, or `'tsv'`*)
  Specify how `columns()` should return results: as a pandas DataFrame, a Python list, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which `columns()` will write tab-delimited results.

- `sort_by` (*string or list of strings, optional: any combination of `'table'`, `'column'`, `'data_type'`, and/or `'nullable'`*)
  Specify the column metadata field(s) on which to sort result data. Results are sorted first by the first named field; groups of records sharing the same value in that field are then sub-sorted by the second field, and so on.

  Appending `:desc` to a field name sorts it in reverse order; `:asc` ensures ascending order.
  Example: `sort_by=['table', 'nullable:desc', 'column:asc']`

## FILTER ARGUMENTS

- `table` (*string or list of strings, optional*)
  Restrict returned data to columns from tables whose names match any of the given strings. A wildcard (`*`) at either or both ends of each string allows partial matches. Case is ignored.

- `column` (*string or list of strings, optional*)
  Restrict returned data to columns whose name matches any of the given strings. Wildcards and case-insensitivity apply as above.

- `data_type` (*string or list of strings, optional*)
  Restrict returned data to columns whose data type matches any of the given strings. Wildcards and case-insensitivity apply as above.

- `nullable` (*boolean, optional*)
  If `True`, restrict returned data to columns whose values are allowed to be empty; if `False`, return data only for columns requiring nonempty values.

- `description` (*string or list of strings, optional*)
  Restrict returned data to columns whose `description` field matches any of the given strings. Wildcards are applied automatically if not provided, to support straightforward keyword searching without extra punctuation. Case is ignored.

- `exclude_table` (*string or list of strings, optional*)
  Restrict returned data to columns from tables whose names do **not** match any of the given strings. Wildcards and case-insensitivity apply as above.

## RETURNS

`pandas.DataFrame` where each row is a metadata record describing one searchable CDA column, comprised of:

| Field | Type | Description |
|---|---|---|
| `table` | string | name of the CDA table containing this column |
| `column` | string | name of this column |
| `data_type` | string | data type of this column |
| `nullable` | boolean | if `True`, this column can contain null values |
| `description` | string | prose description of this column |

— or —

`list` of column names

— or —

nothing; results are written to a user-specified TSV file

## SEE ALSO

[`column_values()`](column_values.md), [`tables()`](tables.md), [`cda_functions()`](cda_functions.md)
