---
title: intersect_file_results()
---

Combine two or more DataFrames produced by get_file_data() via intersection: merge result data for
all files present in all input DataFrames.

```
intersect_file_results(*result_dfs_to_merge, ignore_added_columns=False)
```

## Arguments

### two or more DataFrames returned by get_file_data()

### ignore_added_columns
( boolean; optional ):
Merge only columns from the file table: avoids breakages in
cases where added extra (non-file) columns can't be merged due
to differences in how similar but different upstream queries produced
the results we're trying to merge.
(Default: False: try to merge file data plus all extra data appearing in
all input DataFrames.)

## Returns:
A pandas.DataFrame containing combined metadata about all file rows that
appear in all input DataFrames, including by default all associated 
non-file data present in all input DataFrames.