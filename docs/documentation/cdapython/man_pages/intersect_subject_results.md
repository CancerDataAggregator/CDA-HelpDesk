---
title: intersect_subject_results()
---

# `intersect_subject_results()`

## NAME

`intersect_subject_results` — merge `get_subject_data()` results via intersection

## SYNOPSIS

```python
intersect_subject_results(*result_dfs_to_merge, ignore_added_columns=False)
```

## DESCRIPTION

Combine two or more DataFrames produced by [`get_subject_data()`](get_subject_data.md) via intersection: merge result data for all subjects present in **all** input DataFrames.

## ARGUMENTS

- `result_dfs_to_merge` (*two or more DataFrames, required*)
  DataFrames returned by `get_subject_data()`.

- `ignore_added_columns` (*boolean, optional*)
  Merge only columns from the subject table: avoids breakages in cases where added extra (non-subject) columns can't be merged, due to differences in how similar but different upstream queries produced the results being merged. Default: `False` — try to merge subject data plus all extra data appearing in all input DataFrames.

## RETURNS

`pandas.DataFrame` containing combined metadata about all subject rows that appear in all input DataFrames, including, by default, all associated non-subject data present in all input DataFrames.

## SEE ALSO

[`get_subject_data()`](get_subject_data.md), [`expand_subject_results()`](expand_subject_results.md)
