---
title:  Local installation docs
---

# Installation Guide

cdapython runs on:

python versions >= 3.9

## Pip install

!!! requirements

    - terminal/command line
    - python version >= 3.9 [(Install)](https://www.python.org/downloads/)
    - pip version >= 

1. In your terminal type:

  ```bash
  pip install git+https://github.com/CancerDataAggregator/cdapython.git
  ```
## Terminal/Command line

cdapython is a python package, to run on the command line, start python

```bash
python3
```
and import the cdapython modules:

```python
from cdapython import tables, columns, column_values,  fetch_rows, summary_counts
```
## Interactive notebook

cdapython comes with jupyter notebook installed, and our documentation is all available as jupyter notebooks. To start a notebook server, go to your command line/terminal and type:

```bash
jupyter notebook
```
This will launch an interactive notebook in your browser. Be sure to import the cdapython modules in your first notebook block:

```python
from cdapython import tables, columns, column_values,  fetch_rows, summary_counts
```



