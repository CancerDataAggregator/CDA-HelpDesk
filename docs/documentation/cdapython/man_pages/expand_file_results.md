---
title: expand_file_results()
---

# `expand_file_results()`

## NAME

`expand_file_results` — flatten a nested per-file column into a 2-dimensional table

## SYNOPSIS

```python
expand_file_results(results_dataframe, column_to_expand)
```

## DESCRIPTION

Given a result DataFrame `R` returned by [`get_file_data()`](get_file_data.md), and a column `C` in `R` that contains DataFrames, return a version of the information in `C` expanded into a 2-dimensional table `T`, with one row in `T` for every row in every DataFrame in `C`, and with each row in `T` also containing the `file_id` in `R` that goes with that row.

## ARGUMENTS

- `results_dataframe` (*pandas.DataFrame, required*)
  A result DataFrame returned by `get_file_data()`.

- `column_to_expand` (*string, required*)
  The name of a column in `results_dataframe` whose values are themselves DataFrames (for example, a column produced via `collate_results=True`).

## RETURNS

`pandas.DataFrame` — a flattened, 2-dimensional table with one row per row of every nested DataFrame in `column_to_expand`, each annotated with its associated `file_id`.

## SEE ALSO

[`get_file_data()`](get_file_data.md), [`intersect_file_results()`](intersect_file_results.md)
