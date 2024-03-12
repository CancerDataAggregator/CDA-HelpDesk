---
title: columns()
comments: true
---

Get structured metadata describing searchable CDA columns.


`columns(*, return_data_as='', output_file='', sort_by='', debug=False, **filter_arguments)`

## Arguments

### return_data_as 
( string; optional: 'dataframe' or 'list' or 'tsv' ):
Specify how columns() should return results: as a pandas DataFrame,
a Python list, or as output written to a TSV file named by the user.
If this argument is omitted, columns() will default to returning
results as a DataFrame.

### output_file
( string; optional ):
If return_data_as='tsv' is specified, output_file should contain a
resolvable path to a file into which columns() will write
tab-delimited results.

### sort_by
( string or list of strings; optional:
any combination of 'table', 'column', 'data_type',
and/or 'nullable'):
Specify the column metadata field(s) on which to sort result data.
Results will be sorted first by the first named field; groups of
records sharing the same value in the first field will then be
sub-sorted by the second field, and so on.

Any field with a suffix of ':desc' appended to it will be sorted
in reverse order; adding ':asc' will ensure ascending sort order.
Example: sort_by=[ 'table', 'nullable:desc', 'column:asc' ]

### debug
( boolean; optional ):
If set to True, print internal process details to the standard
error stream.

## Filter arguments
### table
( string or list of strings; optional ):
Restrict returned data to columns from tables whose names match any
of the given strings. A wildcard (asterisk) at either end (or both
ends) of each string will allow partial matches. Case will be
ignored.

### column
( string or list of strings; optional ):
Restrict returned data to columns whose name matches any of the
given strings. A wildcard (asterisk) at either end (or both ends)
of each string will allow partial matches. Case will be ignored.

### data_type
( string or list of strings; optional ):
Restrict returned data to columns whose data type matches any of
the given strings. A wildcard (asterisk) at either end (or both
ends) of each string will allow partial matches. Case will be
ignored.

### nullable
( boolean; optional ):
If set to True, restrict returned data to columns whose values are
allowed to be empty; if False, return data only for columns
requiring nonempty values.

### description_contains
( string or list of strings; optional ):
Restrict returned data to columns whose `description` field matches
any of the given strings. Wildcards will be automatically applied
(end-to-end matching makes no sense here), emphasized by the name
'description_contains' and not 'description'. Case will be ignored.

### exclude_table
( string or list of strings; optional ):
Restrict returned data to columns from tables whose names do _not_
match any of the given strings. A wildcard (asterisk) at either end
(or both ends) of each string will allow partial matches. Case will
be ignored.

## Returns
pandas.DataFrame where each row is a metadata record describing one
searchable CDA column and is comprised of the following fields:

`table` (string: name of the CDA table containing this column)
`column` (string: name of this column)
`data_type` (string: data type of this column)
`nullable` (boolean: if True, this column can contain null values)
`description` (string: prose description of this column)

OR list of column names

OR returns nothing, but writes results to a user-specified TSV file
