---
title: summary_counts_()
comments: true
---

For a set of rows in a user-specified table that all match a user-specified set of filters, get
a report showing counts of values present in that set of rows, profiled across a small set of
pre-selected columns.

`summary_counts(table='', *, match_all=[], match_some=[], data_source=[], debug=False)`


## Arguments
### table
( string; required ):
The table whose rows are to be filtered and counted. (Run the tables()
function to get a list.)

### match_all
( string or list of strings; optional ):
One or more conditions, expressed as filter strings (see below),
ALL of which must be met by all result rows.

### match_some
( string or list of strings; optional ):
One or more conditions, expressed as filter strings (see below),
AT LEAST ONE of which must be met by all result rows.

### data_source
( string or list of strings; optional ):
Restrict results to those deriving from the given upstream data source(s), such
as 'GDC', 'IDC', 'PDC', or 'CDS'. (Default: no filter.)

### debug
( boolean; optional ):
If set to True, internal process details will be printed to the standard error
stream as summary_counts() is running. If False (the default), ...they won't.

## Filter strings
Filter strings are expressions of the form "COLUMN_NAME OP VALUE"
(note in particular that the whitespace surrounding OP is required),
where

- COLUMN_NAME is a searchable CDA column (see the columns() function
for details)

- OP is one of: `< <=  > >= = !=`

- VALUE is a particular value of whatever data type is stored
in COLUMN_NAME (see the columns() function for details), or
the special keyword NULL, indicating the filter should match
missing (null) values in COLUMN_NAME.

Operators `=` and `!=` will work on numeric, boolean and string VALUEs.

Operators `< <= > >=` will only work on numeric VALUEs.

Users can require partial matches to string VALUEs by adding `*` to either or
both ends. For example:

`primary_disease_type = *duct*`
`sex = F*`

String VALUEs need not be quoted inside of filter strings. For example, to include
the filters specified just above in the `match_all` argument, we can write:

`summary_counts( table='subject', match_all=[ 'primary_disease_type = *duct*', 'sex = F*' ] )`

NULL is a special VALUE which can be used to match missing data. For
example, to get a count summary for rows where the `sex` field is missing data,
we can write:

`summary_counts( table='subject', match_all=[ 'sex = NULL' ] )`

## Returns
Python dictionary enumerating counts of all data values (from a small set of pre-selected columns)
appearing in any of the rows of the user-specified `table` that match the user-specified filter criteria
(the 'result rows'). One or two summary keys in this dictionary -- 'total_`table`_matches', and
sometimes 'total_related_files', where appropriate -- will point to integers representing
the number of result rows and the number of files related to those rows, respectively. All other keys
in the dictionary will each contain a CDA column name; each corresponding value will itself be a
dictionary enumerating all the specific values appearing in the result rows for the CDA column
named in the key. Each value in that (sub-)dictionary will represent the total number of times
that its corresponding key appears in the result rows.

And yes, we know how that paragraph looks. We apologize to the entire English language.