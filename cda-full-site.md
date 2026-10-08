# CDA Website — Complete Publish-Ready File Set

Every file below is final content — copy each into the path shown. Files not shown (CSS, data YAML, requirements, readthedocs config, service_openapi.yaml, images) are listed at the bottom as "carry over unchanged from your existing repo" since their content doesn't change.

---

## `mkdocs.yml`

```yaml
site_name: Cancer Data Aggregator
site_description: Search and aggregate cancer data across multiple data commons

theme:
  name: readthedocs
  highlightjs: true

plugins:
  - search
  - mkdocs-jupyter:
      execute: true
      allow_errors: false
      include_source: true
  - macros:
      module_name: main

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tilde
  - pymdownx.snippets:
      base_path: docs
      check_paths: true

extra_css:
  - css/cards.css

nav:
  - Home: index.md
  - Getting Started:
    - Overview: getting_started/index.md
    - Install locally: getting_started/install.md
    - No installation (Colab): getting_started/no-install.md
  - Interactive Search: interactive.ipynb
  - Vignettes:
    - Conceptual Overview: documentation/cdapython/vignettes/index.md
    - "1. Is there anything about X?": documentation/cdapython/vignettes/01_global_search.ipynb
    - "2. Getting oriented before I filter": documentation/cdapython/vignettes/02_systematic_browsing.ipynb
    - "3. I have subjects, what else exists": documentation/cdapython/vignettes/03_match_from_file.ipynb
    - "4. Reassembling a scattered project": documentation/cdapython/vignettes/04_cptac_reassembly.ipynb
    - "5. Subjects with multiple data types": documentation/cdapython/vignettes/05_multimodal_patients.ipynb
  - Developers:
    - API Reference: documentation/developers/index.md
  - Function Reference:
    - "Quick Reference": documentation/cdapython/man_pages/index.ipynb
    - cda_functions(): documentation/cdapython/man_pages/cda_functions.md
    - tables(): documentation/cdapython/man_pages/tables.md
    - columns(): documentation/cdapython/man_pages/columns.md
    - column_values(): documentation/cdapython/man_pages/column_values.md
    - summarize_subjects(): documentation/cdapython/man_pages/summarize_subjects.md
    - summarize_files(): documentation/cdapython/man_pages/summarize_files.md
    - get_subject_data(): documentation/cdapython/man_pages/get_subject_data.md
    - get_file_data(): documentation/cdapython/man_pages/get_file_data.md
    - intersect_subject_results(): documentation/cdapython/man_pages/intersect_subject_results.md
    - expand_subject_results(): documentation/cdapython/man_pages/expand_subject_results.md
    - intersect_file_results(): documentation/cdapython/man_pages/intersect_file_results.md
    - expand_file_results(): documentation/cdapython/man_pages/expand_file_results.md
  - Helpdesk: helpdesk/index.md
  - About Us:
    - about_us/index.md
    - about_us/ourdata.md
  - Release Notes:
    - "Code Release Notes": release_notes/cdapython.md
    - "Data Release Notes": release_notes/data_updates.md
```

---

## `requirements.txt`

```
mkdocs-jupyter
mkdocs-macros-plugin
pyyaml
ipykernel
cdapython
itables
```

---

## `.readthedocs.yaml`

```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

mkdocs:
  configuration: mkdocs.yml

python:
  install:
    - requirements: requirements.txt
```

---

## `main.py` (repo root — macros plugin hook)

```python
"""
mkdocs-macros-plugin hook file.

Defines two macros, both reading from docs/_data/release_status.yml:
  {{ data_available_widget() }}   -- compact, unused currently but kept for future use
  {{ data_available_table() }}    -- full detail, used on homepage and release notes

FRAMING NOTE: CDA pulls a fresh copy of every source at every single CDA release --
extraction timing is NOT the variable here, it's uniform. What varies is how recently
each UPSTREAM SOURCE itself last published new data. The 'extracted' field in
release_status.yml means "the date this source's data was last updated upstream, as
best CDA can tell" -- NOT "the date CDA last pulled it." Language throughout reflects
that: "source last updated" / "Nd since source update", not "extracted" / "Nd since
extraction".

Styling note: all HTML output uses plain hardcoded colors, not theme CSS variables, so
this renders identically regardless of which mkdocs theme is active.
"""

import yaml
from datetime import date, datetime
from pathlib import Path

DATA_PATH = Path(__file__).parent / "docs" / "_data" / "release_status.yml"

FRESH_DAYS = 30
STALE_DAYS = 120


def _load_sources():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)["sources"]


def _update_status_for(src):
    release = str(src.get("release", "")).lower()
    if release in ("unassigned", "unknown", ""):
        return "unknown", "No release assigned yet"

    try:
        updated = datetime.strptime(src["extracted"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        return "unknown", "Unknown"

    age_days = (date.today() - updated).days
    if age_days <= FRESH_DAYS:
        return "fresh", "Recently updated by source"
    else:
        return "stale", f"{age_days}d since source update"


def define_env(env):
    """Required entry point for mkdocs-macros-plugin."""

    @env.macro
    def data_available_widget():
        sources = _load_sources()
        rows = []
        for src in sources:
            status_class, status_label = _update_status_for(src)
            dot_color = {"fresh": "#1a7f37", "stale": "#9a6700", "unknown": "#cf222e"}[status_class]
            rows.append(
                f'<span title="{src["name"]}: {status_label}" style="display:inline-flex;align-items:center;gap:4px;margin-right:14px;font-size:0.85rem;">'
                f'<span style="width:8px;height:8px;border-radius:50%;background:{dot_color};display:inline-block;"></span>'
                f'<strong>{src["name"]}</strong></span>'
            )
        return (
            '<div style="padding:10px 14px;border:1px solid #d0d0d0;'
            'border-radius:8px;margin:16px 0;">'
            '<div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;'
            'color:#777777;margin-bottom:6px;">Data available at CDA</div>'
            + "".join(rows)
            + ' <a href="/release_notes/data_updates/" style="font-size:0.85rem;">Full details →</a>'
            "</div>"
        )

    @env.macro
    def data_available_table():
        sources = _load_sources()
        status_colors = {
            "fresh":   {"bg": "rgba(52,211,153,0.15)",  "text": "#1a7f37", "dot": "#1a7f37"},
            "stale":   {"bg": "rgba(251,191,36,0.18)",  "text": "#9a6700", "dot": "#9a6700"},
            "unknown": {"bg": "rgba(248,113,113,0.18)", "text": "#cf222e", "dot": "#cf222e"},
        }
        header = (
            '<table style="width:100%;border-collapse:collapse;font-size:0.9rem;">'
            "<thead><tr>"
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Source</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Data release</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">API version</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Source last updated</th>'
            '<th style="text-align:left;padding:8px 12px;font-size:0.78rem;'
            'text-transform:uppercase;letter-spacing:0.04em;border-bottom:2px solid #d0d0d0;">Status</th>'
            "</tr></thead><tbody>"
        )
        rows = []
        for src in sources:
            status_class, status_label = _update_status_for(src)
            colors = status_colors[status_class]
            release_cell = (
                f'<a href="{src["link"]}" target="_blank" rel="noopener">{src["release"]}</a>'
                if src.get("link") else src["release"]
            )
            rows.append(
                '<tr style="border-bottom:1px solid #e5e5e5;">'
                f'<td style="padding:10px 12px;"><span style="display:inline-block;width:8px;height:8px;'
                f'border-radius:50%;background:{colors["dot"]};margin-right:8px;"></span><strong>{src["name"]}</strong></td>'
                f'<td style="padding:10px 12px;">{release_cell}</td>'
                f'<td style="padding:10px 12px;">{src["api"]}</td>'
                f'<td style="padding:10px 12px;">{src["extracted"]}</td>'
                f'<td style="padding:10px 12px;"><span style="display:inline-block;padding:3px 12px;'
                f'border-radius:999px;font-size:0.78rem;font-weight:700;background:{colors["bg"]};'
                f'color:{colors["text"]};">{status_label}</span></td>'
                "</tr>"
            )
        return (
            '<div style="border:1px solid #d0d0d0;border-radius:12px;'
            'padding:20px 24px;margin:16px 0;">'
            '<h3 style="margin-top:0;">📅 Data available at CDA</h3>'
            '<p style="color:#555555;font-size:0.85rem;margin-bottom:16px;">'
            "CDA pulls a fresh copy of every source at each release. These dates show how "
            "recently each <em>upstream source itself</em> last published new data — not "
            "how recently CDA last checked.</p>"
            + header + "".join(rows) + "</tbody></table></div>"
        )
```

---

## `docs/_data/release_status.yml`

```yaml
# 'extracted' field name kept as-is to avoid touching every entry, but its MEANING is
# "date this source's data was last updated upstream" -- see main.py docstring.
sources:
  - name: GDC
    release: "46.0"
    api: "8.5.0"
    extracted: "2026-09-23"
    link: "https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/"
  - name: PDC
    release: "6.3"
    api: "4.0.19"
    extracted: "2026-09-23"
    link: "https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm"
  - name: IDC
    release: "v24"
    api: "—"
    extracted: "2026-05-28"
    link: "https://learn.canceridc.dev/data/data-release-notes"
  - name: GC
    release: "30.0"
    api: "—"
    extracted: "2026-08-20"
    link: "https://dataservice.datacommons.cancer.gov/#/releases"
  - name: ICDC
    release: "2025-09-21"
    api: "4.3.0"
    extracted: "2026-05-28"
    link: "https://caninecommons.cancer.gov/#/news"
  - name: CTDC
    release: "unassigned"
    api: "—"
    extracted: "2026-09-23"
    link: "https://datacommons.cancer.gov/repository/clinical-and-translational-data-commons"
```

---

## `docs/css/cards.css`

```css
.grid-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.grid-cards > * {
    border: 1px solid #d0d0d0;
    border-radius: 8px;
    padding: 1rem 1.25rem;
    background: #fafafa;
}

.grid-cards hr {
    margin: 0.5rem 0 0.75rem 0;
    border: none;
    border-top: 1px solid #e0e0e0;
}

.grid-cards p:last-child {
    margin-bottom: 0;
}
```

---

## `docs/index.md`

```markdown
---
title:  Re-Search made simple
---

<div class="center" markdown>

# Cancer Data Aggregator

<p style="font-size: 1.1rem; max-width: 640px; margin: 0 auto 8px;">Think of CDA as one really, really enormous spreadsheet spanning six cancer data centers — GDC, PDC, IDC, GC, ICDC, and CTDC. Search by harmonized, common-language terms and get results back in a standard dataframe (or TSV) you can open in Excel, feed into a pipeline, or send to your favorite cloud resource.</p>

<p style="max-width: 640px; margin: 0 auto 24px;">No matter your coding comfort — from zero code to full API access — there's a way in.</p>

<a href="getting_started/" title="Getting started" class="md-button md-button--primary">Get started →</a>

</div>

{{ data_available_table() }}
```

---

## `docs/getting_started/index.md`

```markdown
---
title: Getting Started
---

<div class="center" markdown>
<p>CDA is one really, really enormous spreadsheet spanning six data centers — GDC, PDC, IDC, GC, ICDC, and CTDC. Every path below gets you to the same data; the difference is how much setup and flexibility you want.</p>
</div>

--8<-- "_snippets/main_cards.md"

## Not sure which one fits?

- Just want to look around? → **No installation, no code** (top-left card above)
- Know roughly what you're searching for, comfortable with a notebook? → **Low code, no install**
- Running the same kinds of searches repeatedly, or need full flexibility? → **Power users**
- Already have a CDA result set and want to do heavier analysis? → **Code in the Cloud**
- Building something that talks to CDA programmatically? → **Developer / API Reference**

Want more detail first? See the full [install locally](install.md) guide or the full [no-installation / Colab](no-install.md) guide.

## What's new

- [Data Release Notes](../release_notes/data_updates.md)
- [Code Release Notes](../release_notes/cdapython.md)
```

---

## `docs/getting_started/install.md`

```markdown
---
title:  Local installation docs
---

# Installation Guide

!!! requirements

    - A command-line environment that supports Python and pip
    - python version >= 3.9 [(Install)](https://www.python.org/downloads/)

1. In your terminal type:

  ```bash
  pip install --upgrade cdapython
  ```

## Terminal/Command line

cdapython is a python package, to run on the command line, start python

```bash
python3
```
and import the cdapython modules:

```python
from cdapython import *
```

## Interactive notebook

cdapython comes with jupyter notebook installed, and our documentation is all available as jupyter notebooks. To start a notebook server, go to your command line/terminal and type:

```bash
jupyter notebook
```
This will launch an interactive notebook in your browser. Be sure to import the cdapython modules in your first notebook block:

```python
from cdapython import *
```
```

---

## `docs/getting_started/no-install.md`

```markdown
---
title:  No installation docs
---

## Launch Google Colab

**Try cdapython in your web browser, no installation required.**

Launch a Jupyter Notebook with interactive, modifiable, example notebooks ready to run.

Click this button to get started: [Try it now](https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Tutorials/Welcome.ipynb){ .md-button .md-button--primary}

You can preview static versions of the [example notebooks here](../documentation/cdapython/vignettes/index.md).

## About Google Colaboratory

### What is it?

[Google Colaboratory](https://colab.research.google.com/?utm_source=scs-index) provides small, free, on-demand computing
resources accessible through your web browser. Our colaboratory space is pre-configured to
provide all the packages you need to run cdapython, as well as example ipython
notebooks. Each time you click the button, it will start a fresh machine with no
memory of your previous changes.

### What can I do in it?

If you are familiar with python, you can freely edit the example notebook to run
different queries, or even create your own ipython notebook to run. You can also
upload code using the import feature in the bottom right pane. Keep in mind
that these instances are relatively small, so they will likely run out of memory
if you try to run a very large query. If you are working with cdapython regularly,
we recommend [installing it locally](./install.md).

### Leaving the notebook

The colab instance, any edits you've made to the code, and any results you create,
will be lost when you close your browser tab or internet connection. If you are
using the instance to run your own queries be sure to save out the results and code to
your google drive by using `File -> Save a copy in drive` before you leave.

### Doing more with cdapython

If you are working with cdapython regularly,
we recommend [installing it locally](./install.md). You'll
be able customize your installation and to run larger and more complex queries
than the colab instances can handle.
```

---

## `docs/_snippets/main_cards.md`

```markdown
<div class="grid-cards" markdown>

-   ⚡ __Don't code? No problem!__

    ---

    Browse through a curated dataset of all subjects that have data at multiple data centers using an intuitive filtering tool right in this website.

    <a href="/interactive/" title="interactive search" class="md-button md-button">Head to our interactive page to try it out.</a>

-   ⚡ __Low code, no install__

    ---

    Fill in the blanks in our pre-built queries to find the data you need without installing a thing.

    <p>Send your results to <a href="https://datacommons.cancer.gov/analytical-resource/broad-institute-firecloud" target="_blank">Broad Institute FireCloud ↗</a> or <a href="https://www.cancergenomicscloud.org/" target="_blank">Velsera Cancer Genomics Cloud ↗</a> for a complete cloud experience. Find the data you need, fetch all the files, and run your favorite bioinformatics pipeline *all without ever leaving your web browser.*</p>

    <a href="https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Tutorials/Welcome.ipynb" title="Try it now" class="md-button md-button">Launch CDA in the cloud</a>

-   🐍 __Power users__

    ---

    Install `cdapython` with `pip` and get up and running in no time

    ```bash
    pip install cdapython
    python3
    ```
    ```python
    from cdapython import *
    ```

-   🐍 __Code in the Cloud__

    ---

    Bring lists of files or subjects found with CDA to the <a href="https://isb-cgc.org/" target="_blank">ISB Cancer Gateway in the Cloud (ISB-CGC) ↗</a> to instantly access both associated derived data and raw files, for use in cloud processing pipelines -- either in your own preferred environment or using ISB-CGC's free Google Cloud Platform credits program.

    <a href="https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Tutorials/010_isbcgc.ipynb" title="isbcgcusecase" class="md-button md-button">Test it out on Google Colab</a>

-   🔌 __Developers__

    ---

    Are you building a metadata microservice? Connecting even more databases? Hosting a computational resource? Want the full REST API spec?

    <p>Whatever your use case, CDA can help.</p>

    [→ __API documentation__](/documentation/developers/)

</div>
```

---

## `docs/interactive.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "tags": ["hide_code"]
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "opt.serverSide=False\n",
    "opt.classes=\"display\"\n",
    "opt.buttons=[\"pageLength\",\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.layout={\"bottomStart\": \"buttons\"}\n",
    "opt.maxBytes=0\n",
    "opt.warn_on_undocumented_option=False\n",
    "from cdapython import *"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Interactive Search"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "subject = get_subject_data(add_columns=[\"diagnosis\", \"sex\", \"stage\", \"anatomic_site\", \"treatment_type\"])\n",
    "subject.set_index(\"subject_id\", inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Welcome to our interactive search page\n",
    "\n",
    "Cancer Data Aggregator is an effort to unite data of multiple types by indexing, harmonizing and aggregating data from multiple data centers. CDA makes these varied datasets uniformly searchable by a common set of terms, regardless of modeling differences at the original source.\n",
    "\n",
    "__This page contains a full listing of all subjects in CDA__ and many of their categorical values, to allow you to search interactively on this website. For detailed instructions on using this tool, [click here](#interactive-search-instructions).\n",
    "\n",
    "To interact with the entire CDA dataset including numerical subject values, more categorical values, and data about the types of files associated with all of these subjects, you will need to use [cdapython directly](getting_started/no-install.md)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "show(\n",
    "    subject,\n",
    "    layout={\"top1\": \"searchBuilder\"},\n",
    "    searchBuilder={\n",
    "        \"preDefined\": {\n",
    "            \"criteria\": [\n",
    "                {\"data\": \"diagnosis\", \"condition\": \"contains\", \"value\": [\"adenocarcinoma\"]}\n",
    "            ]\n",
    "        }\n",
    "    },\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data sources\n",
    "\n",
    "Data is currently curated from:\n",
    "\n",
    "- <a href=\"https://datacommons.cancer.gov/repository/genomic-data-commons\" target=\"_blank\">Genomics Data Commons<img src=\"images/link-external-16.svg\" width=10></a>\n",
    "- <a href=\"https://datacommons.cancer.gov/repository/proteomic-data-commons\" target=\"_blank\">Proteomic Data Commons<img src=\"images/link-external-16.svg\" width=10></a>\n",
    "- <a href=\"https://datacommons.cancer.gov/repository/imaging-data-commons\" target=\"_blank\">Imaging Data Commons<img src=\"images/link-external-16.svg\" width=10></a>\n",
    "- <a href=\"https://datacommons.cancer.gov/repository/general-commons\" target=\"_blank\">General Commons (formerly Cancer Data Services)<img src=\"images/link-external-16.svg\" width=10></a>\n",
    "- <a href=\"https://datacommons.cancer.gov/repository/integrated-canine-data-commons\" target=\"_blank\">Integrated Canine Data Commons<img src=\"images/link-external-16.svg\" width=10></a>\n",
    "\n",
    "## Need more data to search?\n",
    "\n",
    "Our database contains much more data than is available on this page. To search everything with minimal setup try our low-code, no-install [notebooks](getting_started/no-install.md) or [contact us](helpdesk/) for individualized help.\n",
    "\n",
    "## Is this the final product?\n",
    "\n",
    "No. CDA is actively working to provide in-browser search across our entire database, and we hope to share it with you soon. This is just a teaser :)\n",
    "\n",
    "## Questions and Comments\n",
    "\n",
    "If you have questions, comments or suggestions about our data, interface, or anything else, please email us at cancerdataaggregator `@` gmail.com"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Interactive search instructions\n",
    "\n",
    "The page loads with a simple search already filled in: the table below is filtered to subjects whose `diagnosis` contains the word \"adenocarcinoma.\"\n",
    "\n",
    "### Quick start\n",
    "\n",
    "You can change this filter to anything you like, or clear it and build your own. The table automatically filters to whatever search settings you choose — you don't need to press enter or \"start\" the search.\n",
    "\n",
    "### Saving your results\n",
    "\n",
    "Search settings reset whenever you reload the page, so save anything you want to keep. At the bottom of the table are three buttons — `copy`, `CSV`, and `Excel` — for exporting the current results.\n",
    "\n",
    "### Search Builder functions\n",
    "\n",
    "- **Clear All** — removes all current search conditions (does not reset the free-text search box).\n",
    "- **Add Condition** — adds a condition, filled in left to right:\n",
    "  - **Data** — the column to search on.\n",
    "  - **Condition** — how to filter that column.\n",
    "  - **Value** — the value to filter on (skipped for `Empty`/`Not Empty`).\n",
    "- **And / Or** — click the connector box to toggle between `And` and `Or` for the conditions nested inside it; the small `x` deletes the box and everything nested inside it.\n",
    "- **Nesting (`>`)** — lets you build arbitrarily complex And/Or combinations. For example, to find women with adenocarcinoma of the breast *or* lymph nodes: add a `primary_diagnosis_site = breast` condition, then click `>` next to it to nest a second condition for lymph node, then toggle that nested group's connector from `And` to `Or`.\n",
    "- **x** — deletes the corresponding condition line."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `docs/helpdesk/index.md`

```markdown
---
title: Getting Help
---
<div class="grid-cards" markdown>
-   ❓ [__Ask a question__ ↗](https://github.com/CancerDataAggregator/CDA-HelpDesk/discussions/categories/q-a){:target="_blank"}
---
    Search our discussions for an answer to your question, or ask a new one
-   🐛 [__File a bug report__ ↗](https://github.com/CancerDataAggregator/CDA-HelpDesk/discussions/categories/bug-report){:target="_blank"}
---
    Something broken? Let us know!
-   🔀 [__Make a feature request__ ↗](https://github.com/CancerDataAggregator/CDA-HelpDesk/discussions/categories/feature-requests){:target="_blank"}
---
    Help us help you. What can we do to make CDA better?
-   📣 [__Share how you've used CDA__ ↗](https://github.com/CancerDataAggregator/CDA-HelpDesk/discussions/categories/show-and-tell){:target="_blank"}
---
    Tell us how you've used CDA, or even submit some code to share with the world. We'd love to hear from you!
-   🔔 [__Check out our announcements__ ↗](https://github.com/CancerDataAggregator/CDA-HelpDesk/discussions/categories/announcements){:target="_blank"}
---
    Sometimes we do cool stuff too. Come see what we're doing, and what we're planning.
-   🗄️ [__Need a CDA of your own?__](mailto:cancerdataaggregator@gmail.com)
---
    Do you dream of having a CDA database instance of your very own? Or CDA but bigger somehow? We can make those dreams come true. Let's chat!
-   📧 [__Something else?__](mailto:cancerdataaggregator@gmail.com)
---
    Need something we didn't list yet? We still want to hear from you! email us at cancerdataaggregator `@` gmail
</div>
```

---

## `docs/about_us/index.md`

> **Open item — not resolved in this pass:** this page references 12 team/alumni photo files that aren't included anywhere in the source material. See the open items list below.

```markdown
---
title:  About Us
---

# About us

The Cancer Data Aggregator is a service of the National Cancer Institutes' (NCI) Cancer Research Data Commons. We pull metadata for thousands of studies hosted at multiple data repositories across NCI, and make it available for search from a single tool so researchers can more easily find and reuse existing cancer research data. In between pulling and publishing, we thoroughly clean, harmonize, and cross-reference the metadata so you can easily do things like find subjects that have participated in multiple studies, discover data from a disease that was originally described in different ways at each repository, and compile all the data from your favorite program such as CPTAC - no matter where it ended up. 

To learn more about how we make metadata ready for search, head to our [about our data](./ourdata.md) page.

To learn more about how to access and work with data you find using CDA, visit the CRDC [Cloud Resources](https://datacommons.cancer.gov/analyze/analytical-tools) page


## About the Cancer Research Data Commons

The [Cancer Research Data Commons ↗](https://datacommons.cancer.gov/){:target="_blank"} (CRDC) is a cloud-based data science infrastructure that provides secure access to a large, comprehensive, and expanding collection of cancer research data. Users can explore and use analytical and visualization tools for data analysis in the cloud.

![CRDC image](../images/CRDCoverviewDEC2023small.jpeg)


## Our team

<div class="grid-cards" markdown>
-   <figure>
    <img src="../images/arthur.png" width="100" height="100"
         alt="Arthur Brady">
    <figcaption>Arthur Brady<p>Data wrangling & Developer</figcaption>
</figure>

-   <figure>
    <img src="../images/amanda.png" width="100" height="100"
         alt="Amanda Charbonneau">
    <figcaption>Amanda Charbonneau <p>Testing & Directing</figcaption>
</figure>
-   <figure>
    <img src="../images/tanner.png" width="100" height="100"
         alt="Tanner Coon">
    <figcaption>Tanner Coon <p>Developer</figcaption>
</figure>
-   <figure>
    <img src="../images/david.JPG" width="100" height="100"
         alt="David Pot">
    <figcaption>David Pot<p>Principal Investigator</figcaption>
</figure>
</div>

## Alumni

<div class="grid-cards" markdown>
-   <figure>
    <img src="../images/BingxingHuo-bio.png" width="100" height="100"
         alt="Bing-Xing Huo">
    <figcaption>Bing-Xing Huo<p>Principal Investigator - Broad</figcaption>
</figure>
-   <figure>
    <img src="../images/finny.jpg" width="100" height="100"
         alt="Finny Thomas">
    <figcaption>Finny Thomas <p>Developer</figcaption>
</figure>
-   <figure>
    <img src="../images/surya.jpeg" width="100" height="100"
         alt="Surya Saha">
    <figcaption>Surya Saha <p>Project Manager - Velsera</figcaption>
</figure>
-   <figure>
    <img src="../images/jack.png" width="100" height="100"
         alt="Jack DiGiovanna">
    <figcaption>Jack DiGiovanna <p>Principal Investigator - Velsera</figcaption>
</figure>
-   <figure>
    <img src="../images/rachel.png" width="100" height="100"
         alt="Rachel Kutner">
    <figcaption>Rachel Kutner <p>Developer & Project Management</figcaption>
</figure>
-   <figure>
    <img src="../images/kat.jpg" width="100" height="100"
         alt="Kat Thayer">
    <figcaption>Kat Thayer <p>Project Management</figcaption>
</figure>
-   <figure>
    <img src="../images/alex.jpeg" width="100" height="100"
         alt="Alex Baumann">
    <figcaption>Alex Baumann <p>Principal Investigator - Broad</figcaption>
</figure>
</div>

## Funding

This project has been funded in whole or in part with Federal funds from the National Cancer Institute, National Institutes of Health, Task Order No. 17X053 under Contract No. HHSN261200800001E
```

---

## `docs/about_us/ourdata.md`

> **Open item — not resolved in this pass:** references 7 logo images; only CTDC's is a confirmed real saved asset. See open items below.

```markdown
---
title:  Our data sources
---

- ![](../images/genomic-data-commons-gdc_0.png)[Genomics Data Commons ↗](https://datacommons.cancer.gov/repository/genomic-data-commons){:target="_blank"}

The Genomic Data Commons (GDC) is a cancer knowledge network that supports hosting, standardization, and analysis of genomic, clinical, and biospecimen data from cancer research programs. The GDC harmonizes raw sequencing data, identifies and applies state-of-the-art bioinformatics methods for generating mutation calls, structural variants and other high-level data, and provides scalable downloads and web-based analysis tools. Because of the personal nature of genomic data, some genomic data in the GDC may be controlled access, requiring eRA Commons authentication and dbGaP authorization to access the data. 


- ![](../images/proteomic-data-commons-pdc_0.png)[Proteomic Data Commons ↗](https://datacommons.cancer.gov/repository/proteomic-data-commons){:target="_blank"}

The Proteomic Data Commons (PDC) was developed to advance understanding of how proteins help to shape the risk, diagnosis, development, progression, and treatment of cancer. In-depth analysis of proteomic data allows the study of both how and why cancer develops and informs ways of tailoring treatment for individual patients using precision medicine. All proteomic data in the PDC are open access and, with appropriate attribution, can be included in publications.


- ![](../images/imaging-data-commons-idc_0.png)[Imaging Data Commons ↗](https://datacommons.cancer.gov/repository/imaging-data-commons){:target="_blank"}

NCI Imaging Data Commons (IDC) is a cloud-based repository of publicly available cancer imaging data co-located with the analysis and exploration tools and resources. IDC is a node within the broader NCI Cancer Research Data Commons (CRDC) infrastructure that provides secure access to a large, comprehensive, and expanding collection of cancer research data.

All data hosted by IDC is available publicly. The current content of IDC is populated using the radiology collections from The Cancer Imaging Archive (TCIA), as well as data collected by other major NCI initiatives, such as TCGA, CPTAC, NLST and HTAN. IDC does not perform de-identification of images but accepts data de-identified by TCIA or other Data Coordinating Centers that are approved by NCI Security.


- ![](../images/general-commons_0.png)[General Commons ↗](https://datacommons.cancer.gov/repository/general-commons){:target="_blank"}

The GC provides data storage and sharing capabilities for NCI-funded studies that fall under the following categories:
•    Studies with data that do not match an existing CRDC data commons 
•    Studies with data that do not fit current data type criteria and/or the minimum metadata standards for a CRDC data commons. 

GC currently hosts a variety of data types from NCI projects such as the Human Tumor Atlas Network (HTAN), Division of Cancer Control and Population Sciences (DCCPS), and Childhood Cancer Data Initiative (CCDI) as well as data from independent research projects. The GC is home to both open and controlled access data.

- ![](../images/integrated-canine-data-commons-icdc_0.png)[Integrated Canine Data Commons ↗](https://caninecommons.cancer.gov/#/explore){:target="_blank"}

The Integrated Canine Data Commons (ICDC) is a cloud-based repository of spontaneously-arising canine cancer data. ICDC was established to further research on human cancers by enabling comparative analysis with canine cancer. The data in the ICDC is sourced from multiple different programs and projects; all focused on canine subjects. The data is harmonized into an integrated data model and then made available to the research community. 

- ![](../images/clinical-and-translational-data-commons-ctdc.png)[Clinical and Translational Data Commons ↗](https://datacommons.cancer.gov/repository/clinical-and-translational-data-commons){:target="_blank"}

The Clinical and Translational Data Commons (CTDC) accelerates scientific discoveries that make an impact on cancer outcomes to help people live longer, healthier lives, by reducing barriers to data access and use from NCI-funded clinical and translational studies. CTDC features include a Data Exploration dashboard to quickly visualize and refine searches of CTDC data, multiple data types including clinical and molecular/sequencing data, and data harmonization across studies through alignment with NCI's Cancer Data Standards Registry and Repository (caDSR) Common Data Elements (CDEs). CTDC's inaugural dataset comes from the Cancer Moonshot Biobank (CMB), which collects longitudinal clinical data and biospecimens shared by participants throughout their standard-of-care treatment at participating US medical institutions.

- ![](../images/isb-cancer-gateway-in-the-cloud.png)[ISB Cancer Gateway in the Cloud ↗](https://www.isb-cgc.org/){:target="_blank"}

The ISB Cancer Gateway in the Cloud (ISB-CGC) is one of three National Cancer Institute (NCI) Cloud Resources tasked with enabling researchers to combine cancer data and cloud computation. ISB-CGC's relationship with CDA runs in both directions. **Upstream**, ISB-CGC is the source of all mutation data in CDA: GDC's own mutation files are released as per-individual VCFs, and ISB-CGC aggregates these into a single harmonized, queryable mutation dataset hosted in Google BigQuery, which CDA then incorporates. **Downstream**, ISB-CGC is also a consumer of CDA: they take CDA's non-mutation phenotypic data and incorporate it into their own search tools, alongside data from other sources such as HTAN, TCGA, CPTAC, and TARGET.
```

---

## `docs/release_notes/cdapython.md`

```markdown
---
title:  cdapython releases
status: new
---

# Public releases

## Available April 7, 2026

Global keyword search is now available on 'summarize_subjects', 'summarize_files', 'get_subject_data',
and 'get_file_data'. See `documentation/cdapython/vignettes/01_global_search.ipynb`

## Available August 18, 2025

New API: Streamlined, object-based query API that supports complex filter sets
Improved cdapython with easier to read, subject and file based results tables, more intuitive query language, and support for joining data across multiple results

`cdapython` is now available on PyPI -- install with `pip install cdapython` instead of installing from GitHub.

### Known Issues

- `upstream_source` results are incorrectly linking some records. We recommend not using this field until the fix is implemented in our next code release


## Available July 16, 2024

cdapython version 2024.1.4
API version 2024.1.2

### Highlights:

- Hotfix to resolve issues when querying against BIGINT typed columns. 


We discovered a problem when attempting to apply filters against BIGINT typed columns (ex. file byte_size). This was resolved and all queries not noted in the previous known issues should be runnable. 

### Known Issues

- The generated query string returned from the API will always show the filter value in quotes even if it is not a quoted value (ex. " byte_size > 20 " will be presented as " byte_size < '20' "). This is just an issue presenting the values in the query as a string and not what is actually queried to the database.


## Available July 11, 2024

cdapython version 2024.1.4
API version 2024.1.1

### Highlights:

- Hotfix to resolve issues when using the summary_counts() function with the mutation table


We discovered a problem when attempting to use the summary_counts() function with the mutation table. Attempting this would always result in an error. This was caused by an oversight in the code when we made the change from somatic_mutation to mutation in the previous release. The issue has been resolved.


## Available June 26, 2024

cdapython version 2024.1.3
API version 2024.1.1

### Highlights:

- Fixed issue where somatic_mutation query was returning incorrect results
- Fixed some performance issues with somatic_mutation queries
- Renamed somatic_mutation table to mutation


We discovered incorrect results coming from queries involving the somatic_mutation table. This was caused by the table not having its own id/primary key, instead relying on the subject_alias. This was a deviation from how every other data table was structured, therefore certain queries would fall apart. Changes were made to the data model to structure the newly named "mutation" table to mirror every other table. Due to this change, we needed to simply remove certain code from the API that was added in an attempt handle quirks with the original somatic_mutation table as well as update a few things within the cdapython client.


## Available May 29, 2024

- Summary value data has been reformatted for easier reading
  
- null data has been disambiguated
  
- Users can now submit a tab separated file (tsv) of identifiers or any other set of values to search using the `match_from_file` parameter in fetch_rows. See [this vignette](../documentation/cdapython/vignettes/03_match_from_file.ipynb) for an example.

### Known issues

- `match_from_file` cannot handle very large lists of values (greater than ~10,000)

- the cdapython update is not currently available in pypi, please install using `pip install git+https://github.com/CancerDataAggregator/cdapython.git`. It should be available in pypi soon.

- Some complex joins will return more data than `summary_counts` or the `count_only` parameter report. This is due to miscounting of the join structure.

- Not all errors are handled gracefully, as we haven't found them all yet. If you experience one, please let us know.

- help text for individual functions (and an error message, if you try to use an unavailable value) is currently the only way to obtain a valid list of data_source labels (DC names) for queries. Current list is GDC, PDC, IDC, and CDS.

- column_values endpoint won't process more than one system (i.e. data_source/DC) filter per query.

- the mutations endpoint gives wrong counts (but correct results)
ex.: filtering by hugo_symbol='DOK1' reports 85 results, when the correct number of matching records (and the number of records that is actually returned) is 95.

-Certain queries can pass back large amounts of data which can timeout or fill memory restrictions in colab, mybinder, and other low-memory systems.


## Available April 5, 2024

cdapython has had a complete rewrite to simplify the code. 

### Known Issues:

- the cdapython update is not currently available in pypi, please install using `pip install git+https://github.com/CancerDataAggregator/cdapython.git`. It should be available in pypi soon.

- Impossible joins need better error handling, e.g. `fetch_rows( table='subject', link_to_table='subject' )`.

- Some complex joins will return more data than `summary_counts` or the `count_only` parameter report. This is due to miscounting of the join structure.

- Not all errors are handled gracefully, as we haven't found them all yet. If you experience one, please let us know.

- Developers using the API may experience query problems when building calls that are technically correctly formatted, but do not fit our style guide. ex.: file_associated_project and subject_associated_project currently only work as filters when applied from their home-entity endpoint. ex.: using SELECTVALUES at the mutations endpoint without including the case_barcode column will break. These will be resolved in our upcoming API update. Until then, please contact us directly for assistance.

- help text for individual functions (and an error message, if you try to use an unavailable value) is currently the only way to obtain a valid list of data_source labels (DC names) for queries. Current list is GDC, PDC, IDC, and CDS.

- column_values endpoint won't process more than one system (i.e. data_source/DC) filter per query.

- the mutations endpoint gives wrong counts (but correct results)
ex.: filtering by hugo_symbol='DOK1' reports 85 results, when the correct number of matching records (and the number of records that is actually returned) is 95.

- the mutations endpoint exposes internal record alias info in API results (attaching example)
front end presently strips them out.

- Using the API directly (not through cdapython), it is possible to max out the Java heap space with certain queries.

-Certain queries can pass back large amounts of data which can timeout or fill memory restrictions in colab, readthedocs, and low-memory systems.


# beta versions

## Available August 22, 2023.

### Updates

- get_all has been expanded to work on unique_terms

### Bug fixes

- A visual bug where get_all was displaying multiple progress bars has been fixed
- A bug in the code base model relationships has been fixed that was causing some queries to fail, or to not return all related results.
- Improved linking between mutation table and everything else

### Known bugs and issues - these will be fixed in an upcoming release

- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.


## Available May 4, 2023.

### Updates

- Data extraction process completely rewritten with improved mappings
- Parsing language completely rewritten to increase query speed and flexibility
- `get_all` function replaces `auto_paginator`
- New `.offset()` operator
- New `.limit()` operator 
- Dropped support for python 3.7

### Bug fixes

- 'treatment_anatomic_site', 'treatment_type', 'method_of_diagnosis' and others are now properly filled

### Known bugs and issues - these will be fixed in an upcoming release

- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- mutation endpoint is not harmonized to other endpoints
- progress bars are duplicated



## Available December 21, 2022.

### Updates

- cdapython can now take subject/patient identifier lists from txt, csv, and tsv files as input for search
- The unique_terms function now returns a count of null values along with the term counts

### Bug fixes
- Fixed error where / character was causing some urls to break
- Fixed error where some columns could be counted, but not enumerated

### Known bugs and issues - these will be fixed in an upcoming release

- 'treatment_anatomic_site', 'treatment_type', and 'method_of_diagnosis' are missing data
- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- mutation endpoint is not harmonized to other endpoints



## Available November 3, 2022.

### Updates

- users can now search for subjects that have data from multiple data centers using the `FROM` function
- users can search within dataframes
- dataframe results can be ordered by any column
- `columns` now has information about what endpoint each column lives in, as well as what type of data it is (number, word, etc) and whether it's a required field

### Known bugs and issues - these will be fixed in an upcoming release

- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.
- mutation endpoint is not harmonized to other endpoints

## Available September 2022.

 We recommend updating to take advantage of improvements to our query language

The beta 3.1 release of CDA now includes search for a gene and mutation information from TCGA


### Updates

- New `mutation` endpoint allows search for gene and mutation information by HUGO gene name, subject, specimen and file
- Searches no longer require full path names for columns, e.g. 'ResearchSubject.Diagnosis.Treatment.treatment_anatomic_site' is now 'treatment_anatomic_site'
- 'id' columns have been made unique, e.g. ''ResearchSubject.Diagnosis.Treatment.id' is now 'treatment_id'
- New `join_as_str` function allows users to use results from one Q search as input to another
- `filter` function in `run` renamed to `include` and now includes flag to allow users to dynamically rename columns in search results
- New `auto_paginator` function has been added that does not require the user to loop through results
- `paginator` and `auto_paginator` now display a progress bar
-  `limit` flag in paginators renamed to `page_size`
- Query return details has been simplified
- `to_list` can now do both fuzzy and exact matching
- `unique_terms` can now optionally show counts of term usage
- `columns` can now display descriptions
- `Q` can now accept arbitrarily complex math as part of a query, e.g.: 
 
         Q('days_to_birth >= 50 * -365 AND days_to_birth <= 20 + -365').specimen.run().to_dataframe()
- Code optimization to improve search speed and performance


### Bug fixes

- Files associated with cancer or normal tissue specimens are now properly attributed as cancer or normal
- `filters` option in `to_list` function is now case-insensitive
- Various error message and handling improvements


### Known bugs and issues - these will be fixed in an upcoming release

- paginator and auto_paginator progress bars do not always reach 100%, when all data is retrieved.
- adding columns to a results table from another endpoint causes duplication. If the column has much more or much less data than the results table, the duplication may cause inappropriate joins.


---

# Early alphas

## Available as of 7/11/22

The beta 3.0 release of CDA searches across data from the Genomics Data Commons (GDC), the Proteomics Data Commons (PDC), and the Imaging Data Commons (IDC) to aggregate and return data to users via a single application programming interface (API).


## Updates

* Added support for the following SQL operators: IN, LIKE, NOT IN, IS NOT, IS
* Q now comes with a better query parser that allows for writing full AND/OR logic into a single Q object
    - Example: `Q("ResearchSubject.primary_diagnosis_site = 'kidney' AND ResearchSubject.Diagnosis.stage = 'Stage II')`
* Methods for data retrieval were split into multiple entities as opposed to returning one large nested structure
    - To support this, method chaining was added to allow for querying each of the specific entities (e.g. `Q('[query here]').subject.run()`)
    - Entities supported: `subject`, `researchsubject`, `specimen`, `diagnosis`, `treatment`, `file`
    - Along with this also comes files and counts for each entity (e.g. `subject.file`, `subject.count`)
* Counts functionality added, giving total counts for entities and per DCC depending on usage
    - `Q("ResearchSubject.primary_diagnosis_site = 'kidney'").count.run()` would return total counts for each entity and DCC
    - `Q("ResearchSubject.primary_diagnosis_site = 'kidney'").subject.count.run()` would give a more generalized breakdown of specific fields in subject (e.g. number of records per distinct value for `sex`, `ethnicity`, `cause_of_death` or `identifier.system`)
    - `Q("ResearchSubject.primary_diagnosis_site = 'kidney'").subject.file.count.run()` would give a breakdown of distinct fields for subject files such as `data_type` or `file_format`
* Filter flag added to Q's run method which allows horizontal filtering of results
* Verbose flag added to Q's run method to hide/show Q actions when running a query
* Queries on text fields are now case-insensitive
* Added to_dataframe to Q's Result object that converts the JSON structure to a pandas dataframe
* Added paginator to Q's Result object that allows for pagination through result pages. This also has a flag for paginating as a dataframe.
* Added table formatting to count results objects for easier reading

## Bug fixes

* Fixed issue where queries on list columns that were not lists of json objects (i.e. subject_associated_project) would fail
* Fixed issue where integer fields were being returned as strings


## Known bugs and issues - these will be fixed in an upcoming release

* `unique_terms` are not sorted when they return
* tumor stages are not harmonized, there are redundant terms (complicates query)
* Days_to_birth should be reformatted (currently negative) or have an example query
* Docker jupyter notebook does not work if a notebook is already open in port 8888
* Searches on the subject endpoint incorrectly count files. Please use the file counts for the same query from the files endpoint
* Some PDC files are incorrectly labeled at the specimen level, for e.g. a file may be inappropriately labeled as both cancer and normal.

## 2.X

Version 3.0 is a full rewrite of our code and older versions of cdapython are no longer maintained or supported.
If you'd like to see how the project has evolved, you can still access the their documentation here:

- [2.0](https://github.com/CancerDataAggregator/CDA-HelpDesk/blob/2.0/docs/source/ReleaseNotes.md)
- [2.1](https://github.com/CancerDataAggregator/CDA-HelpDesk/blob/2.1/docs/source/ReleaseNotes.md)

<!-- Footnotes themselves at the bottom. -->
```

---

## `docs/release_notes/data_updates.md`

```markdown
---
title:  data releases
status: new
---

# Data Release Notes

{{ data_available_table() }}

# Public releases

## Available June 30, 2026

<p>CDA June 2026 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">45.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">8.4.4</a>&nbsp;(extracted 2026-05-22)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">6.1</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">4.0.14</a>&nbsp;(extracted 2026-06-17)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v24</a>&nbsp;(extracted 2026-05-28)</li>
    <li>GC data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">27.0</a>&nbsp;(from most recent dump file provided to us by GC -- received 2026-05-14)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2026-04-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.3.0</a>&nbsp;(extracted 2026-05-28)</li>
</ul>

## Available April 7, 2026

<p>CDA March 2026 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">45.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.10.1.1</a>&nbsp;(extracted 2026-03-02)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">5.3</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">4.0.8</a>&nbsp;(extracted 2026-03-02)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v23</a>&nbsp;(extracted 2025-11-26)</li>
    <li>GC data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">23.0</a>&nbsp;(from most recent dump file provided to us by GC -- received 2026-02-20)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2025-09-01</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.2.0</a>&nbsp;(extracted 2026-03-03)</li>
</ul>


## Available December 16, 2025
<p>CDA December 2025 release notes:</p>

<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">45.0-</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.10.1</a>&nbsp;(extracted 2025-12-05)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">5.1.1</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">4.0.4</a>&nbsp;(extracted 2025-12-08)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v23</a>&nbsp;(extracted 2025-11-26)</li>
    <li>GC data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">21.0</a>&nbsp;(from most recent dump file provided to us by GC -- received 2025-10-20)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.2.0.475</a>&nbsp;(extracted 2025-12-08)</li>
</ul>

## Available September 12, 2025

<p>CDA September 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">43.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.10.1</a>&nbsp;(extracted 2025-08-25)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.13</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.27</a>&nbsp;(extracted 2025-08-25)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v21</a>&nbsp;(extracted 2025-07-09)</li>
    <li>GC data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">19.0</a>&nbsp;(from most recent dump file provided to us by GC -- received 2025-08-25)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.2.0.475</a>&nbsp;(extracted 2025-08-25)</li>
</ul>


## Available August 18, 2025

<p>CDA August 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">43.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.10</a>&nbsp;(extracted 2025-07-09)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.12</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.27</a>&nbsp;(extracted 2025-07-08)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v21</a>&nbsp;(extracted 2025-07-09)</li>
    <li>CDS data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">17.0</a>&nbsp;(from most recent dump file provided to us by CDS -- received 2025-06-12)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.1.0.361</a>&nbsp;(extracted 2025-07-09)</li>
</ul>


## Available June 24, 2025

<p>CDA June 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">43</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.9.1</a>&nbsp;(extracted 2025-06-19)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.11</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.26</a>&nbsp;(extracted 2025-06-19)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v21</a>&nbsp;(extracted 2025-05-20)</li>
    <li>CDS data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">17.0</a>&nbsp;(from most recent dump file provided to us by CDS -- received 2025-06-12)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.1.0.361</a>&nbsp;(extracted 2025-06-19)</li>
</ul>

## Available May 29, 2025

<p>CDA May 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">43.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.8.5</a>&nbsp;(extracted 2025-05-20)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.10</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.23</a>&nbsp;(extracted 2025-05-20)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v21</a>&nbsp;(extracted 2025-05-20)</li>
    <li>CDS data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">17.0</a>&nbsp;(from most recent dump file provided to us by CDS -- received 2025-05-14)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.1.0.361</a>&nbsp;(extracted 2025-05-20)</li>
</ul>

## Available April 25, 2025

<p>CDA April 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">42.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.8.5</a>&nbsp;(extracted 2025-04-22)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.9</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.22</a>&nbsp;(extracted 2025-04-22)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v20</a>&nbsp;(extracted 2025-01-24)</li>
    <li>CDS data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">16.2</a>&nbsp;(from most recent dump file provided to us by CDS -- exported 2025-03-31)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.1.0</a>&nbsp;(extracted 2025-04-23)</li>
</ul>

## Available March 26, 2025

<p>CDA March 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">42.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.7.0</a>&nbsp;(extracted 2025-03-12)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.6</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.19</a>&nbsp;(extracted 2025-03-19)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v20</a>&nbsp;(extracted 2025-01-24)</li>
    <li>CDS data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">16.0</a>&nbsp;(from most recent dump file provided to us by CDS -- received 2025-03-13)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.1.0</a>&nbsp;(extracted 2025-03-19)</li>
</ul>


## Available Feb 28, 2025

<p>CDA February 2025 release notes:</p>
<ul>
    <li>GDC data release <a href="https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/">42.0</a>; API version <a href="https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes">7.7.1</a>&nbsp;(extracted 2025-02-14)</li>
    <li>PDC data release <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm">4.5</a>; API version <a href="https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm">3.0.15</a>&nbsp;(extracted 2025-02-14)</li>
    <li>IDC data release <a href="https://learn.canceridc.dev/data/data-release-notes">v20</a>&nbsp;(extracted 2025-01-24)</li>
    <li>CDS data release <a href="https://dataservice.datacommons.cancer.gov/#/releases">15.0</a>&nbsp;(from most recent dump file provided to us by CDS -- received 2024-12-18)</li>
    <li>ICDC data release <a href="https://caninecommons.cancer.gov/#/news">2023-10-16</a>; front-end version <a href="https://github.com/CBIIT/bento-icdc-frontend/releases">4.1.0</a>&nbsp;(extracted 2025-02-14)</li>
</ul>




## Available December 20, 2024
- GDC data release [41.0](https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/); API version [7.5.1](https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes) (extracted 2024-11-19)
    - GDC introduced breaking changes into its data model between our November extraction and our mid-December extraction attempt
    - 18 diagnosis fields were removed
    - [release notes](https://docs.gdc.cancer.gov/Data_Portal/Release_Notes/Data_Portal_Release_Notes/#release-231) may not give full field list; complete changelog estimate currently under way
    - GDC data in CDA's December release is thus based on the extracted instance of v41.0 from November, while we adjust our ETL
- PDC data release [4.4](https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm); API version [3.0.15](https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm) (extracted 2024-12-17)
- IDC data release [v20](https://learn.canceridc.dev/data/data-release-notes) (extracted 2024-12-17)
- CDS data release [15.0](https://dataservice.datacommons.cancer.gov/#/releases) (from most recent dump file provided to us by CDS -- received 2024-12-18)
    - CDS removed tumor_tissue_type from image, resulting in some CDA data loss (tumor/normal annotations)
    - CDA changed our file.data_category field for CDS data to use CDS's genomic_info.library_strategy field instead of earlier file.experimental_strategy_and_data_subtypes
- ICDC data release [2023-10-16](https://caninecommons.cancer.gov/#/news); front-end version [4.1.0](https://github.com/CBIIT/bento-icdc-frontend/releases) (extracted 2024-12-17)

## Available November 26, 2024

### Data extraction and release information

- GDC data release [41.0](https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/); API version [7.6.1](https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes) (extracted 2024-11-19)
- PDC data release [4.4](https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm); API version [3.0.12](https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm) (extracted 2024-11-19)
- IDC data release [v19](https://learn.canceridc.dev/data/data-release-notes) (extracted 2024-11-19)
- CDS data release [13.0](https://dataservice.datacommons.cancer.gov/#/releases); front-end version [4.3.0](https://github.com/CBIIT/bento-cds-frontend/releases) (from most recent dump file provided to us by CDS -- received 2024-10-31)
- ICDC data release [2023-10-16](https://caninecommons.cancer.gov/#/news); front-end version [4.1.0](https://github.com/CBIIT/bento-icdc-frontend/releases) (extracted 2024-11-19)


## Available October 29, 2024

### Data extraction and release information

CDA data version 2024-10

- GDC data release [41.0](https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/); API version [7.4.1](https://docs.gdc.cancer.gov/API/Release_Notes/API_Release_Notes/) (extracted 2024-10-11)
- PDC data release [4.4](https://pdc-release-notes.s3.amazonaws.com/PDC_Data_Release_Notes.htm); API version [3.0.10](https://pdc-release-notes.s3.amazonaws.com/PDC_Software_Release_Notes.htm) (extracted 2024-10-11)
- IDC data release [v19](https://learn.canceridc.dev/data/data-release-notes) (extracted 2024-10-11)
- CDS data release [13.0](https://dataservice.datacommons.cancer.gov/#/releases); front-end version [4.3.0](https://github.com/CBIIT/bento-cds-frontend/releases) (from most recent dump file provided to us by CDS -- received 2024-10-02)
- ICDC data release [2023-10-16](https://caninecommons.cancer.gov/#/news); front-end version [4.1.0](https://github.com/CBIIT/bento-icdc-frontend/releases) (extracted 2024-10-21)


## Available August 27, 2024

### Data extraction and release information

CDA data version 2024-08

- GDC data release 40.0 extracted 2024-08-18
- PDC data release 4.3 extracted 2024-08-18
- IDC data release v18 extracted 2024-08-18
- CDS data release 12.0 extracted 2024-08-14
- ICDC data release 2023-10-16 extracted 2024-08-18

## Available July 23, 2024

### Data extraction and release information

CDA data version 2024-07
Extracted July 18, 2024:

- GDC data release 40.0; API version 4.0.0 tag 7.3
- PDC data release 4.2; API version 3.0.4.1
- IDC data release v18
- CDS data release 11.0; front-end version 4.2.0.269
- ICDC data release 2023-10-16; front-end version 4.0.0.181

## Available June 26, 2024

### Data extraction and release information

CDA data version 2024-06
Extracted Fri June 21 2024:

- CDS v10.0
- GDC v40.0
- ICDC v4.0.0
- IDC v18
- PDC v4.1

## Available May 29, 2024

### Data extraction and release information

- GDC data version 40.0
- PDC data version 4.1
- IDC data version v18
- CDS data version 9.0

#### Known Issues

- DICOM was not included in the CRDC Data Element list for file_format, so no IDC files have file_format values


## Available April 5, 2024

CDA is now harmonizing terms as they are incorporated into the CRDC Data Element list. In this release we have included harmonized the values for:

- ethnicity
- file_format
- morphology
- primary_diagnosis
- race
- species
- therapeutic_agent
- source_material_type (cancer/normal)
- treatment_type
- vital_status

In future releases, we expect the harmonization to both broaden and improve. Additionally, in an upcoming release we will provide both the harmonized and original values to make finding the original data easier.

### Data extraction and release information

- GDC data version 39.0 (extraction date 3/27/2024)
- PDC data version 3.8 (extraction date 3/27/2024)
- IDC data version v17 (extraction date 3/27/2024)
- CDS data version 8.0 (extraction date 3/27/2024)

#### Known Issues

- DICOM was not included in the CRDC Data Element list for file_format, so no IDC files have file_format values
- CDS data includes clashing integer IDs. We included that data with the following changes:
    - Ensured that any integer IDs are well-wrapped by project qualifiers to make them unique within CDS
    - In instances where the same ID was attached to multiple, conflicting metadata the resulting records will be clobbered copies of one instance. A record of the affected data was kept internally at the time of this release.


# beta versions

## Available September, 12 2023.

#### Data extraction and release information


- GDC data version 38.0 (extraction date 9/1/2023)
- PDC data version 3.4 (extraction date 8/24/2023)
- IDC data version 15 (extraction date 7/19/2023)
- CDS data version 3.0 (extraction date 8/31/2023)

Data from Cancer Data Services (CDS) is now available!


## Available June 13, 2023.



#### Data extraction and release information

- GDC data version 37.0 (extraction date 6/1/2023)
- PDC data version 3.0 (extraction date 6/5/2023)
- IDC data version 14 (extraction date 6/7/2023)

IDC data now contains ethnicity data

## Available May 4, 2023.



### Datasets & Fields

#### Data extraction and release information

The current version and release dates for each of the database are:

* GDC data version 37, extraction date - 4/5/2023
* PDC data version 2.16, extraction date - 2/9/2023
* IDC data version 13, extraction date - 4/4/2023



## Available November 3, 2022.

### Datasets & Fields

#### Data extraction and release information
The current version and release dates for each of the database are:

* GDC data version - v34.0, GDC extraction date - 09/29/2022
* PDC data version - v2.10, PDC extraction date - 09/29/2022
* IDC data version - v.10.0, IDC extraction date - 09/29/2022


## Available September 2022.

### Datasets & Fields

* Versions:
    * GDC: v33.1, 06/23/2022
    * PDC: v2.7, 06/23/2022[^1]
    * IDC: v.9.0, 06/24/2022

[^1]:Information pulled from the PDC API may contain embargoed data.

---

# Early alphas

## Available as of 7/11/22.


The beta 3.0 release of CDA searches across data from the Genomics Data Commons (GDC), the Proteomics Data Commons (PDC), and the Imaging Data Commons (IDC) to aggregate and return data to users via a single application programming interface (API).

### Datasets & Fields

* All datasets updated as follows
    * GDC: v33.1, 06/23/2022
    * PDC: v2.7, 06/23/2022[^1]
    * IDC: v.9.0, 06/24/2022

[^1]:Information pulled from the PDC API may contain embargoed data.


### Metadata Changes


* Summary
    * Previous table format now called Subjects endpoint
        * Replaced all File entities with Files - a list of file ids associated with the entity that the list is located in. e.g
            * File -> Files
            * ResearchSubject.File -> ResearchSubject.Files
            * ResearchSubject.Specimen.File -> ResearchSubject.Specimen.Files
    * Files endpoint added:
        * Endpoint oriented around File information
        * Includes all information regarding the file's associated entities(Subject, ResearchSubject, and Specimen)
    * Newly available fields:
        * vital_status
        * days_to_death
        * cause_of_death
        * ResearchSubject.Diagnosis.morphology
        * ResearchSubject.Diagnosis.method_of_diagnosis
        * File.data_modality
        * File.dbgap_accession_number
        * File.imaging_modality
        * File.imaging_series
        * ResearchSubject.Diagnosis.Treatment.therapeutic_agent
        * ResearchSubject.Diagnosis.Treatment.treatment_anatomic_site
        * ResearchSubject.Diagnosis.Treatment.treatment_effect
        * ResearchSubject.Diagnosis.Treatment.treatment_end_reason
        * ResearchSubject.Diagnosis.Treatment.number_of_cycles
    * Renamed fields (old -> new):
        * ResearchSubject.associated_project -> ResearchSubject.member_of_research_project
        * ResearchSubject.primary_disease_site -> ResearchSubject.primary_diagnosis_site
        * ResearchSubject.primary_disease_type -> ResearchSubject.primary_disease_type
        * ResearchSubject.Specimen.age_at_collection -> ResearchSubject.Specimen.days_to_collection



## Known bugs and issues - these will be fixed in an upcoming release

* tumor stages are not harmonized, there are redundant terms (complicates query)
* Searches on the subject endpoint incorrectly count files. Please use the file counts for the same query from the files endpoint
* Some PDC files are incorrectly labeled at the specimen level, for e.g. a file may be inappropriately labeled as both cancer and normal.

## 2.X

Version 3.0 is a full rewrite of our code and older versions of cdapython are no longer maintained or supported.
If you'd like to see how the project has evolved, you can still access the their documentation here:

- [2.0](https://cda.readthedocs.io/en/2.0/ReleaseNotes.html)
- [2.1](https://cda.readthedocs.io/en/2.1/ReleaseNotes.html)

<!-- Footnotes themselves at the bottom. -->
```

---

## `docs/documentation/developers/index.md`

```markdown
---
title:  Developer documentation
---

<redoc spec-url='./service_openapi.yaml'></redoc>
<script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"> </script>
```

> **Open item:** the `readthedocs` theme doesn't support hiding the sidebar/TOC the way Material does, so this page shows the normal nav alongside the Redoc viewer. Not fixed in this pass — see open items below.

---

## `docs/documentation/developers/service_openapi.yaml`

Carry over unchanged from your existing repo — this is the generated REST API spec and wasn't part of the content changes. (If you don't have it handy, it's the same file referenced in the original scaffold; regenerate from the live API's `/openapi.json` if it's gone missing.)

---

## `docs/documentation/cdapython/man_pages/index.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "intro-help",
   "metadata": {},
   "source": [
    "\n",
    "To see help pages while you work type:\n",
    "\n",
    "```\n",
    "help(function)\n",
    "```\n",
    "\n",
    "example:\n",
    "\n",
    "```\n",
    "help(get_subject_data)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "import-header",
   "metadata": {},
   "source": [
    "## Import available `cdapython` functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "import-cell",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": [
     "hide_code"
    ]
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "\n",
    "opt.classes=\"display\"\n",
    "opt.buttons=[\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.maxBytes=0\n",
    "from cdapython import *"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cda-functions-header",
   "metadata": {},
   "source": [
    "## See what cdapython functions are available"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cda-functions-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "cda_functions()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "tables-header",
   "metadata": {},
   "source": [
    "## Get a list of searchable CDA tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "tables-cell",
   "metadata": {
    "editable": true,
    "scrolled": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "tables()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "columns-header",
   "metadata": {},
   "source": [
    "## Explore CDA tables' columns in detail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "columns-cell",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "columns()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "column-values-header",
   "metadata": {},
   "source": [
    "## See what values are populated in a given column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "column-values-cell",
   "metadata": {
    "editable": true,
    "scrolled": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "column_values( 'anatomic_site' )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "summarize-subjects-header",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "source": [
    "## Get subject row summary information for a column value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "summarize-subjects-cell",
   "metadata": {
    "editable": true,
    "scrolled": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "summarize_subjects( match_all = 'anatomic_site = kid*')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "summarize-files-header",
   "metadata": {},
   "source": [
    "## Get file row summary information for a column value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "summarize-files-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_files( match_all = 'anatomic_site = kid*')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "get-subject-data-header",
   "metadata": {},
   "source": [
    "## Fetch subject rows for a column value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "get-subject-data-cell",
   "metadata": {
    "editable": true,
    "scrolled": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "get_subject_data( match_all = 'subject_id = TCGA.TCGA-04-1369')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "get-file-data-header",
   "metadata": {},
   "source": [
    "## Fetch file rows for a column value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "get-file-data-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "get_file_data( match_all = 'subject_id = TCGA.TCGA-04-1369')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "intersect-subject-header",
   "metadata": {},
   "source": [
    "## Combine two subject result sets (keep only subjects in both)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "intersect-subject-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "ct_subjects = get_subject_data( match_all = ['anatomic_site = *kidney*', 'file_type = CT Image Storage'] )\n",
    "mutation_subjects = get_subject_data( match_all = ['anatomic_site = *kidney*', 'file_type = Annotated Somatic Mutation'] )\n",
    "intersect_subject_results( ct_subjects, mutation_subjects )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "expand-subject-header",
   "metadata": {},
   "source": [
    "## Flatten a nested per-subject results column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "expand-subject-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "collated = get_subject_data( match_all = ['anatomic_site = *kidney*'], add_columns = 'file.*', collate_results = True )\n",
    "expand_subject_results( collated, 'file_data' )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "intersect-file-header",
   "metadata": {},
   "source": [
    "## Combine two file result sets (keep only files in both)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "intersect-file-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "normal_files = get_file_data( match_all = ['tumor_vs_normal = normal', 'format = bam'] )\n",
    "tumor_files = get_file_data( match_all = ['tumor_vs_normal = tumor', 'format = bam'] )\n",
    "intersect_file_results( normal_files, tumor_files )"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "expand-file-header",
   "metadata": {},
   "source": [
    "## Flatten a nested per-file results column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "expand-file-cell",
   "metadata": {},
   "outputs": [],
   "source": [
    "collated_files = get_file_data( match_all = ['format = bam'], add_columns = 'subject.*', collate_results = True )\n",
    "expand_file_results( collated_files, 'subject_data' )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `docs/documentation/cdapython/man_pages/cda_functions.md`

```markdown
---
title: cda_functions()
---

# `cda_functions()`

**NAME**

`cda_functions` — list the cdapython functions available for scripting and interactive sessions

**SYNOPSIS**

```python
cda_functions()
```

**DESCRIPTION**

Returns a list of cdapython functions useful for both scripting and interactive data sessions.

**RETURNS**

A list of function names.

**SEE ALSO**

[`columns()`](columns.md), [`column_values()`](column_values.md), [`summarize_subjects()`](summarize_subjects.md), [`summarize_files()`](summarize_files.md), [`get_subject_data()`](get_subject_data.md), [`get_file_data()`](get_file_data.md)
```

---

## `docs/documentation/cdapython/man_pages/tables.md`

```markdown
---
title: tables()
---

# `tables()`

**NAME**

`tables` — list all searchable CDA data tables

**SYNOPSIS**

```python
tables()
```

**DESCRIPTION**

Get a list of all searchable CDA data tables.

**RETURNS**

`list of strings` — names of searchable CDA tables.

**SEE ALSO**

[`columns()`](columns.md), [`cda_functions()`](cda_functions.md)
```

---

## `docs/documentation/cdapython/man_pages/columns.md`

```markdown
---
title: columns()
---

# `columns()`

**NAME**

`columns` — get structured metadata describing searchable CDA columns

**SYNOPSIS**

```python
columns(*, return_data_as='', output_file='', sort_by='', **filter_arguments)
```

**DESCRIPTION**

Get structured metadata describing searchable CDA columns.

**ARGUMENTS**

- `return_data_as` (*string, optional: `'dataframe'`, `'list'`, or `'tsv'`*)
  Specify how `columns()` should return results: as a pandas DataFrame, a Python list, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which `columns()` will write tab-delimited results.

- `sort_by` (*string or list of strings, optional: any combination of `'table'`, `'column'`, `'data_type'`, and/or `'nullable'`*)
  Specify the column metadata field(s) on which to sort result data. Results are sorted first by the first named field; groups of records sharing the same value in that field are then sub-sorted by the second field, and so on.

  Appending `:desc` to a field name sorts it in reverse order; `:asc` ensures ascending order.
  Example: `sort_by=['table', 'nullable:desc', 'column:asc']`

**FILTER ARGUMENTS**

- `table` (*string or list of strings, optional*)
  Restrict returned data to columns from tables whose names match any of the given strings. A wildcard (`*`) at either or both ends of each string allows partial matches. Case is ignored.

- `column` (*string or list of strings, optional*)
  Restrict returned data to columns whose name matches any of the given strings. Wildcards and case-insensitivity apply as above.

- `data_type` (*string or list of strings, optional*)
  Restrict returned data to columns whose data type matches any of the given strings. Wildcards and case-insensitivity apply as above.

- `nullable` (*boolean, optional*)
  If `True`, restrict returned data to columns whose values are allowed to be empty; if `False`, return data only for columns requiring nonempty values.

- `description` (*string or list of strings, optional*)
  Restrict returned data to columns whose `description` field matches any of the given strings. Wildcards are applied automatically if not provided, to support straightforward keyword searching without extra punctuation. Case is ignored.

- `exclude_table` (*string or list of strings, optional*)
  Restrict returned data to columns from tables whose names do **not** match any of the given strings. Wildcards and case-insensitivity apply as above.

**RETURNS**

`pandas.DataFrame` where each row is a metadata record describing one searchable CDA column, comprised of:

| Field | Type | Description |
|---|---|---|
| `table` | string | name of the CDA table containing this column |
| `column` | string | name of this column |
| `data_type` | string | data type of this column |
| `nullable` | boolean | if `True`, this column can contain null values |
| `description` | string | prose description of this column |

— or —

`list` of column names

— or —

nothing; results are written to a user-specified TSV file

**SEE ALSO**

[`column_values()`](column_values.md), [`tables()`](tables.md), [`cda_functions()`](cda_functions.md)
```

---

## `docs/documentation/cdapython/man_pages/column_values.md`

```markdown
---
title: column_values()
---

# `column_values()`

**NAME**

`column_values` — show all distinct values present in a column, with occurrence counts

**SYNOPSIS**

```python
column_values(
    column='',
    *,
    return_data_as='',
    output_file='',
    sort_by='',
    filters=None,
    data_source=None,
    force=False
)
```

**DESCRIPTION**

Show all distinct values present in `column`, along with a count of occurrences for each value.

**ARGUMENTS**

- `column` (*string, required*)
  The column to fetch values from.

- `return_data_as` (*string, optional: `'dataframe'`, `'list'`, or `'tsv'`*)
  Specify how `column_values()` should return results: as a pandas DataFrame, a Python list, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which `column_values()` will write tab-delimited results.

- `sort_by` (*string, optional: `'count'` (default for `return_data_as='dataframe'` and `'tsv'`), `'value'` (default for `return_data_as='list'`), `'count:desc'`, `'value:desc'`, `'count:asc'`, or `'value:asc'`*)
  Specify the primary field to sort when preparing result data: on values, or on counts of values.

  A field name with a suffix of `:desc` appended to it will be sorted in reverse order; adding `:asc` will ensure ascending sort order. Example: `sort_by='value:desc'`

  Secondary sort order is automatic: if results are primarily sorted by count, they are also (alphabetically) sorted by value within each group of values sharing the same count. If results are primarily sorted by value, there is no secondary sort — each value is unique by design, so there are no same-value groups with differing counts to further arrange.

- `filters` (*string or list of strings, optional*)
  Restrict returned values to those matching any of the given strings. A wildcard (`*`) at either or both ends of each string allows partial matches. Case is ignored. Specify an empty filter string `''` to match and count missing (null) values.

- `data_source` (*string, optional*)
  Restrict returned values to the given upstream data source. Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'PDC'`, `'IDC'`, and `'ICDC'`. Defaults to `None` (no filter).

- `force` (*boolean, optional*)
  Force execution of high-overhead queries on columns (like IDs) flagged as having large numbers of values. Defaults to `False`, in which case attempts to retrieve values for flagged columns result in a warning.

**RETURNS**

`pandas.DataFrame` — or — `list` — or — nothing; results are written to a user-specified TSV file.

**SEE ALSO**

[`columns()`](columns.md), [`tables()`](tables.md), [`cda_functions()`](cda_functions.md)
```

---

## `docs/documentation/cdapython/man_pages/summarize_subjects.md`

```markdown
---
title: summarize_subjects()
---

# `summarize_subjects()`

**NAME**

`summarize_subjects` — get a value-count report profiling a filtered set of CDA subject rows

**SYNOPSIS**

```python
summarize_subjects(
    *search_terms,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    return_data_as='',
    output_file='',
    add_extras=None
)
```

**DESCRIPTION**

For a set of CDA subject rows that all match a user-specified set of filters — "result rows" — get a report showing counts of values present in that set of rows, profiled across (user-modifiable) columns of interest.

**ARGUMENTS**

- `search_terms` (*zero or more strings, optional*)
  One or more search terms (including phrases), all of which must be associated with each result row. A wildcard `*` at either or both ends of each term enables partial matches to longer values.
  Example: `summarize_subjects('kidney', 'adeno*', 'hispanic or latino')`

- `match_all` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings (see **FILTER STRINGS** below), **all** of which must be met by all result rows.

- `match_any` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **at least one** of which must be met by all result rows.

- `match_from_file` (*3-element dictionary of strings, optional*)
  A dictionary with three named elements:
  1. `input_file` — the name of a local TSV file (with column names in its first row)
  2. `input_column` — the name of a column in that TSV
  3. `cda_column_to_match` — the name of a CDA column

  Restricts result rows to those where the value of the given CDA column matches at least one value from the given column in the given TSV file.

- `data_source` (*string or list of strings, optional*)
  Restrict results to those deriving from the given upstream data source(s). Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'IDC'`, `'PDC'`, and `'ICDC'`. Default: no filter.

- `add_columns` (*string or list of strings, optional*)
  One or more columns from a second table to add to summary output.

- `exclude_columns` (*string or list of strings, optional*)
  One or more columns to remove from summary output.

- `return_data_as` (*string, optional: `'dataframe_list'`, `'dict'`, or `'json'`*)
  Specify how to return results: as a list of pandas DataFrames, as a Python dictionary, or as output written to a JSON file named by the user. If omitted, for each DataFrame that would have been returned by `'dataframe_list'`, a table is instead pretty-printed to standard output (and nothing is returned).

- `output_file` (*string, optional*)
  If `return_data_as='json'` is specified, `output_file` should contain a resolvable path to a file into which JSON-formatted results will be written.

- `add_extras` (*string or list of strings, optional*)
  One or more columns of extra metadata to include, to contextualize harmonized CDA column values. Current valid values are `'synonym_terms'`, `'slim_terms'`, `'containing_terms'`, and `'all'` (which includes all of the above). Default: no extras.

**FILTER STRINGS**

Filter strings are expressions of the form `"COLUMN_NAME OP VALUE"` (the whitespace surrounding `OP` is required), where:

- `COLUMN_NAME` is a searchable CDA column (see [`columns()`](columns.md))
- `OP` is one of: `<` `<=` `>` `>=` `=` `!=`
- `VALUE` is a value of whatever data type is stored in `COLUMN_NAME`, or the special keyword `NULL`, indicating the filter should match missing (null) values in `COLUMN_NAME`

`=` and `!=` work on numeric, boolean, and string values. `<` `<=` `>` `>=` work only on numeric values.

Partial matches to string values are supported by adding `*` to either or both ends. Examples:

```
diagnosis = *duct*
sex = F*
size < 100
```

String values need not be quoted inside filter strings:

```python
summarize_subjects(match_all=['diagnosis = *duct*', 'sex = F*'])
```

`NULL` matches missing data:

```python
summarize_subjects(match_all=['year_of_birth = NULL'])
```

**RETURNS**

`list` of `pandas.DataFrame` objects, one per summarized column, enumerating counts (or statistical summaries, for unbounded numeric values) over all of that column's data values appearing in matching result rows. Two DataFrames in this list — `number_of_matching_subjects` and `number_of_files_related_to_matching_subjects` — contain integers representing the total number of result subject rows and the total number of related files, respectively. Every other DataFrame is titled with a CDA column name and contains value counts or statistical summaries for that column, as filtered by the result row set.

— or —

Python `dict` enumerating counts of all data values for each summarized column (or a statistical summary, for unbounded numeric data) across all matching result rows. Two keys — `number_of_matching_subjects` and `number_of_files_related_to_matching_subjects` — point to integers representing the total number of result subject rows and associated file rows, respectively. Every other key is a CDA column name, whose value is itself a dictionary enumerating observed value counts (or a statistical summary) for that column.

— or —

JSON-formatted text representing the same structure as `return_data_as='dict'`, written to `output_file`.

— or —

nothing; a series of tables describing the same data is printed to standard output instead.

**NOTES**

Worth knowing while reading these counts: the file count reported here is *every file belonging to a subject who matched*, which can include files that have nothing to do with why that subject matched in the first place. If you want a count of files that themselves satisfy your filter, use [`summarize_files()`](summarize_files.md) instead.

**SEE ALSO**

[`summarize_files()`](summarize_files.md), [`get_subject_data()`](get_subject_data.md), [`columns()`](columns.md)
```

---

## `docs/documentation/cdapython/man_pages/summarize_files.md`

```markdown
---
title: summarize_files()
---

# `summarize_files()`

**NAME**

`summarize_files` — get a value-count report profiling a filtered set of CDA file rows

**SYNOPSIS**

```python
summarize_files(
    *search_terms,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    return_data_as='',
    output_file='',
    add_extras=None
)
```

**DESCRIPTION**

For a set of CDA file rows that all match a user-specified set of filters — "result rows" — get a report showing counts of values present in that set of rows, profiled across (user-modifiable) columns of interest.

This function's arguments and filter-string syntax are identical to [`summarize_subjects()`](summarize_subjects.md), applied to the `file` table instead of `subject`. See `summarize_subjects()` for the full description of each argument and of filter-string syntax.

**ARGUMENTS**

- `search_terms` (*zero or more strings, optional*)
  One or more search terms (including phrases), all of which must be associated with each result row. A wildcard `*` at either or both ends of each term enables partial matches to longer values.
  Example: `summarize_files('kidney', 'adeno*', 'hispanic or latino')`

- `match_all` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **all** of which must be met by all result rows.

- `match_any` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **at least one** of which must be met by all result rows.

- `match_from_file` (*3-element dictionary of strings, optional*)
  A dictionary with three named elements:
  1. `input_file` — the name of a local TSV file (with column names in its first row)
  2. `input_column` — the name of a column in that TSV
  3. `cda_column_to_match` — the name of a CDA column

  Restricts result rows to those where the value of the given CDA column matches at least one value from the given column in the given TSV file.

- `data_source` (*string or list of strings, optional*)
  Restrict results to those deriving from the given upstream data source(s). Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'IDC'`, `'PDC'`, and `'ICDC'`. Default: no filter.

- `add_columns` (*string or list of strings, optional*)
  One or more columns from a second table to add to summary output.

- `exclude_columns` (*string or list of strings, optional*)
  One or more columns to remove from summary output.

- `return_data_as` (*string, optional: `'dataframe_list'`, `'dict'`, or `'json'`*)
  Specify how to return results: as a list of pandas DataFrames, as a Python dictionary, or as output written to a JSON file named by the user. If omitted, for each DataFrame that would have been returned by `'dataframe_list'`, a table is instead pretty-printed to standard output (and nothing is returned).

- `output_file` (*string, optional*)
  If `return_data_as='json'` is specified, `output_file` should contain a resolvable path to a file into which JSON-formatted results will be written.

- `add_extras` (*string or list of strings, optional*)
  One or more columns of extra metadata to include, to contextualize harmonized CDA column values. Current valid values are `'synonym_terms'`, `'slim_terms'`, `'containing_terms'`, and `'all'` (which includes all of the above). Default: no extras.

**FILTER STRINGS**

Filter strings are expressions of the form `"COLUMN_NAME OP VALUE"` (the whitespace surrounding `OP` is required), where:

- `COLUMN_NAME` is a searchable CDA column (see [`columns()`](columns.md))
- `OP` is one of: `<` `<=` `>` `>=` `=` `!=`
- `VALUE` is a value of whatever data type is stored in `COLUMN_NAME`, or the special keyword `NULL`, indicating the filter should match missing (null) values in `COLUMN_NAME`

`=` and `!=` work on numeric, boolean, and string values. `<` `<=` `>` `>=` work only on numeric values.

Partial matches to string values are supported by adding `*` to either or both ends. Examples:

```
diagnosis = *duct*
sex = F*
size < 100
```

String values need not be quoted inside filter strings:

```python
summarize_files(match_all=['diagnosis = *duct*', 'sex = F*', 'size < 100'])
```

`NULL` matches missing data:

```python
summarize_files(match_all=['access = NULL'])
```

**RETURNS**

`list` of `pandas.DataFrame` objects, one per summarized column, enumerating counts (or statistical summaries, for unbounded numeric values) over all of that column's data values appearing in matching result rows. Two DataFrames in this list — `number_of_matching_files` and `number_of_subjects_related_to_matching_files` — contain integers representing the total number of result file rows and the total number of related subjects, respectively. Every other DataFrame is titled with a CDA column name and contains value counts or statistical summaries for that column, as filtered by the result row set.

— or —

Python `dict` enumerating counts of all data values for each summarized column (or a statistical summary, for unbounded numeric data) across all matching result rows. Two keys — `number_of_matching_files` and `number_of_subjects_related_to_matching_files` — point to integers representing the total number of result file rows and associated subject rows, respectively. Every other key is a CDA column name, whose value is itself a dictionary enumerating observed value counts (or a statistical summary) for that column.

— or —

JSON-formatted text representing the same structure as `return_data_as='dict'`, written to `output_file`.

— or —

nothing; a series of tables describing the same data is printed to standard output instead.

**SEE ALSO**

[`summarize_subjects()`](summarize_subjects.md), [`get_file_data()`](get_file_data.md), [`columns()`](columns.md)
```

---

## `docs/documentation/cdapython/man_pages/get_subject_data.md`

```markdown
---
title: get_subject_data()
---

# `get_subject_data()`

**NAME**

`get_subject_data` — get CDA subject rows matching user-specified criteria

**SYNOPSIS**

```python
get_subject_data(
    *search_terms,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    collate_results=False,
    include_external_refs=False,
    return_data_as='dataframe',
    output_file='',
    add_extras=None
)
```

**DESCRIPTION**

Get CDA subject rows ("result rows") that match user-specified criteria.

**ARGUMENTS**

- `search_terms` (*zero or more strings, optional*)
  One or more search terms (including phrases), all of which must be associated with each result row. A wildcard `*` at either or both ends of each term enables partial matches to longer values.
  Example: `get_subject_data('kidney', 'adeno*', 'hispanic or latino')`

- `match_all` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings (see **FILTER STRINGS** below), **all** of which must be met by all result rows.

- `match_any` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **at least one** of which must be met by all result rows.

- `match_from_file` (*3-element dictionary of strings, optional*)
  A dictionary with three named elements:
  1. `input_file` — the name of a local TSV file (with column names in its first row)
  2. `input_column` — the name of a column in that TSV
  3. `cda_column_to_match` — the name of a CDA column

  Restricts result rows to those where the value of the given CDA column matches at least one value from the given column in the given TSV file. If matching on native source identifiers (e.g. a GDC case UUID) rather than CDA's own subject IDs, match against `upstream_id` instead of `subject_id`.

- `data_source` (*string or list of strings, optional*)
  Restrict results to those deriving from the given upstream data source(s). Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'IDC'`, `'PDC'`, and `'ICDC'`. Default: no filter.

- `add_columns` (*string or list of strings, optional*)
  One or more columns from a second table to add to result data.

- `exclude_columns` (*string or list of strings, optional*)
  One or more columns to remove from result data.

- `collate_results` (*boolean, optional*)
  If `True`: for each result subject, include a DataFrame collating results linked to that subject from each non-subject table that was queried. Otherwise, for each result subject, include a list of unique values associated with that subject from each non-subject column that was queried. Default: `False`.

- `include_external_refs` (*boolean, optional*)
  If `True`: for each result subject, include a DataFrame called `external_reference_data` that collates references to external resources containing data describing that subject. Default: `False`.

- `return_data_as` (*string, optional: `'dataframe'` or `'tsv'`*)
  Specify how to return results: as a pandas DataFrame, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which tab-delimited results will be written.

- `add_extras` (*string or list of strings, optional*)
  One or more columns of extra metadata to include, to contextualize harmonized CDA column values. Current valid values are `'synonym_terms'`, `'slim_terms'`, `'containing_terms'`, and `'all'` (which includes all of the above). Default: no extras.

**FILTER STRINGS**

Filter strings are expressions of the form `"COLUMN_NAME OP VALUE"` (the whitespace surrounding `OP` is required), where:

- `COLUMN_NAME` is a searchable CDA column (see [`columns()`](columns.md))
- `OP` is one of: `<` `<=` `>` `>=` `=` `!=`
- `VALUE` is a value of whatever data type is stored in `COLUMN_NAME`, or the special keyword `NULL`, indicating the filter should match missing (null) values in `COLUMN_NAME`

`=` and `!=` work on numeric, boolean, and string values. `<` `<=` `>` `>=` work only on numeric values.

Partial matches to string values are supported by adding `*` to either or both ends. Examples:

```
diagnosis = *duct*
sex = F*
```

String values need not be quoted inside filter strings:

```python
get_subject_data(match_all=['diagnosis = *duct*', 'sex = F*'])
```

`NULL` matches missing data:

```python
get_subject_data(match_all=['cause_of_death = NULL'])
```

**RETURNS**

(Default) `pandas.DataFrame` containing CDA subject data matching the user-specified filter criteria. The DataFrame's named columns match columns in the `subject` table plus any optional user-added columns from other tables, and each row represents one CDA `subject` row (possibly with related data from other tables appended, according to user directives).

— or —

nothing; results are written to a user-specified TSV file.

**SEE ALSO**

[`get_file_data()`](get_file_data.md), [`summarize_subjects()`](summarize_subjects.md), [`intersect_subject_results()`](intersect_subject_results.md), [`expand_subject_results()`](expand_subject_results.md), [`columns()`](columns.md)
```

---

## `docs/documentation/cdapython/man_pages/get_file_data.md`

```markdown
---
title: get_file_data()
---

# `get_file_data()`

**NAME**

`get_file_data` — get CDA file rows matching user-specified criteria

**SYNOPSIS**

```python
get_file_data(
    *search_terms,
    match_all=None,
    match_any=None,
    match_from_file={'input_file': '', 'input_column': '', 'cda_column_to_match': ''},
    data_source=None,
    add_columns=None,
    exclude_columns=None,
    collate_results=False,
    return_data_as='dataframe',
    output_file='',
    add_extras=None
)
```

**DESCRIPTION**

Get CDA file rows ("result rows") that match user-specified criteria.

**ARGUMENTS**

- `search_terms` (*zero or more strings, optional*)
  One or more search terms (including phrases), all of which must be associated with each result row. A wildcard `*` at either or both ends of each term enables partial matches to longer values.
  Example: `get_file_data('kidney', 'adeno*', 'hispanic or latino')`

- `match_all` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings (see **FILTER STRINGS** below), **all** of which must be met by all result rows.

- `match_any` (*string or list of strings, optional*)
  One or more conditions, expressed as filter strings, **at least one** of which must be met by all result rows.

- `match_from_file` (*3-element dictionary of strings, optional*)
  A dictionary with three named elements:
  1. `input_file` — the name of a local TSV file (with column names in its first row)
  2. `input_column` — the name of a column in that TSV
  3. `cda_column_to_match` — the name of a CDA column

  Restricts result rows to those where the value of the given CDA column matches at least one value from the given column in the given TSV file.

- `data_source` (*string or list of strings, optional*)
  Restrict results to those deriving from the given upstream data source(s). Current valid values are `'CTDC'`, `'GC'`, `'GDC'`, `'IDC'`, `'PDC'`, and `'ICDC'`. Default: no filter.

- `add_columns` (*string or list of strings, optional*)
  One or more columns from a second table to add to result data.

- `exclude_columns` (*string or list of strings, optional*)
  One or more columns to remove from result data.

- `collate_results` (*boolean, optional*)
  If `True`: for each result file, include a DataFrame collating results linked to that file from each non-file table that was queried. Otherwise, for each result file, include a list of unique values associated with that file from each non-file column that was queried. Default: `False`.

- `return_data_as` (*string, optional: `'dataframe'` or `'tsv'`*)
  Specify how to return results: as a pandas DataFrame, or as output written to a TSV file named by the user. If omitted, defaults to returning results as a DataFrame.

- `output_file` (*string, optional*)
  If `return_data_as='tsv'` is specified, `output_file` should contain a resolvable path to a file into which tab-delimited results will be written.

- `add_extras` (*string or list of strings, optional*)
  One or more columns of extra metadata to include, to contextualize harmonized CDA column values. Current valid values are `'synonym_terms'`, `'slim_terms'`, `'containing_terms'`, and `'all'` (which includes all of the above). Default: no extras.

**FILTER STRINGS**

Filter strings are expressions of the form `"COLUMN_NAME OP VALUE"` (the whitespace surrounding `OP` is required), where:

- `COLUMN_NAME` is a searchable CDA column (see [`columns()`](columns.md))
- `OP` is one of: `<` `<=` `>` `>=` `=` `!=`
- `VALUE` is a value of whatever data type is stored in `COLUMN_NAME`, or the special keyword `NULL`, indicating the filter should match missing (null) values in `COLUMN_NAME`

`=` and `!=` work on numeric, boolean, and string values. `<` `<=` `>` `>=` work only on numeric values.

Partial matches to string values are supported by adding `*` to either or both ends. Examples:

```
diagnosis = *duct*
sex = F*
```

String values need not be quoted inside filter strings:

```python
get_file_data(match_all=['diagnosis = *duct*', 'sex = F*'])
```

`NULL` matches missing data — including in fields from associated subject rows:

```python
get_file_data(match_all=['cause_of_death = NULL'])
```

**RETURNS**

(Default) `pandas.DataFrame` containing CDA file data matching the user-specified filter criteria. The DataFrame's named columns match columns in the `file` table plus any optional user-added columns from other tables, and each row represents one CDA `file` row (possibly with related data from other tables appended, according to user directives).

— or —

nothing; results are written to a user-specified TSV file.

**SEE ALSO**

[`get_subject_data()`](get_subject_data.md), [`summarize_files()`](summarize_files.md), [`intersect_subject_results()`](intersect_subject_results.md), [`expand_subject_results()`](expand_subject_results.md), [`columns()`](columns.md)
```

---

## `docs/documentation/cdapython/man_pages/intersect_subject_results.md`

```markdown
---
title: intersect_subject_results()
---

# `intersect_subject_results()`

**NAME**

`intersect_subject_results` — merge `get_subject_data()` results via intersection

**SYNOPSIS**

```python
intersect_subject_results(*result_dfs_to_merge, ignore_added_columns=False)
```

**DESCRIPTION**

Combine two or more DataFrames produced by [`get_subject_data()`](get_subject_data.md) via intersection: merge result data for all subjects present in **all** input DataFrames.

**ARGUMENTS**

- `result_dfs_to_merge` (*two or more DataFrames, required*)
  DataFrames returned by `get_subject_data()`.

- `ignore_added_columns` (*boolean, optional*)
  Merge only columns from the subject table: avoids breakages in cases where added extra (non-subject) columns can't be merged, due to differences in how similar but different upstream queries produced the results being merged. Default: `False` — try to merge subject data plus all extra data appearing in all input DataFrames.

**RETURNS**

`pandas.DataFrame` containing combined metadata about all subject rows that appear in all input DataFrames, including, by default, all associated non-subject data present in all input DataFrames.

**SEE ALSO**

[`get_subject_data()`](get_subject_data.md), [`expand_subject_results()`](expand_subject_results.md)
```

---

## `docs/documentation/cdapython/man_pages/expand_subject_results.md`

```markdown
---
title: expand_subject_results()
---

# `expand_subject_results()`

**NAME**

`expand_subject_results` — flatten a nested per-subject column into a 2-dimensional table

**SYNOPSIS**

```python
expand_subject_results(results_dataframe, column_to_expand)
```

**DESCRIPTION**

Given a result DataFrame `R` returned by [`get_subject_data()`](get_subject_data.md), and a column `C` in `R` that contains DataFrames, return a version of the information in `C` expanded into a 2-dimensional table `T`, with one row in `T` for every row in every DataFrame in `C`, and with each row in `T` also containing the `subject_id` in `R` that goes with that row.

**ARGUMENTS**

- `results_dataframe` (*pandas.DataFrame, required*)
  A result DataFrame returned by `get_subject_data()`.

- `column_to_expand` (*string, required*)
  The name of a column in `results_dataframe` whose values are themselves DataFrames (for example, a column produced via `collate_results=True`).

**RETURNS**

`pandas.DataFrame` — a flattened, 2-dimensional table with one row per row of every nested DataFrame in `column_to_expand`, each annotated with its associated `subject_id`.

**SEE ALSO**

[`get_subject_data()`](get_subject_data.md), [`intersect_subject_results()`](intersect_subject_results.md)
```

---

## `docs/documentation/cdapython/man_pages/intersect_file_results.md`

```markdown
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
```

---

## `docs/documentation/cdapython/man_pages/expand_file_results.md`

```markdown
---
title: expand_file_results()
---

# `expand_file_results()`

**NAME**

`expand_file_results` — flatten a nested per-file column into a 2-dimensional table

**SYNOPSIS**

```python
expand_file_results(results_dataframe, column_to_expand)
```

**DESCRIPTION**

Given a result DataFrame `R` returned by [`get_file_data()`](get_file_data.md), and a column `C` in `R` that contains DataFrames, return a version of the information in `C` expanded into a 2-dimensional table `T`, with one row in `T` for every row in every DataFrame in `C`, and with each row in `T` also containing the `file_id` in `R` that goes with that row.

**ARGUMENTS**

- `results_dataframe` (*pandas.DataFrame, required*)
  A result DataFrame returned by `get_file_data()`.

- `column_to_expand` (*string, required*)
  The name of a column in `results_dataframe` whose values are themselves DataFrames (for example, a column produced via `collate_results=True`).

**RETURNS**

`pandas.DataFrame` — a flattened, 2-dimensional table with one row per row of every nested DataFrame in `column_to_expand`, each annotated with its associated `file_id`.

**SEE ALSO**

[`get_file_data()`](get_file_data.md), [`intersect_file_results()`](intersect_file_results.md)
```

---

## `docs/documentation/cdapython/vignettes/index.md`

```markdown
---
title: Vignette Conceptual Overview
---

# Vignette Conceptual Overview

You can think of the CDA as a really, really enormous spreadsheet full of data. To search this enormous spreadsheet, you'd want to select columns that have data you're interested in, and then filter the rows to only the values you care about.

CDA makes this data searchable in two main endpoints:

- **subject:** a patient entity capturing the study-independent metadata for research subjects. Human research subjects are usually not traceable to a particular person, to protect their privacy.
- **file:** a unit of data about subjects, research subjects, specimens, or their associated information.

If you're looking to build a cohort of distinct individuals who meet some criteria, you'd search using `get_subject_data`, which returns a table with one row per subject -- then use the `add_columns` parameter inside `get_subject_data` to pull in extra information per subject (file details, treatment history, whatever's relevant to what you're building).

## The five vignettes

This site includes 5 standalone vignettes, each built around a different starting point for the same underlying question -- "is there already data about X?":

1. [Is there anything about X?](01_global_search.ipynb) -- a bare-term global search
2. [Getting oriented before I filter](02_systematic_browsing.ipynb) -- browsing tables/columns/values deliberately before committing to a query
3. [I have subjects, what else exists](03_match_from_file.ipynb) -- checking a real GDC case export against what else CDA knows, matching on native `upstream_id`s
4. [Reassembling a scattered project](04_cptac_reassembly.ipynb) -- finding every piece of a known project (like CPTAC) that got split across data centers
5. [Subjects with multiple data types](05_multimodal_patients.ipynb) -- finding subjects who have two or more kinds of data for the same condition

## A note on harmonization and ontologies

Worth knowing as you read these: only `anatomic_site` and `disease` currently have true ontology-backed rollup behavior in CDA (UBERON and ICD-O-3, respectively) -- those are the only fields where `add_extras` will show something meaningfully new. Most other harmonized fields are fully standardized but conceptually flat (no hierarchy to roll up through, e.g. `sex`, `species`); a handful of fields aren't harmonized yet at all (`stage`, `treatment_type`, and others). Full harmonization status and mappings are public at the [harmonization reference repo](https://github.com/CancerDataAggregator/harmonization_reference/tree/main/value_maps_by_concept).
```

---

## `docs/documentation/cdapython/vignettes/01_global_search.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Is there anything about kidney cancer already?\n",
    "\n",
    "*Standalone -- no prior vignette required.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I'm a grad student. I don't have a disease picked out yet, and I don't have much budget to go collect new data myself -- so before I commit to anything, I just want to know: is there *already* data out there about kidney cancer? I don't know what columns CDA has, I don't know what words the data uses internally, and honestly I don't want to find out before I even know if this is worth my time.\n",
    "\n",
    "So I'm not going to go look anything up first. I'm just going to type the word and see what happens."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cdapython import *\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "opt.classes=\"display nowrap compact\"\n",
    "opt.buttons=[\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.maxBytes=0\n",
    "opt.columnDefs = [{\"className\": \"dt-left\", \"targets\": \"_all\"}]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects('kidney')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "46,569 subjects, from one word, with zero setup. I didn't tell it which column to look in -- `kidney` could be an anatomic site, a diagnosis, part of a file description, anything -- it just searched everywhere at once and found every subject connected to the term in any way.\n",
    "\n",
    "I don't know yet if that's useful to me. Let's see what these subjects actually look like before deciding anything. The summary doesn't show every column by default, so let me check what's available and pull in a few that sound relevant:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "columns()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects('kidney', add_columns=['anatomic_site', 'diagnosis', 'format'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Interesting -- a lot of these subjects also show up with `vcf` in their file formats. If there's sequencing data sitting around too, that's worth knowing before I pick a direction. I can just add a second word -- I don't need to abandon the first one or restart with a more careful query:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects('kidney', 'vcf', add_columns=['anatomic_site', 'diagnosis', 'format'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Two free-text terms like this means \"must touch both\" -- every subject here is connected to *both* kidney and vcf somewhere in their record, still searched across every column at once. 2,516 subjects, with 23,096 vcf files between them -- a much smaller, more specific number than my first search, and I got there without writing a single filter string."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now I want to actually look at the `anatomic_site` column on these results, and there's more going on in it than I expected. The biggest single value isn't \"kidney\" at all -- it's a missing/null value, which just means plenty of these subjects matched on something other than anatomy (their diagnosis, a file description, whatever). After that, \"kidney\" itself is the largest real value, which makes sense.\n",
    "\n",
    "But then \"blood\" shows up with over 20,000 hits. That has nothing to do with kidney anatomy. What's actually happening is that global search found a subject through *some* connection to \"kidney,\" and then showed me *everything* about that subject -- including a completely unrelated blood draw that has nothing to do with why they matched in the first place. That's not a mistake; it's the whole point of searching at the subject level instead of the field level. I didn't ask for blood data, but now I know it's there, which I never would have found if I'd only searched inside the anatomic_site field directly."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The second thing I notice: \"right kidney\" and \"left kidney\" also show up, each more specific than the plain word I typed. That one *is* an anatomy match -- CDA's anatomic_site field is backed by a real medical ontology (UBERON), and searching a broad term like \"kidney\" automatically pulls in anything more specific that sits underneath it in that hierarchy. \"Right kidney\" and \"left kidney\" are two of those more-specific terms; there are dozens more sitting even deeper in that same branch that never happened to show up directly in my particular result set. I didn't need to know that hierarchy existed, let alone look anything up in it, for this to work.\n",
    "\n",
    "So two different things just happened in the same result: one subject-level (\"here's everything about this person, including blood work you didn't ask for\") and one anatomy-specific (\"here's a more precise version of the term you typed, found automatically\"). If I want to know *why* a specific anatomic_site row matched -- the literal word, or something more specific rolling up -- I can ask CDA to show its work:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects('kidney', 'vcf', add_columns=['anatomic_site', 'diagnosis', 'format'], add_extras=['all'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Same subjects, same count -- `add_extras` doesn't change what matched, it just annotates *why*. A row with \"right kidney\" now shows that it matched because it rolls up to \"kidney\" in the ontology.\n",
    "\n",
    "Worth knowing: this kind of automatic rollup currently only happens for `anatomic_site` and `disease` -- those are the two fields backed by a real external ontology (UBERON and ICD-O-3, respectively). Most other harmonized fields, like `sex` or `species`, are fully standardized too, but don't have a hierarchy to roll up through in the first place -- there's no such thing as a \"more specific\" sex. A few fields (`stage`, `treatment_type`, and others) aren't harmonized yet at all. So `add_extras` won't do anything interesting on those -- not because something's broken, but because there's nothing underneath them yet to show."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I still haven't written a single filter, looked up a controlled vocabulary, or checked what table anything lives in. 2,516 subjects with both kidney involvement and sequencing data is enough for me to decide this is worth pursuing -- and if I do, [Getting oriented before I filter](02_systematic_browsing.ipynb) is where I'd go next to actually get oriented in what's here before building a real query."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `docs/documentation/cdapython/vignettes/02_systematic_browsing.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Getting oriented before I write a real query\n",
    "\n",
    "*Standalone -- no prior vignette required.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I'm building toward an actual grant proposal, so unlike just poking around with a keyword, I want to know what I'm working with before I commit to anything. I don't want to guess at a column name and get it wrong, and I don't want to filter on a value that turns out to be spelled differently than I assumed. Before I touch `get_subject_data`, I want to look around."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cdapython import *\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "opt.classes=\"display nowrap compact\"\n",
    "opt.buttons=[\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.maxBytes=0\n",
    "opt.columnDefs = [{\"className\": \"dt-left\", \"targets\": \"_all\"}]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, the biggest-picture view -- what tables even exist to search:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I'm interested in age at diagnosis, but I don't know the exact column name offhand. Rather than guess, I can search by what a column is described as doing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "columns(description='age')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`age_at_observation` looks right, and its description tells me it's recorded in years -- I didn't have to find that out the hard way by filtering and getting confused later. Before I filter on it, I want to see what the values actually look like -- is it populated often, are there extreme outliers, anything odd:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "column_values('age_at_observation', data_source='GDC')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "That gives me a real sense of the range before I write a single filter. Now I want a count, not a list of rows -- how many subjects actually have both an adenocarcinoma diagnosis and a non-null age:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects(match_all=['diagnosis = *adenocarcinoma*', 'age_at_observation != NULL'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1,308 subjects. `!= NULL` here means \"has a value at all,\" not an unusual edge case -- it's a normal, filterable condition. The reverse (`age_at_observation = NULL`) would show me everyone *missing* an age, which is its own useful check: if I required age on every search, how much data would I silently be throwing away?\n",
    "\n",
    "Some of what matched here turned out to be mice, so I'll narrow further:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects(match_all=['diagnosis = *adenocarcinoma*', 'age_at_observation != NULL', 'species = human'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1,226 human subjects -- 82 of my original 1,308 turned out to be mice, filtered out with one added condition. That's a real, usable number. Now I want to look at age brackets specifically -- numeric columns support ordinary comparison operators, and I can chain two to express a range:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects(match_all=['60 < age_at_observation <= 70', 'diagnosis = *adenocarcinoma*', 'species = human'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "493 subjects in that age bracket alone. I checked the table landscape, found the right column by description instead of guessing, looked at real values before filtering, and used `NULL` and numeric ranges deliberately rather than stumbling into them. None of this required knowing the underlying data model or any source's internal vocabulary -- just a willingness to look before leaping, which is the whole point of browsing first when the stakes are higher than idle curiosity."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `docs/documentation/cdapython/vignettes/03_match_from_file.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Checking my own subject list against what else CDA knows\n",
    "\n",
    "*Standalone -- no prior vignette required.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I pulled a case list straight out of GDC -- demographics, diagnoses, project info, which experimental strategies each case has, file counts, all of it. This is the file I've actually been working in. I'm not looking for new subjects, and I'm not trying to explore anything -- I already have my cohort. What I want to know is whether there's *more* data about these specific people sitting in CDA that GDC alone doesn't show me, without retyping every case ID into a filter by hand, and without making a separate clean file just for CDA -- I want to use the file I already have."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cdapython import *\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "opt.classes=\"display nowrap compact\"\n",
    "opt.buttons=[\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.maxBytes=0\n",
    "opt.columnDefs = [{\"className\": \"dt-left\", \"targets\": \"_all\"}]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "My file, `cases.tsv`, has a column called `id` with GDC's own case UUIDs in it -- `bc84c5c5-1785-4edd-b732-8987f862063e` and so on. These aren't CDA's internal subject IDs; they're the native identifiers GDC itself assigned, the same ones I'd already be using in any GDC-side analysis. `match_from_file` takes three things: which file, which column in that file to use, and which CDA column to match it against. Since I'm matching native source IDs instead of CDA's own IDs, I match against `upstream_id`, not `subject_id`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_subject_data(\n",
    "    match_from_file={\n",
    "        'input_file': 'cases.tsv',\n",
    "        'input_column': 'id',\n",
    "        'cda_column_to_match': 'upstream_id'\n",
    "    },\n",
    "    add_columns='upstream_identifiers.*'\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This matters because I never had to convert anything -- the exact IDs sitting in my existing GDC export work directly as a CDA lookup key, as long as `upstream_id` is what I tell it to match against instead of CDA's own ID scheme. Adding `upstream_identifiers.*` shows me exactly which sources have data on each case -- these are all TCGA-OV subjects pulled from GDC, so I'm curious whether any of them also show up in PDC or another source I wasn't already looking at.\n",
    "\n",
    "Before pulling full records, I want a shape of what I'd actually be getting:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_files(match_from_file={\n",
    "    'input_file': 'cases.tsv',\n",
    "    'input_column': 'id',\n",
    "    'cda_column_to_match': 'upstream_id'\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects(match_from_file={\n",
    "    'input_file': 'cases.tsv',\n",
    "    'input_column': 'id',\n",
    "    'cda_column_to_match': 'upstream_id'\n",
    "})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that I know whether there's more data out there on these cases than GDC alone showed me, I want to know exactly where each piece came from -- not just \"PDC has something,\" but a pointer back to that source's own record for this specific case, so I can look at it directly or cite it properly:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "subjects_with_refs = get_subject_data(\n",
    "    match_from_file={\n",
    "        'input_file': 'cases.tsv',\n",
    "        'input_column': 'id',\n",
    "        'cda_column_to_match': 'upstream_id'\n",
    "    },\n",
    "    include_external_refs=True\n",
    ")\n",
    "subjects_with_refs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There's a new `external_reference_data` column here -- a small table per subject pointing back to the actual upstream record that described them, separate from `data_source` (which just tells me *which* data center a row came from, not the specific record). This is the kind of thing I'd want before citing a source properly in a publication, or before trusting that CDA's version of a record matches what GDC's own record actually says.\n",
    "\n",
    "And my case file -- demographics, diagnosis fields, experimental strategies, file counts, all of it -- never had to leave my spreadsheet in the first place. I searched using the export I already had, not a stripped-down copy made just for this lookup."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `docs/documentation/cdapython/vignettes/04_cptac_reassembly.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Please tell me you know how to find all the CPTAC data\n",
    "\n",
    "*Standalone -- no prior vignette required.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I just found out that the Clinical Proteomic Tumor Analysis Consortium (CPTAC) exists, and that its data got spread out across several different data centers -- not because anyone organized it that way, but because that's just where pieces of it happened to land over the years. Every one of those data centers has its own format, its own identifiers, its own way of describing things. If I had to go find every piece myself and figure out which subject in one repository was the same person as which subject in another, that's not a weekend project. That's a years-long archival nightmare, and I don't have years.\n",
    "\n",
    "So before I give up on reusing this data entirely, I want to know: can this tool actually do that part for me?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cdapython import *\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "opt.classes=\"display nowrap compact\"\n",
    "opt.buttons=[\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.maxBytes=0\n",
    "opt.columnDefs = [{\"className\": \"dt-left\", \"targets\": \"_all\"}]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "columns(column=['*project*'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`project_name` looks like the right field. I'm searching for people, not files, so:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects(match_all='project_name = *cptac*')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4,504 subjects. One line. Every subject tagged as part of CPTAC, already reconciled across however many data centers their pieces actually live in, already matched up as the same people, without me ever touching an identifier-matching problem by hand. That multi-year harmonization headache I was dreading is just... done, invisibly, before I even ran this cell.\n",
    "\n",
    "Notice this summary also reports a file count: 340,803. I'll want the files eventually too, so let's look at them directly:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_files(match_all='project_name = *cptac*')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "294,674 files -- a smaller number than the 340,803 I just saw attached to my subjects, and that's worth understanding rather than brushing past. `summarize_subjects`' file count is *every file belonging to a subject who matched* -- which can include files that have nothing to do with CPTAC specifically, the same way an unrelated blood draw can tag along on a subject found through a completely different search. `summarize_files` only counts files that themselves satisfy the filter. Same subjects, two different units being counted -- one via the person, one via the file itself.\n",
    "\n",
    "Let me narrow to something specific -- I'm interested in kidney and bladder subjects today. I still want everything to be CPTAC, *and* I want it to touch one of two anatomic sites, so I need an \"all of this\" condition and an \"any of these\" condition at the same time:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_files(\n",
    "    match_all=['project_name = *cptac*'],\n",
    "    match_any=['anatomic_site = *kidney*', 'anatomic_site = *bladder*']\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "280 subjects, 36,942 files -- a much more targeted result than my unfiltered CPTAC pull. Since I'll actually need to retrieve these files, I want the `drs_uri` for each one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_file_data(\n",
    "    match_all=['project_name = *cptac*'],\n",
    "    match_any=['anatomic_site = *kidney*', 'anatomic_site = *bladder*']\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A `drs_uri` points directly at the cloud bucket where a file actually lives -- not at some portal or interface I'd have to visit at GDC, PDC, or wherever the file originally landed. I can hand these URIs straight to a cloud workspace like Terra or the Cancer Genomics Cloud, and the workspace resolves them on its own. There's no detour through any individual data center's own system. The only real constraint is access: if a file is controlled-access and I don't have the right permissions, having the URI doesn't get me the file -- but for anything open-access, this is the entire retrieval step.\n",
    "\n",
    "For instance, if I wanted to see how much of my unfiltered CPTAC total came from just one source:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summarize_subjects(match_all='project_name = *cptac*', data_source='GDC')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-- comparing that to my 4,504 total from earlier, the difference isn't just \"the rest came from elsewhere.\" A lot of these subjects have data at *more than one* data center, so they're counted once in my combined total but would also show up if I checked any other single source they happen to live in too. That's not a bug or a double-count on CDA's part -- it's just what cross-source reassembly actually looks like once you're reconnecting a project that was scattered to begin with."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `docs/documentation/cdapython/vignettes/05_multimodal_patients.ipynb`

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Finding subjects who have more than one kind of data\n",
    "\n",
    "*Standalone -- no prior vignette required.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "I don't just want \"everyone with kidney cancer\" -- I want subjects who have *both* imaging and sequencing data for the same kidney cancer, because my actual hypothesis needs to compare across modalities for the same person, not just pool two separate populations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from cdapython import *\n",
    "from itables import init_notebook_mode, show\n",
    "init_notebook_mode(all_interactive=True)\n",
    "import itables.options as opt\n",
    "opt.classes=\"display nowrap compact\"\n",
    "opt.buttons=[\"copyHtml5\", \"csvHtml5\", \"excelHtml5\"]\n",
    "opt.maxBytes=0\n",
    "opt.columnDefs = [{\"className\": \"dt-left\", \"targets\": \"_all\"}]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, what file types actually exist to ask for:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "columns(table='file')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "column_values('file_type')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`CT Image Storage` and `Annotated Somatic Mutation` look like the two I want. If I put both in one `match_all`, though, that won't work the way I want -- `match_all` means every condition has to be true of the *same row*, and no single file can be both a CT image and a mutation file at once. What I actually need is two separate searches -- kidney subjects with CT data, kidney subjects with mutation data -- and then the overlap between them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ct_subjects = get_subject_data(\n",
    "    match_all=['anatomic_site = *kidney*', 'file_type = CT Image Storage'],\n",
    "    add_columns='file.*'\n",
    ")\n",
    "\n",
    "mutation_subjects = get_subject_data(\n",
    "    match_all=['anatomic_site = *kidney*', 'file_type = Annotated Somatic Mutation'],\n",
    "    add_columns='file.*'\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`add_columns='file.*'` pulls in every column from the file table so I can see where to actually get these files later. That's useful, but it's worth knowing `exclude_columns` exists for the reverse case -- if a particular pull brought in columns I know I won't use, I can drop them by name the same way I added them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, the actual overlap -- subjects appearing in *both* result sets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ct_and_mutation = intersect_subject_results(ct_subjects, mutation_subjects)\n",
    "ct_and_mutation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "That's my actual cohort -- subjects who have both. But looking at the `file_type` and `file_id` columns, I can't tell which file belongs to which type for a given subject; everything's mashed together in one row per subject. Re-running with `collate_results=True` pairs up the related file columns per file, so I can tell which files have which properties:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ct_subjects = get_subject_data(\n",
    "    match_all=['anatomic_site = *kidney*', 'file_type = CT Image Storage'],\n",
    "    add_columns='file.*',\n",
    "    collate_results=True\n",
    ")\n",
    "mutation_subjects = get_subject_data(\n",
    "    match_all=['anatomic_site = *kidney*', 'file_type = Annotated Somatic Mutation'],\n",
    "    add_columns='file.*',\n",
    "    collate_results=True\n",
    ")\n",
    "ct_and_mutation = intersect_subject_results(ct_subjects, mutation_subjects)\n",
    "ct_and_mutation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There's a new `file_data` column now, with `data_source`, `file_id`, and `access` collated per file -- useful for feeding into another function, but still a nested structure that's hard to just look at directly. `expand_subject_results` flattens it into a normal table, one row per file instead of one row per subject:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "expand_subject_results(ct_and_mutation, 'file_data')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Same subjects as before, but now anyone with multiple files gets multiple rows, and each row only shows the values that actually go together. I now have exactly the cohort I needed -- confirmed to have both modalities, with the files per subject untangled instead of guessed at -- without ever needing to know how the underlying tables related to each other before I started."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

---

## `README.md`

```markdown
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

## Known issues

- **Missing images:** the About Us pages reference 18 image files (team photos, alumni photos, 6 data-source logos); only the CTDC logo is a confirmed real asset. The rest need to be supplied before these pages are complete.
- **Interactive Search page:** the instructions describe the Search Builder UI but don't yet include real screenshots.
- **Developer page theme limitation:** `hide: navigation, toc` frontmatter (a Material-for-MkDocs feature) has no effect under the `readthedocs` theme, so the Redoc viewer currently renders with the normal sidebar/TOC alongside it. Revisit if/when the theme is reconsidered.
- **Function Reference drift:** the man pages are transcribed from a documented snapshot of `cdapython`'s signatures and should be spot-checked against the installed package version periodically.
- **Vignettes 3 and 5** make live calls at build time; if `cases.tsv` (vignette 3's input file) isn't present in the build environment, that notebook will fail to execute. See open items below.

## Funding

This project has been funded in whole or in part with Federal funds from the National Cancer Institute, National Institutes of Health, Task Order No. 17X053 under Contract No. HHSN261200800001E
```

---

# Not included — files to carry over from your repo unchanged

These weren't part of the content work and have no text/draft issues to fix, so they're not reproduced above — just copy them straight from your existing repo:

- `docs/documentation/developers/service_openapi.yaml` (generated REST spec)
- Any actual image assets you do have (e.g. the CTDC logo, if saved)

---

# Open items — things you'll need to resolve, not fixed in this pass

**Missing assets**
1. **Team/alumni photos** (`docs/about_us/index.md`) — 12 image files referenced, none included in source material: Arthur, Amanda, Tanner, David, Bing-Xing, Finny, Surya, Jack, Rachel, Kat, Alex, plus the CRDC overview graphic.
2. **Data-source logos** (`docs/about_us/ourdata.md`) — 7 logo images referenced; only CTDC's is confirmed as a real saved asset (GDC, PDC, IDC, GC, ICDC, ISB-CGC logos are unconfirmed/missing).
3. **Interactive Search screenshots** — the Search Builder instructions describe UI elements (Add Condition, nesting button, etc.) but have no accompanying images; the original screenshots (`attachment:image.png` etc.) were never real files in this repo.

**Content/data dependencies**
4. **`cases.tsv`** — Vignette 3 (`match_from_file`) depends on this file being present in the build/execution environment. Confirm it's checked into the repo (or generated by a build step) before `execute: true` tries to run that notebook — otherwise the build will fail.
5. **Live-executed counts** — because `mkdocs-jupyter` runs with `execute: true`, every number quoted in the vignette prose (e.g. "46,569 subjects," "4,504 subjects") is illustrative based on a past run and will be replaced by whatever the live API returns at build time. If the API's data changes meaningfully, the surrounding narrative prose (which references specific numbers) may read oddly against the freshly executed output. Worth a periodic read-through after data releases.

**Design/theme decisions (parked, not blocking)**
6. **Theme reconsideration** — `readthedocs` theme is functional but doesn't support hiding nav/TOC (needed for a cleaner Redoc API page) or other Material-only features. A real theme decision (top nav, dual sidebars, sticky header, site search behavior) is still open.
7. **Developer page layout** — currently shows the normal sidebar/TOC next to the Redoc viewer because of the above theme limitation. Not broken, just not ideal.

**Maintenance**
8. **Function Reference accuracy** — the man pages are transcribed from a documented snapshot of `cdapython`. Worth a periodic diff against the actual installed package's function signatures (`help(function)` output) to catch drift.
9. **CORS-based interactive query tool** — the standalone dropdown-query prototype that tried to hit the API directly from the browser is deleted (confirmed broken, blocked by CORS/firewall). If in-browser ad-hoc querying beyond the static `interactive.ipynb` dataframe is still a goal, that's a separate, real engineering project — not a doc fix.
10. **`service_openapi.yaml` freshness** — wasn't touched in this pass; worth confirming it's still an accurate export of the live API's `/openapi.json` before publishing, since API routes/schemas can drift independently of the docs site.
