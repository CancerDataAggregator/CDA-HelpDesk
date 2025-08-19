---
title: intersect_subject_results()
---

Combine two or more DataFrames produced by get_subject_data() via intersection: merge result data for
all subjects present in all input DataFrames.

```
intersect_subject_results(*result_dfs_to_merge, ignore_added_columns=False)
```

## Arguments

### two or more DataFrames returned by get_subject_data()

### ignore_added_columns
( boolean; optional ):
Merge only columns from the subject table: avoids breakages in
cases where added extra (non-subject) columns can't be merged due
to differences in how similar but different upstream queries produced
the results we're trying to merge.
(Default: False: try to merge subject data plus all extra data appearing in
all input DataFrames.)

## Returns:
A pandas.DataFrame containing combined metadata about all subject rows that
appear in all input DataFrames, including by default all associated 
non-subject data present in all input DataFrames.