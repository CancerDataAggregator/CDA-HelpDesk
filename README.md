# Access the Help Desk

To ask questions, submit bugs, or request features [click here](https://github.com/CancerDataAggregator/CDA-HelpDesk/discussions) or on the `Discussions` tab at the top of this page.

# About

This repository contains all of the documentation for [CDA python](https://github.com/CancerDataAggregator/cdapython)

It is designed using the [Material template by Martin Donath](https://squidfunk.github.io/mkdocs-material/) and built using [readthedocs](https://readthedocs.org/)

## Example Notebooks

All example notebooks are dynamically built when the site is rendered for viewing on the web, and can be downloaded from the website.
Interactive versions of those notebooks can be used at this link:

[Google Colab Notebooks](https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Tutorials/Welcome.ipynb)

# Cancer Data Aggregator — Documentation Site

Source for the CDA documentation site, built with `mkdocs` + the `readthedocs` theme.

## Structure

- `getting_started/` — install, no-install (Colab), and routing for new users
- `interactive.ipynb` — no-code, in-browser search (static dataframe, client-side filtering)
- `documentation/cdapython/vignettes/` — five standalone, goal-based `cdapython` walkthroughs
- `documentation/cdapython/man_pages/` — function reference, one page per function
- `documentation/developers/` — REST API reference (Redoc, generated from `service_openapi.yaml`)
- `release_notes/` — code and data release history

## Build locally

```bash
pip install -r requirements.txt
mkdocs serve
```

## Build on Read the Docs

Push to GitHub, import on readthedocs.org — picks up `.readthedocs.yaml` automatically.

## Notebook execution

`mkdocs-jupyter` runs with `execute: true`, `allow_errors: false` — every vignette and the Quick Reference notebook execute against the live API at build time, so displayed counts are always current.

## Funding

This project has been funded in whole or in part with Federal funds from the National Cancer Institute, National Institutes of Health, Task Order No. 17X053 under Contract No. HHSN261200800001E