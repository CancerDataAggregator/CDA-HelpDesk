---
title: intersect_file_results()
---

# `intersect_file_results()`

**NAME**

`intersect_file_results` — merge `get_file_data()` results via intersection

**SYNOPSIS**

```python
intersect_file_results(*result_dfs_to_merge, ignore_added_columns=False)
```

**DESCRIPTION**

Combine two or more DataFrames produced by [`get_file_data()`](get_file_data.md) via intersection: merge result data for all files present in **all** input DataFrames.

**ARGUMENTS**

- `result_dfs_to_merge` (*two or more DataFrames, required*)
  DataFrames returned by `get_file_data()`.

- `ignore_added_columns` (*boolean, optional*)
  Merge only columns from the file table: avoids breakages in cases where added extra (non-file) columns can't be merged, due to differences in how similar but different upstream queries produced the results being merged. Default: `False` — try to merge file data plus all extra data appearing in all input DataFrames.

**RETURNS**

`pandas.DataFrame` containing combined metadata about all file rows that appear in all input DataFrames, including, by default, all associated non-file data present in all input DataFrames.

**SEE ALSO**

[`get_file_data()`](get_file_data.md), [`expand_file_results()`](expand_file_results.md), [`intersect_subject_results()`](intersect_subject_results.md)