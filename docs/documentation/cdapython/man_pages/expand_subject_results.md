---
title: expand_subject_results()
---

# `expand_subject_results()`

## NAME

`expand_subject_results` — flatten a nested per-subject column into a 2-dimensional table

## SYNOPSIS

```python
expand_subject_results(results_dataframe, column_to_expand)
```

## DESCRIPTION

Given a result DataFrame `R` returned by [`get_subject_data()`](get_subject_data.md), and a column `C` in `R` that contains DataFrames, return a version of the information in `C` expanded into a 2-dimensional table `T`, with one row in `T` for every row in every DataFrame in `C`, and with each row in `T` also containing the `subject_id` in `R` that goes with that row.

## ARGUMENTS

- `results_dataframe` (*pandas.DataFrame, required*)
  A result DataFrame returned by `get_subject_data()`.

- `column_to_expand` (*string, required*)
  The name of a column in `results_dataframe` whose values are themselves DataFrames (for example, a column produced via `collate_results=True`).

## RETURNS

`pandas.DataFrame` — a flattened, 2-dimensional table with one row per row of every nested DataFrame in `column_to_expand`, each annotated with its associated `subject_id`.

## SEE ALSO

[`get_subject_data()`](get_subject_data.md), [`intersect_subject_results()`](intersect_subject_results.md)
