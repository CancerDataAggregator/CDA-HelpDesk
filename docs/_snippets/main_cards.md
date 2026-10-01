<!--
  Shared card grid — included by both docs/index.md and docs/getting_started/index.md
  via pymdownx.snippets. Edit ONLY this file; both pages will pick up changes automatically.

  Link paths below are written relative to docs/getting_started/index.md (the deeper file).
  Since docs/index.md sits one level up, pymdownx.snippets does NOT auto-adjust relative
  links for you -- if a link breaks on the root index page after this change, that's why.
  Fix: either use paths relative to docs/ root here and adjust getting_started/index.md's
  version separately, or use MkDocs absolute-from-docs-root paths (leading slash) instead
  of relative ones, which resolve the same regardless of which page includes this file.
-->

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Don't code? No problem!__

    ---

    Browse through a curated dataset of all subjects that have data at multiple data centers using an intuitive filtering tool right in this website.

    <a href="/interactive/" title="interactive search" class="md-button md-button">Head to our interactive page to try it out.</a>

-   :material-clock-fast:{ .lg .middle } __Low code, no install__

    ---

    Fill in the blanks in our pre-built queries to find the data you need without installing a thing.

    <p>Send your results to <a href="https://datacommons.cancer.gov/analytical-resource/broad-institute-firecloud" target="_blank">Broad Institute FireCloud <span class="twemoji"></span></a> or <a href="https://www.cancergenomicscloud.org/" target="_blank">Velsera Cancer Genomics Cloud <span class="twemoji"></span></a> for a complete cloud experience. Find the data you need, fetch all the files, and run your favorite bioinformatics pipeline *all without ever leaving your web browser.*</p>

    <a href="https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Tutorials/Welcome.ipynb" title="Try it now" class="md-button md-button">Launch CDA in the cloud</a>

-   :fontawesome-brands-python:{ .lg .middle } __Power users__

    ---

    Install `cdapython` with `pip` and get up and running in no time

    ```bash
    pip3 uninstall -y cdapython; pip3 install git+https://github.com/CancerDataAggregator/cdapython.git@develop
    python3
    ```
    ```python
    from cdapython import *
    ```

-   :fontawesome-brands-python:{ .lg .middle } __Code in the Cloud__

    ---

    Bring lists of files or subjects found with CDA to the <a href="https://isb-cgc.org/" target="_blank">ISB Cancer Gateway in the Cloud (ISB-CGC) <span class="twemoji"></span></a> to instantly access both associated derived data and raw files, for use in cloud processing pipelines -- either in your own preferred environment or using ISB-CGC's free Google Cloud Platform credits program.

    <a href="https://colab.research.google.com/github/CancerDataAggregator/Community-Notebooks/blob/main/Tutorials/010_isbcgc.ipynb" title="isbcgcusecase" class="md-button md-button">Test it out on Google Colab</a>

-   :simple-swagger:{ .lg .middle } __Developers__

    ---

    Are you building a metadata microservice? Connecting even more databases? Hosting a computational resource?

    <p>Whatever your use case, CDA can help.</p>

    [:octicons-arrow-right-24: __API documentation__](/documentation/developers/)

</div>
