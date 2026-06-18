---
title: column_values()
---

Show all distinct values present in `column`, along with a count
of occurrences for each value.

```
column_values
(column='', *, return_data_as='dataframe', output_file='', sort_by='', filters='', data_source='', force=False, debug=False)
```


## Arguments

### column
( string; required ):
The column to fetch values from.

### return_data_as
( string; optional:'dataframe'(default) or 'list' or 'tsv' ):
Specify how `column_values()` should return results: as a pandas
DataFrame, a Python list, or as output written to a TSV file named
by the user. If this argument is omitted, column_values() will default
to returning results as a DataFrame.

### output_file
( string; optional ):
If return_data_as='tsv' is specified, output_file should contain a
resolvable path to a file into which column_values will write tab-delimited results.

### sort_by
( string; optional:'count'( default for `return_data_as='dataframe'` and `return_data_as='tsv'` ) or 'value'( default for `return_data_as='list'` ) or '`count:desc`' or '`value:desc`' or '`count:asc`' or '`value:asc`' ):

Specify the primary column to sort when preparing result data: on
values, or on counts of values.

A column name with a suffix of '`:desc`' appended to it will be
sorted in reverse order; adding '`:asc`' will ensure ascending sort
order. Example: `sort_by='value:desc'`

Secondary sort order is automatic: if the results are to be
primarily sorted by count, then the automatic behavior will be to
also (alphabetically) sort by value within each group of values
that all share the same count. If results are primarily sorted by
value, then there is no secondary sort -- each value is unique by
design, so results don't contain groups with the same value but
different counts, so there's nothing to arrange once the primary
sort has been applied.

### filters

( string or list of strings; optional ):

Restrict returned values to those matching any of the given strings.
A wildcard (asterisk) at either end (or both ends) of each string
will allow partial matches. Case will be ignored. Use an empty
filter string '' to match and count missing (null) values.

### data_source

( string; optional ):
Restrict returned values to the given upstream data source, such
as 'GDC', 'PDC', 'IDC', 'GC' and 'ICDC'. Defaults to `''` (no filter).

### force
( boolean; optional ): 
Force execution of high-overhead queries on columns (like IDs)
flagged as having large numbers of values. Defaults to False, in which case attempts to retrieve values for flagged columns will result in a warning.

## Returns
pandas.DataFrame 

OR

list

OR

returns nothing, but writes retrieved data to a user-specified TSV file
