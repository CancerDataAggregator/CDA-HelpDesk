---
title: get_file_data()
---

Get CDA file rows ('result rows') that match user-specified criteria.


```
get_file_data(
    *,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    collate_results=False,
    include_external_refs=False,
    return_data_as='dataframe',
    output_file=''
)
```

## Arguments

### match_all 
( string or list of strings; optional ):
One or more conditions, expressed as filter strings (see below),
ALL of which must be met by all result rows.

### match_any 
( string or list of strings; optional ):
One or more conditions, expressed as filter strings (see below),
AT LEAST ONE of which must be met by all result rows.

### match_from_file 
( 3-element dictionary of strings; optional ):
A dictionary containing 3 named elements:
    1. 'input_file': The name of a (local) TSV file (with column names in its first row)
    2. 'input_column': The name of a column in that TSV
    3. 'cda_column_to_match': The name of a CDA column
Restrict result rows to those where the value of the given CDA
column matches at least one value from the given column
in the given TSV file.

### data_source 
( string or list of strings; optional ):
Restrict results to those deriving from the given upstream
data source(s). Current valid values are 'GDC', 'IDC', 'PDC',
'GC' and 'ICDC'. (Default: no filter.)

### add_columns 
( string or list of strings; optional ):
One or more columns from a second table to add to result data.

### exclude_columns 
( string or list of strings; optional ):
One or more columns to remove from result data.

### collate_results
( boolean; optional ):
If True: for each result file, include a DataFrame collating
results linked to that file from each non-file table that was
queried. Otherwise, for each result file, include a list of
unique values associated with that file from each non-file
column that was queried. Defaults to False.

### return_data_as
( string; optional: 'dataframe' or 'tsv' ):
Specify how to return results: as a pandas DataFrame,
or as output written to a TSV file named by the user. If this
argument is omitted, the default is to return results as a DataFrame.
    
### output_file
( string; optional ):
 If return_data_as='tsv' is specified, `output_file` should contain a
resolvable path to a file into which tab-delimited results will be
written.

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

`diagnosis = *duct*`

`sex = F*`

String VALUEs need not be quoted inside of filter strings. For example, to include
the filters specified just above in the `match_all` argument, when querying
the `file` table, we can write:

`get_file_data( match_all=[ 'diagnosis = *duct*', 'sex = F*' ] )`

NULL is a special VALUE which can be used to match missing data. For
example, to get CDA file data for which the `cause_of_death` field
is missing data, we can write:

`get_file_data( match_all=[ 'cause_of_death = NULL' ] )`

## Returns
(Default) A pandas.DataFrame containing CDA file data matching the user-specified filter criteria. The DataFrame's named columns will match columns in the `file` table plus any optional user-added columns from other tables, and each row in the DataFrame will represent one CDA `file` row (possibly with related data from other tables appended to it, according to user directives).

OR

returns nothing, but writes results to a user-specified TSV file