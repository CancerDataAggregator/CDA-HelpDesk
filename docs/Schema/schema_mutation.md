---
title: Mutation schema
---

The **mutation** entity is a stand alone endpoint that is not yet harmonized with other CDA endpoints. Within the **mutation** record are data from TCGA tumor mutation studies.

You can download this JSON directly on our [Github page.](https://raw.githubusercontent.com/CancerDataAggregator/readthedocs/main/docs/Schema/schema_mutation.md)


Use the "+" and "-" icons to expand and collapse sections of the schema.

<div class="container">
<div id="test">

<script type="text/javascript" src="../../javascripts/renderjson.js"></script>
<script>
renderjson.set_show_to_level(2).set_icons('+', '-');


var example = [
    {
        "name": "AA_MAF",
        "description": "Non-reference allele and frequency of existing variant in NHLBI-ESP African American population",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "AFR_MAF",
        "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined African population",
        "mode": "NULLABLE",
        "type": "FLOAT"
    },
    {
        "name": "ALLELE_NUM",
        "description": "Allele number from input; 0 is reference, 1 is first alternate etc.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "AMR_MAF",
        "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined American population",
        "mode": "NULLABLE",
        "type": "FLOAT"
    },
    {
        "name": "Allele",
        "description": "The variant allele used to calculate the consequence",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Amino_acids",
        "description": "Amino acid substitution caused by the mutation. Only given if the variation affects the protein-coding sequence",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "BIOTYPE",
        "description": "Biotype of transcript",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "CANONICAL",
        "description": "A flag (YES) indicating that the VEP-based canonical transcript, the longest translation, was used for this gene. If not, the value is null",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "CCDS",
        "description": "The  CCDS identifier for this transcript, where applicable",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "CDS_position",
        "description": "Relative position of base pair in coding sequence. A - symbol is displayed as the numerator if the variant does not appear in coding sequence",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "CLIN_SIG",
        "description": "Clinical significance of variant from dbSNP",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "CONTEXT",
        "description": "The reference allele per VCF specs, and its five flanking base pairs",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "COSMIC",
        "description": "Overlapping COSMIC variants",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Center",
        "description": "One or more genome sequencing center reporting the variant",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Chromosome",
        "description": "Chromosome, possible values: chr1-22, and chrX",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Codons",
        "description": "The alternative codons with the variant base in upper case",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Consequence",
        "description": "Consequence type of this variant; sequence ontology terms",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "DISTANCE",
        "description": "Shortest distance from the variant to transcript",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "DOMAINS",
        "description": "The source and identifier of any overlapping protein domains",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "EAS_MAF",
        "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined East Asian population",
        "mode": "NULLABLE",
        "type": "FLOAT"
    },
    {
        "name": "EA_MAF",
        "description": "Non-reference allele and frequency of existing variant in NHLBI-ESP European American population",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ENSP",
        "description": "The Ensembl protein identifier of the affected transcript",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "EUR_MAF",
        "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined European population",
        "mode": "NULLABLE",
        "type": "FLOAT"
    },
    {
        "name": "EXON",
        "description": "The exon number (out of total number)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "End_Position",
        "description": "Highest numeric genomic position of the reported variant on the genomic reference sequence. Mutation end coordinate",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "Entrez_Gene_Id",
        "description": "Entrez gene ID (an integer). 0 is used for regions that do not correspond to a gene region or Ensembl ID",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "ExAC_AF",
        "description": "Global Allele Frequency from   ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_AFR",
        "description": "African/African American Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_AMR",
        "description": "American Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_Adj",
        "description": "Adjusted Global Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_EAS",
        "description": "East Asian Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_FIN",
        "description": "Finnish Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_NFE",
        "description": "Non-Finnish European Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_OTH",
        "description": "Other Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "ExAC_AF_SAS",
        "description": "South Asian Allele Frequency from ExAC",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Existing_variation",
        "description": "Known identifier of existing variation",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Exon_Number",
        "description": "The exon number (out of total number)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "FILTER",
        "description": "Copied from input VCF. This includes filters implemented directly by the variant caller and other external software used in the DNA-Seq pipeline. See below for additional details.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Feature",
        "description": "Stable Ensembl ID of feature (transcript, regulatory, motif)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Feature_type",
        "description": "Type of feature. Currently one of Transcript, RegulatoryFeature, MotifFeature (or blank)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "GDC_FILTER",
        "description": "GDC filters applied universally across all MAFs",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "GDC_Validation_Status",
        "description": "GDC implementation of validation checks. See notes section (#5) below for details",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "GMAF",
        "description": "Non-reference allele and frequency of existing variant in   1000 Genomes",
        "mode": "NULLABLE",
        "type": "FLOAT"
    },
    {
        "name": "Gene",
        "description": "The gene symbol. In this table, gene symbol is gene name e.g. ACADVL",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "HGNC_ID",
        "description": "Gene identifier from the HUGO Gene Nomenclature Committee if applicable",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "HGVS_OFFSET",
        "description": "Indicates by how many bases the HGVS notations for this variant have been shifted",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "HGVSc",
        "description": "The coding sequence of the variant in HGVS recommended format",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "HGVSp",
        "description": "The protein sequence of the variant in HGVS recommended format. p.= signifies no change in the protein",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "HGVSp_Short",
        "description": "Same as the HGVSp column, but using 1-letter amino-acid codes",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Hugo_Symbol",
        "description": "HUGO symbol for the gene (HUGO symbols are always in all caps). Unknown is used for regions that do not correspond to a gene",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "IMPACT",
        "description": "The impact modifier for the consequence type",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "INTRON",
        "description": "The intron number (out of total number)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "MC3_Overlap",
        "description": "Indicates whether this region overlaps with an MC3 variant for the same sample pair",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "MINIMISED",
        "description": "Alleles in this variant have been converted to minimal representation before consequence calculation (1 or null)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Matched_Norm_Sample_UUID",
        "description": "Unique GDC identifier for normal aliquot (10189 unique)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Mutation_Status",
        "description": "An assessment of the mutation as somatic, germline, LOH, post transcriptional modification, unknown, or none. The values allowed in this field are constrained by the value in the Validation_Status field",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "NCBI_Build",
        "description": "The reference genome used for the alignment (GRCh38)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "One_Consequence",
        "description": "The single consequence of the canonical transcript in  sequence ontology terms, eg missense_variant",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "PHENO",
        "description": "Indicates if existing variant is associated with a phenotype, disease or trait (0, 1, or null)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "PICK",
        "description": "Indicates if this block of consequence data was picked by VEP's   pick feature (1 or null)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "PUBMED",
        "description": "Pubmed ID(s) of publications that cite existing variant",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "PolyPhen",
        "description": "The PolyPhen prediction and/or score",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Protein_position",
        "description": "Relative position of affected amino acid in protein. A - symbol is displayed as the numerator if the variant does not appear in coding sequence",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "RefSeq",
        "description": "RefSeq identifier for this transcript",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Reference_Allele",
        "description": "The plus strand reference allele at this position. Includes the deleted sequence for a deletion or - for an insertion",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "SAS_MAF",
        "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined South Asian population",
        "mode": "NULLABLE",
        "type": "FLOAT"
    },
    {
        "name": "SIFT",
        "description": "The   SIFT prediction and/or score, with both given as prediction (score)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "SOMATIC",
        "description": "Somatic status of each ID reported under Existing_variation (0, 1, or null)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "SWISSPROT",
        "description": "UniProtKB/Swiss-Prot accession",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "SYMBOL",
        "description": "Eg TP53, LRP1B, etc (same as Hugo_Symbol field except blank instead of Unknown",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "SYMBOL_SOURCE",
        "description": "The source of the gene symbol, usually HGNC, rarely blank, other sources include Uniprot_gn, EntrezGene, etc",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Sequencer",
        "description": "Instrument used to produce primary sequence data",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Start_Position",
        "description": "Lowest numeric position of the reported variant on the genomic reference sequence. Mutation start coordinate",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "Strand",
        "description": "Either + or - to denote whether read mapped to the sense (+) or anti-sense (-) strand",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "TRANSCRIPT_STRAND",
        "description": "The DNA strand (1 or -1) on which the transcript/feature lies",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "TREMBL",
        "description": "UniProtKB/TrEMBL identifier of protein product",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "TSL",
        "description": "Transcript support level, which is based on independent RNA analyses",
        "mode": "NULLABLE",
        "type": "INTEGER"
    },
    {
        "name": "Transcript_ID",
        "description": "Ensembl ID of the transcript affected by the variant",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Tumor_Sample_UUID",
        "description": "Unique GDC identifier for tumor aliquot (10189 unique)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Tumor_Seq_Allele1",
        "description": "Primary data genotype for tumor sequencing (discovery) allele 1. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Tumor_Seq_Allele2",
        "description": "Primary data genotype for tumor sequencing (discovery) allele 2. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Tumor_Validation_Allele1",
        "description": "Secondary data from orthogonal technology. Tumor genotyping (validation) for allele 1. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Tumor_Validation_Allele2",
        "description": "Secondary data from orthogonal technology. Tumor genotyping (validation) for allele 2",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "UNIPARC",
        "description": "UniParc identifier of protein product",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "VARIANT_CLASS",
        "description": "Sequence Ontology variant class",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Validation_Method",
        "description": "The assay platforms used for the validation call",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Variant_Classification",
        "description": "Translational effect of variant allele",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "Variant_Type",
        "description": "Type of mutation. TNP (tri-nucleotide polymorphism) is analogous to DNP (di-nucleotide polymorphism) but for three consecutive nucleotides. ONP (oligo-nucleotide polymorphism) is analogous to TNP but for consecutive runs of four or more (SNP, DNP, TNP, ONP, INS, DEL, or Consolidated)",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "aliquot_barcode_normal",
        "description": "TCGA aliquot barcode for the normal control, eg TCGA-12-1089-01A-01D-0517-01",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "aliquot_barcode_tumor",
        "description": "TCGA aliquot barcode for the tumor, eg TCGA-12-1089-01A-01D-0517-01",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "all_effects",
        "description": "A semicolon delimited list of all possible variant effects, sorted by priority ([Symbol,Consequence,HGVSp_Short,Transcript_ID,RefSeq,HGVSc,Impact,Canonical,Sift,PolyPhen,Strand])",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "cDNA_position",
        "description": "Relative position of base pair in the cDNA sequence as a fraction. A - symbol is displayed as the numerator if the variant does not appear in cDNA",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "callerName",
        "description": "|-delimited list of mutation caller(s) that agreed on this particular call, always in alphabetical order: muse, mutect, somaticsniper, varscan",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "case_barcode",
        "description": "Original TCGA case barcode, eg TCGA-DX-A8BN",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "case_id",
        "description": "Unique GDC identifier for the underlying case",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "dbSNP_RS",
        "description": "The rs-IDs from the   dbSNP database, novel if not found in any database used, or null if there is no dbSNP record, but it is found in other databases",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "dbSNP_Val_Status",
        "description": "The dbSNP validation status is reported as a semicolon-separated list of statuses. The union of all rs-IDs is taken when there are multiple",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "fileName",
        "description": "|-delimited list of name of underlying MAF file",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "fileUUID",
        "description": "|-delimited list of unique GDC identifiers for underlying MAF file",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "n_depth",
        "description": "Read depth across this locus in normal BAM",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "normal_bam_uuid",
        "description": "Unique GDC identifier for the underlying normal bam file",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "project_short_name",
        "description": "Project name abbreviation; the program name appended with a project name abbreviation; eg. TCGA-OV, etc.",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "sample_barcode_normal",
        "description": "TCGA sample barcode for the normal control, eg TCGA-12-1089-01A. One sample may have multiple sets of CN segmentations corresponding to multiple aliquots; use GROUP BY appropriately in queries",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "sample_barcode_tumor",
        "description": "TCGA sample barcode for the tumor, eg TCGA-12-1089-01A. One sample may have multiple sets of CN segmentations corresponding to multiple aliquots; use GROUP BY appropriately in queries",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "src_vcf_id",
        "description": "|-delimited list of GDC VCF file identifiers",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "t_alt_count",
        "description": "Read depth supporting the variant allele in tumor BAM",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "t_depth",
        "description": "Read depth across this locus in tumor BAM",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "t_ref_count",
        "description": "Read depth supporting the reference allele in tumor BAM",
        "mode": "NULLABLE",
        "type": "STRING"
    },
    {
        "name": "tumor_bam_uuid",
        "description": "Unique GDC identifier for the underlying bam file",
        "mode": "NULLABLE",
        "type": "STRING"
    }
];
    document.getElementById("test").appendChild(renderjson(example));
</script>
</div></div>
