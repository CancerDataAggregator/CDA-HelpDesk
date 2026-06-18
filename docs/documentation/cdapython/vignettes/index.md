
You can think of the CDA as a really, really enormous spreadsheet full of data. To search this enormous spreadsheet, you'd want to select columns that have data you're interested in, and then filter the rows to only the values you care about. 

<div class="cdanote" style="background-color:#b3e5d5;color:black;padding:20px;">
    
CDA data comes from six sources:
<ul>
<li><b>The <a href="https://proteomic.datacommons.cancer.gov/pdc/"> Proteomic Data Commons</a> (PDC)</b></li>
<li><b>The <a href="https://gdc.cancer.gov/">Genomic Data Commons</a> (GDC)</b></li>
<li><b>The <a href="https://datacommons.cancer.gov/repository/imaging-data-commons">Imaging Data Commons</a> (IDC)</b></li>
<li><b>The <a href="https://general.datacommons.cancer.gov/#/">General Commons</a> (GC)</b></li>
<li><b>The <a href="https://caninecommons.cancer.gov/#/explore">Integrated Canine Data Commons</a> (ICDC)</b></li>
<li><b>The <a href="https://www.isb-cgc.org/">ISB Cancer Gateway in the Cloud</a> (ISB-CGC)</b></li>
</ul> 
    
The CDA makes this data searchable in two main endpoints:

<ul>
<li><b>subject:</b> A patient entity captures the study-independent metadata for research subjects. Human research subjects are usually not traceable to a particular person to protect the subjects privacy.</li>

<li><b>file:</b> A unit of data about subjects, researchsubjects, specimens, or their associated information.</li>

</ul>
</div>

If you are looking to build a cohort of distinct individuals who meet some criteria, you would search using `get_subject_data`, and the result will be a table of information with one row per subject, then use the `add_columns` feature inside of `get_subject_data` to add on extra information.
