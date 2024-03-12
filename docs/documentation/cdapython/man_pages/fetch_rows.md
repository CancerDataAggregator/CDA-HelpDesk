---
title: fetch_rows()
comments: true
---

Get CDA data records ('result rows') from `table` that match user-specified criteria.


```
fetch_rows(table=None, *, match_all=[], match_some=[], link_to_table='', add_columns=[], data_source=[], count_only=False, debug=False)
```

## Arguments
### table
( string; required ):
The table whose rows are to be filtered and retrieved. (Run the tables()
function to get a list.)

### match_all 
( string or list of strings; optional ):
One or more conditions, expressed as filter strings (see below),
ALL of which must be met by all result rows.

### match_some 
( string or list of strings; optional ):
One or more conditions, expressed as filter strings (see below),
AT LEAST ONE of which must be met by all result rows.

### link_to_table 
( string; optional ):
A second table from which to fetch rows related to the row results
from `table` that this function produces. `link_to_table` results
will be appended to `table` rows to which they're related:
any `table` row related to more than one `link_to_table` row will
be repeated in the returned data, with one distinct `link_to_table` row
appended to each repeated copy of its related `table` row.
Note: if `link_to_table` is specified, the `add_columns` parameter will be
overridden and ignored.

### add_columns 
( string or list of strings; optional ):
One or more columns from a second table to add to result data from `table`.
If multiple values from an added column are all associated with a single
`table` row, that row will be repeated once for each distinct value, with
the added data appended to each row.

### data_source 
( string or list of strings; optional ):
Restrict results to those deriving from the given upstream data source(s), such
as 'GDC', 'IDC', 'PDC', or 'CDS'. (Default: no filter.)

### count_only 
( boolean; optional ):
If set to True, fetch_rows() will return two integers: the number of CDA
`table` rows matching the specified filters, and the total number of rows
that this function would return if `count_only` were not True. (These numbers
will be identical if no data from outside `table` has been joined to result
rows. If `count_only` is set to False (the default), fetch_rows() will
return a pandas DataFrame containing all CDA `table` rows that match the
given filters.

### debug 
( boolean; optional ):
If set to True, internal process details will be printed to the standard error
stream as fetch_rows() is running. If False (the default), ...they won't.

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
the filters specified just above in the `match_all` argument, when querying
the `subject` table, we can write:

`fetch_rows( table='subject', match_all=[ 'primary_disease_type = *duct*', 'sex = F*' ] )`

NULL is a special VALUE which can be used to match missing data. For
example, to get `researchsubject` rows where the `primary_diagnosis_site` field
is missing data, we can write:

`fetch_rows( table='researchsubject', match_all=[ 'primary_diagnosis_site = NULL' ] )`

## Returns
integer representing the total number of CDA `table` rows matching the given
filters (if count_only=True)

OR

pandas.DataFrame containing CDA `table` rows matching the user-specified
filter criteria. The DataFrame's named columns will match columns in `table`,
and each row in the DataFrame will contain one CDA `table` row (possibly
with related data from a second table appended to it, according to user
directives).