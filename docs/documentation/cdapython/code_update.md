---
title:  Updating your code from cdapython beta
---

# Updating your code from cdapython beta

We've added a few features while also simplifying the cdapython interface to make search faster and easier. This page provides a one-to-one mapping for all of the previous functions of cda-python to their new forms. If you need more help updating your code base, please contact us cancerdataaggregator `@` gmail.com

## Global changes

### Install

- old: install from github
- new: `pip install git+https://github.com/CancerDataAggregator/cdapython.git`

*** If you previously installed cdapython in a VM, discard that VM and install in a fresh one. The new cdapython has dependency conflicts with the old version and will not install properly over the older version ***

### Import

- old: `from cdapython import Q, columns, unique_terms`
- new: `from cdapython import tables, columns, column_values, fetch_rows, summary_counts`

### See help text

- old: N/A
- new: `help(<functionname>)`

- old: N/A
- new: in any function, add a `debug=True` parameter to get detailed error information

### Output Type

- old: some functions could have `to_dataframe()`, `to_list`, or `to_csv` appended, others had a parameter
- new: all functions that return matrix-like data (columns, column_values, and fetch_rows) take the two parameters `return_data_as` and `output_file`. `return_data_as` can be set to dataframe, list or tsv. When tsv is specified, use `output_file` to supply a path/to/filename.tsv

### List all tables

- old: N/A
- new: `tables()` simple function that returns a list of currently queryable table names

## Specific function updates

### List all columns

function is still `columns()`

#### columns flags

- old: `page_size`, `limit`, and `description` parameters have been removed
- new: columns always returns all unique values and their counts by default, however there are several new parameters

- new: `sort_by=<column:asc/desc>` sort results by any column

- new: `filters=<variable or list of variables>` You can now filter out any column(s) entirely, or apply filters by row to any column(s). [Full filter list.](#filter-arguments)

See [columns](../man_pages/columns/) for more details

### See all unique values for a given column

- old: `unique_terms()`
- new: `column_values()` 

#### parameters

- old: `page_size`, `limit`, and `count` parameters have been removed
- new: column_values always returns all unique values and their counts by default, however there are several new parameters

- old: `system=<data source>`
- new: `data_source=<data source>` can now take a list, as in `data_source=["GDC", "PDC"]`

- new: `sort_by=<column:asc/desc>` sort results by any column
- new: `force=<True/False>` For columns with an extremely large number of unique values, such as filename, the query will fail with a large data warning. You can override the warning with `Force=True`

See [column_values](../man_pages/column_values/) for more details

### Summarize results

- old: `<queryobject>.<table>.count.run()`
- new: `summary_counts(table=<table>, <optional parameters>)` running this command with no parameters will return counts for the entire table.

#### parameters

- new: `match_all=<filter or list of filters>`. This is effectively `AND` for all of the listed filters, any of which can take a `*` wildcard e.g. `match_all=["sex = male", "data_type = *sv"]`

- new: `match_any=<filter or list of filters>`. This is effectively `OR` for all of the listed filters, all of which can take a `*` wildcard e.g. `match_all=["sex = male", "data_type = *sv"]`

- new: `data_source` restrict the results to a data_source(s), e.g. `data_source=['GDC', 'IDC']`

See [summary_counts](../man_pages/summary_counts/) for more details

### Returning a matrix of results

- old: all of the functions previously used with, or chained onto `Q()...run()` have been replaced with the single function `fetch_rows()`
- new: `fetch_rows(table=<table>, <optional parameters>)

#### parameters

- new: `match_all=<filter or list of filters>`. This is effectively `AND` for all of the listed filters, any of which can take a `*` wildcard e.g. `match_all=["sex = male", "data_type = *sv"]`

- new: `match_any=<filter or list of filters>`. This is effectively `OR` for all of the listed filters, all of which can take a `*` wildcard e.g. `match_all=["primary_diagnosis = neuro*", "days_to_birth > 600"]`

- new: `data_source` restrict the results to a data_source(s), e.g. `data_source=['GDC', 'IDC']`

- new: `link_to_table=<table>` will return your results joined to the specifed table

- new: `provenance=<True/False>` will return your results expanded to show which data_source each row came from, and the accompanying identifiers

- new: `count_only=<True/False>` will return a simple row count for your results rather than the results themselves

See [fetch_rows](../man_pages/fetch_rows/) for more details
