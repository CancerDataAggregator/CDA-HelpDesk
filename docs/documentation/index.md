
You can think of the CDA as a really, really enormous spreadsheet full of data. To search this enormous spreadsheets, you'd want select columns that have data you're interested in, and then filter the rows to only the values you care about. 

<div class="cdanote" style="background-color:#b3e5d5;color:black;padding:20px;">
    
CDA data comes from four sources:
<ul>
<li><b>The <a href="https://proteomic.datacommons.cancer.gov/pdc/"> Proteomic Data Commons</a> (PDC)</b></li>
<li><b>The <a href="https://gdc.cancer.gov/">Genomic Data Commons</a> (GDC)</b></li>
<li><b>The <a href="https://datacommons.cancer.gov/repository/imaging-data-commons">Imaging Data Commons</a> (IDC)</b></li>
<li><b>The <a href="https://dataservice.datacommons.cancer.gov/#/home">Cancer Data Service</a> (CDS)</b></li> 
</ul> 
    
The CDA makes this data searchable in five main endpoints:

<ul>
<li><b>subject:</b> A patient entity captures the study-independent metadata for research subjects. Human research subjects are usually not traceable to a particular person to protect the subjects privacy.</li>
<li><b>researchsubject:</b> A research subject is the entity of interest in a specific research study or project, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subjects privacy. This entity plays the role of the case_id in existing data. A subject who participates in 3 studies will have 3 researchsubject IDs.</li>
<li><b>specimen:</b> Any material taken as a sample from a biological entity (living or dead), or from a physical object or the environment. Specimens are usually collected as an example of their kind, often for use in some investigation.</li>
<li><b>mutation:</b> Molecular data about specific mutations, currently limited to the TCGA-READ project from GDC.</li>
<li><b>file:</b> A unit of data about subjects, researchsubjects, specimens, or their associated information.</li>
</ul>
and two endpoints that offer deeper information about data in the researchsubject endpoint:
<ul>
<li><b>diagnosis:</b> A collection of characteristics that describe an abnormal condition of the body as assessed at a point in time. May be used to capture information about neoplastic and non-neoplastic conditions.</li>
<li><b>treatment:</b> Represent medication administration or other treatment types.</li>
</ul>
</div>


If the CDA works like a giant spreadsheet, the endpoints are sets of specific columns that always go together. Any metadata field can be searched from any endpoint, the only difference between search types is what type of data is returned by default. 

If you are looking to build a cohort of distinct individuals who meet some criteria, you would search by `subject`, and the result will be a table of information with one row per subject. If you are looking for biosamples that can be ordered or a specific format of information (for e.g. histological slides) start with `specimen`. This search will return a table of information with one row per biosample. If you want to build a cohort, but are particularly interested in studies rather than the participates per se, search by `researchsubject`. 