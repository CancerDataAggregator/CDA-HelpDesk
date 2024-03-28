---
title:  Search made simple
comments: true
---

<div class="center" markdown> <p>With CDA you search by harmonized, common language terms. Using simple language you can get information about the subjects, files, or specimens that you care about in a standard dataframe format (tsv) that you can open in Excel, integrate into a pipeline or upload to your favorite cloud resource.</p></div>


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Don't code? No problem!__

    ---

    Browse through a curated dataset of all subjects that have data at multiple data centers using an intuitive filtering tool right in this website. 
<a href="../interactive/" title="interactive search" class="md-button md-button">Head to our interactive page to try it out.
</a></p>

-   :material-clock-fast:{ .lg .middle } __Low code, no install__

    ---

    Fill in the blanks in our pre-built queries to find the data you need without installing a thing. <p>Send your results to [Broad Institute FireCloud:octicons-link-external-16:](https://datacommons.cancer.gov/analytical-resource/broad-institute-firecloud){:target="_blank"} or [Velsera Cancer Genomics Cloud:octicons-link-external-16:](https://www.cancergenomicscloud.org/){:target="_blank"} for a complete cloud experience. Find the data you need, fetch all the files, and run your favorite bioinformatics pipeline *all without ever leaving your web browser.*<p>
<a href="https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Welcome.ipynb" title="Try it now" class="md-button md-button">Launch CDA in the cloud
</a></p>

-   :fontawesome-brands-python:{ .lg .middle } __Power users__

    ---

    Install `cdapython` with `pip` and get up
    and running in no time

    ```bash
    pip install cdapython
    python3
    ```

    ```python
    from cdapython import tables, columns, column_values, fetch_rows, summary_counts
    ```

-   :simple-swagger:{ .lg .middle } __Developers__

    ---

    Are you building a metadata micro-service? Connecting even more databases? Hosting a computational resource? <p>Whatever your use case, CDA can help.

    [:octicons-arrow-right-24:**swagger documentation**](../documentation/developers/index.md)

-   :simple-mysql:{ .lg .middle } __Need even more data?__

    ---

    Do you dream of having a CDA database instance of your very own? Or CDA but bigger somehow?
    We can make those dreams come true. Lets chat!

    :material-email: cancerdataaggregator `@` gmail

</div>

