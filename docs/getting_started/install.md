---
title:  Local installation docs
comments: true
---

# Installation Guide

cdapython runs on:

Mac OS python versions: 3.8, 3.9, 3.10

Ubuntu python versions 3.8, 3.9, 3.10

Windows python versions: 3.8, 3.9, 3.10


## Conda + Pip install

!!! requirements

    - terminal/command line
    - python version >= 3.8 [(Install)](https://www.python.org/downloads/)
    - pip version >= 

1. In your terminal type:

  ```bash
  pip install cdapython
  ```
## Terminal/Command line

cdapython is a python package, to run on the command line, start python

```bash
python3
```
and import the cdapython modules:

```python
from cdapython.data_exploration import tables, columns, column_values, column_data_types
from cdapython.fetch import fetch_rows
from cdapython.query import summary_counts
```
## Interactive notebook

cdapython comes with jupyter notebook installed, and our documentation is all available as jupyter notebooks. To start a notebook server, go to your command line/terminal and type:

```bash
jupyter notebook
```
This will launch an interactive notebook in your webbrowser. Be sure to import the cdapython modules in your first notebook block:

```python
from cdapython.data_exploration import tables, columns, column_values, column_data_types
from cdapython.fetch import fetch_rows
from cdapython.query import summary_counts
```



