---
title: summarize_subjects()
---

For a set of CDA subject rows that all match a user-specified set of filters -- "result rows" -- get a report showing counts of values present in that
set of rows, profiled across (user-modifiable) columns of interest.

```
summarize_subjects(
    *,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    return_data_as='',
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
Restrict results to those deriving from the given upstream data source(s). Current valid values are 'GDC', 'IDC', 'PDC',
'GC' and 'ICDC'. (Default: no filter.)

### add_columns
( string or list of strings; optional ):
One or more columns from a second table to add to summary output.

### exclude_columns
( string or list of strings; optional ):
One or more columns to remove from summary output.

### return_data_as
( string; optional: 'dataframe_list' or 'dict' or 'json' ):
Specify how to return results: as a list of pandas DataFrames, as a
Python dictionary, or as output written to a JSON file named by the user.
If this argument is omitted, then for each DataFrame that would have
been returned by the 'dataframe_list' option, a table will be
pretty-printed to the standard output stream (and nothing will be returned).

### output_file
( string; optional ):
If return_data_as='json' is specified, output_file should contain a
resolvable path to a file into which summary_counts() will write
JSON-formatted results.

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
`size < 100`

String VALUEs need not be quoted inside of filter strings. For example, to include
the filters specified just above in the `match_all` argument, we can write:

`summarize_subjects( match_all=[ 'primary_disease_type = *duct*', 'sex = F*' ] )`

NULL is a special VALUE which can be used to match missing data. For
example, to get a count summary for rows where the `sex` field is missing data,
we can write:

`summarize_subjects( match_all=[ 'year_of_birth = NULL' ] )`

## Returns
        
list of pandas DataFrames, with one DataFrame for each summarized column,
enumerating counts (or statistically summarizing unbounded numeric values) over all of that column's data values appearing in any CDA subject rows that match the user-specified filter criteria (the 'result rows'). Two DataFrames in this list --
    'number_of_matching_subjects' and 'number_of_files_related_to_matching_subjects' --
will contain integers representing the total number of result subject rows and the
total number of related files, respectively. Every other DataFrame in the list
will be titled with a CDA column name and will contain value counts or statistical summaries for that column as filtered by the result row set.

OR

Python dictionary enumerating counts of all data values for each summarized column (or a statistical summary of those data values, in the case of unbounded numeric data) across all CDA subject rows that match the user-specified filter criteria (the 'result rows').
Two summary keys in this dictionary -- 
    'number_of_matching_subjects' and
    'number_of_files_related_to_matching_subjects' -- 
will point to integers representing the total number of result subject rows 
and the total number of associated file rows, respectively. Every other key 
in the dictionary will contain a CDA column name; every dictionary value 
will itself be a dictionary either enumerating observed counts of all values 
appearing in that column as filtered by the result row set, or encoding a
statistical summary of those values in the case of unbounded numeric data.

OR

JSON-formatted text representing the same structure as the `return_data_as='dict'` option, written to `output_file`.

OR 

returns nothing, but displays a series of tables to standard output
describing the same data returned by the other `return_data_as` options.

And yes, we know how those first two paragraphs look. We apologize to the entire English language