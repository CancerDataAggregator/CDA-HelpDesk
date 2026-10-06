---
title:  Re-Search made simple
---

<div class="center" markdown>

# Cancer Data Aggregator

<p style="font-size: 1.1rem; max-width: 640px; margin: 0 auto 8px;">Think of CDA as one really, really enormous spreadsheet spanning six cancer data centers — GDC, PDC, IDC, GC, ICDC, and CTDC. Search by harmonized, common-language terms and get results back in a standard dataframe (or TSV) you can open in Excel, feed into a pipeline, or send to your favorite cloud resource.</p>

<p style="max-width: 640px; margin: 0 auto 24px;">No matter your coding comfort — from zero code to full API access — there's a way in.</p>

<a href="getting_started/" title="Getting started" class="md-button md-button--primary">Get started →</a>

</div>

{{ release_status_table() }}

<div class="cdanote" style="background-color:#fff3cd;color:black;padding:20px;margin-top:24px;">

<b>A note on mutation data and ISB-CGC:</b> the <a href="https://www.isb-cgc.org/">ISB Cancer Gateway in the Cloud</a> (ISB-CGC) is not one of CDA's six data sources, but it has a two-way relationship with CDA. <b>Upstream</b>, all mutation data in CDA comes from GDC via ISB-CGC's aggregation pipeline, which combines GDC's per-individual VCF files into a single harmonized, searchable dataset. <b>Downstream</b>, ISB-CGC also consumes CDA's non-mutation phenotypic data and incorporates it into their own search tools. See <a href="./about_us/ourdata.md">our data sources</a> page for more detail.

</div>
