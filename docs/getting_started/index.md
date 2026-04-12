---
title:  Re-Search made simple
---
# Find the Cancer Data You Need—No Coding Required

The **Cancer Data Aggregator (CDA)** connects you to subjects, files, and specimens across **GDC**, **PDC**, and **IDC** through one simple interface. Filter by common clinical terms and export results directly to Excel or the Cloud.

!!! abstract "Start Here"
    If you want to browse data visually without writing any code, our interactive tool is the best place to begin.
    
    [🚀 Start Searching Interactively](https://cda.readthedocs.io/en/latest/interactive_search.html){ .md-button .md-button--primary }
    *(No installation or account needed)*

---

## Choose Your Research Path

Whether you prefer a visual interface, cloud-based notebooks, or a full Python environment, the CDA meets you where you are.

=== "No Code (Interactive)"

    ### Explore Data Visually
    Perfect for clinical researchers and building cohorts quickly.
    
    * **No Install:** Works entirely in your browser.
    * **Intuitive Filtering:** Search by harmonized terms (age, diagnosis, project).
    * **Export:** Download your cohort as a `.tsv` to open in Excel.

    [Try the Interactive Search →](https://cda.readthedocs.io/en/latest/interactive_search.html){ .md-button }

=== "Low Code (Cloud)"

    ### Analyze in the Cloud
    Fill in the blanks in our pre-built queries to find and process data without local setup.
    
    * **Connected:** Send results directly to [Broad Institute FireCloud](https://cda.readthedocs.io/en/latest/) or [Velsera Cancer Genomics Cloud](https://cda.readthedocs.io/en/latest/).
    * **Scalable:** Run bioinformatics pipelines on the data you find without leaving your browser.

    [Launch CDA in the Cloud →](https://cda.readthedocs.io/en/latest/#low-code-no-install){ .md-button }

=== "Power Users (Python)"

    ### Integrate with Python
    For bioinformaticians building automated pipelines.
    
    ```bash
    pip install cdapython
    ```

    ```python
    from cdapython import Q
    # Example: Find subjects with specific diagnosis
    r = Q('primary_diagnosis = "Adenocarcinoma"').run()
    print(r)
    ```

    [View Developer Tools →](https://cda.readthedocs.io/en/latest/developer_tools.html){ .md-button }

---

## Master the CDA in Minutes

Check out our video guides to see how the CDA simplifies complex data cross-referencing.

* [📺 Video: Intro to CDA](https://cda.readthedocs.io/en/latest/vignettes/video_intro.html)
* [📺 Video: Build a Cohort Interactively](https://cda.readthedocs.io/en/latest/vignettes/video_build_a_cohort_interactively.html)
* [📺 Video: Cohort Building with Python](https://cda.readthedocs.io/en/latest/vignettes/video_cohort_building_with_cdapython.html)

---

## Why Use the CDA?

| Feature | The CDA Advantage |
| :--- | :--- |
| **Harmonization** | We translate different data center terms into one common language. |
| **Cross-Center** | Find subjects that have data in GDC, PDC, and IDC simultaneously. |
| **Versatility** | Move from a simple search to a massive cloud pipeline in the same ecosystem. |

---

### Stay Updated
* [Latest Data Releases](https://cda.readthedocs.io/en/latest/)
* [CDA Python Library Updates](https://cda.readthedocs.io/en/latest/release_notes/cdapython_releases.html)

---
[Back to top]
