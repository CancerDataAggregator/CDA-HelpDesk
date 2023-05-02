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
[
  {
    "name": "project_short_name",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Project name abbreviation; the program name appended with a project name abbreviation; eg. TCGA-OV, etc.",
    "fields": []
  },
  {
    "name": "case_barcode",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Original case barcode, eg TCGA-DX-A8BN",
    "fields": []
  },
  {
    "name": "cda_subject_id",
    "mode": "REQUIRED",
    "type": "STRING",
    "description": "CDA subject ID corresponding to value in case_barcode",
    "fields": []
  },
  {
    "name": "primary_site",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Anatomical site of the cancer under investigation or review",
    "fields": []
  },
  {
    "name": "Hugo_Symbol",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "HUGO symbol for the gene (HUGO symbols are always in all caps). Unknown is used for regions that do not correspond to a gene",
    "fields": []
  },
  {
    "name": "Entrez_Gene_Id",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Entrez gene ID (an integer). 0 is used for regions that do not correspond to a gene region or Ensembl ID",
    "fields": []
  },
  {
    "name": "Center",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "One or more genome sequencing center reporting the variant",
    "fields": []
  },
  {
    "name": "NCBI_Build",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The reference genome used for the alignment (GRCh38)",
    "fields": []
  },
  {
    "name": "Chromosome",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Chromosome, possible values: chr1-22, and chrX",
    "fields": []
  },
  {
    "name": "Start_Position",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Lowest numeric position of the reported variant on the genomic reference sequence. Mutation start coordinate",
    "fields": []
  },
  {
    "name": "End_Position",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Highest numeric genomic position of the reported variant on the genomic reference sequence. Mutation end coordinate",
    "fields": []
  },
  {
    "name": "Strand",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Either + or - to denote whether read mapped to the sense (+) or anti-sense (-) strand",
    "fields": []
  },
  {
    "name": "Variant_Classification",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Translational effect of variant allele",
    "fields": []
  },
  {
    "name": "Variant_Type",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Type of mutation. TNP (tri-nucleotide polymorphism) is analogous to DNP (di-nucleotide polymorphism) but for three consecutive nucleotides. ONP (oligo-nucleotide polymorphism) is analogous to TNP but for consecutive runs of four or more (SNP, DNP, TNP, ONP, INS, DEL, or Consolidated)",
    "fields": []
  },
  {
    "name": "Reference_Allele",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The plus strand reference allele at this position. Includes the deleted sequence for a deletion or - for an insertion",
    "fields": []
  },
  {
    "name": "Tumor_Seq_Allele1",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Primary data genotype for tumor sequencing (discovery) allele 1. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases",
    "fields": []
  },
  {
    "name": "Tumor_Seq_Allele2",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Primary data genotype for tumor sequencing (discovery) allele 2. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases",
    "fields": []
  },
  {
    "name": "dbSNP_RS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The rs-IDs from the   dbSNP database, novel if not found in any database used, or null if there is no dbSNP record, but it is found in other databases",
    "fields": []
  },
  {
    "name": "dbSNP_Val_Status",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The dbSNP validation status is reported as a semicolon-separated list of statuses. The union of all rs-IDs is taken when there are multiple",
    "fields": []
  },
  {
    "name": "Tumor_Aliquot_Barcode",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Aliquot barcode for the tumor sample",
    "fields": []
  },
  {
    "name": "Matched_Norm_Aliquot_Barcode",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Aliquot barcode for the matched normal sample",
    "fields": []
  },
  {
    "name": "Match_Norm_Seq_Allele1",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Primary data genotype. Matched normal sequencing allele 1. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases (cleared in somatic MAF)",
    "fields": []
  },
  {
    "name": "Match_Norm_Seq_Allele2",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Matched normal sequencing allele 2",
    "fields": []
  },
  {
    "name": "Tumor_Validation_Allele1",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Secondary data from orthogonal technology. Tumor genotyping (validation) for allele 1. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases",
    "fields": []
  },
  {
    "name": "Tumor_Validation_Allele2",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Secondary data from orthogonal technology. Tumor genotyping (validation) for allele 2",
    "fields": []
  },
  {
    "name": "Match_Norm_Validation_Allele1",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Secondary data from orthogonal technology. Matched normal genotyping (validation) for allele 1. A - symbol for a deletion represents a variant. A - symbol for an insertion represents wild-type allele. Novel inserted sequence for insertion does not include flanking reference bases (cleared in somatic MAF)",
    "fields": []
  },
  {
    "name": "Match_Norm_Validation_Allele2",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Secondary data from orthogonal technology. Matched normal genotyping (validation) for allele 2 (cleared in somatic MAF)",
    "fields": []
  },
  {
    "name": "Verification_Status",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Second pass results from independent attempt using same methods as primary data source. Generally reserved for 3730 Sanger Sequencing",
    "fields": []
  },
  {
    "name": "Validation_Status",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Second pass results from orthogonal technology",
    "fields": []
  },
  {
    "name": "Mutation_Status",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "An assessment of the mutation as somatic, germline, LOH, post transcriptional modification, unknown, or none. The values allowed in this field are constrained by the value in the Validation_Status field",
    "fields": []
  },
  {
    "name": "Sequencing_Phase",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "TCGA sequencing phase (if applicable). Phase should change under any circumstance that the targets under consideration change",
    "fields": []
  },
  {
    "name": "Sequence_Source",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Molecular assay type used to produce the analytes used for sequencing. Allowed values are a subset of the SRA 1.5 library_strategy field values. This subset matches those used at CGHub",
    "fields": []
  },
  {
    "name": "Validation_Method",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The assay platforms used for the validation call",
    "fields": []
  },
  {
    "name": "Score",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Not in use",
    "fields": []
  },
  {
    "name": "BAM_File",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Not in use",
    "fields": []
  },
  {
    "name": "Sequencer",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Instrument used to produce primary sequence data",
    "fields": []
  },
  {
    "name": "Tumor_Aliquot_UUID",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Unique GDC identifier for tumor aliquot (10189 unique)",
    "fields": []
  },
  {
    "name": "Matched_Norm_Aliquot_UUID",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Unique GDC identifier for normal aliquot (10189 unique)",
    "fields": []
  },
  {
    "name": "HGVSc",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The coding sequence of the variant in HGVS recommended format",
    "fields": []
  },
  {
    "name": "HGVSp",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The protein sequence of the variant in HGVS recommended format. p.= signifies no change in the protein",
    "fields": []
  },
  {
    "name": "HGVSp_Short",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Same as the HGVSp column, but using 1-letter amino-acid codes",
    "fields": []
  },
  {
    "name": "Transcript_ID",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Ensembl ID of the transcript affected by the variant",
    "fields": []
  },
  {
    "name": "Exon_Number",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The exon number (out of total number)",
    "fields": []
  },
  {
    "name": "t_depth",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Read depth across this locus in tumor BAM",
    "fields": []
  },
  {
    "name": "t_ref_count",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Read depth supporting the reference allele in tumor BAM",
    "fields": []
  },
  {
    "name": "t_alt_count",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Read depth supporting the variant allele in tumor BAM",
    "fields": []
  },
  {
    "name": "n_depth",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": "Read depth across this locus in normal BAM",
    "fields": []
  },
  {
    "name": "n_ref_count",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Read depth supporting the reference allele in normal BAM (cleared in somatic MAF)",
    "fields": []
  },
  {
    "name": "n_alt_count",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Read depth supporting the variant allele in normal BAM (cleared in somatic MAF)",
    "fields": []
  },
  {
    "name": "all_effects",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "A semicolon delimited list of all possible variant effects, sorted by priority ([Symbol,Consequence,HGVSp_Short,Transcript_ID,RefSeq,HGVSc,Impact,Canonical,Sift,PolyPhen,Strand])",
    "fields": []
  },
  {
    "name": "Allele",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The variant allele used to calculate the consequence",
    "fields": []
  },
  {
    "name": "Gene",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The gene symbol. In this table, gene symbol is gene name e.g. ACADVL",
    "fields": []
  },
  {
    "name": "Feature",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Stable Ensembl ID of feature (transcript, regulatory, motif)",
    "fields": []
  },
  {
    "name": "Feature_type",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Type of feature. Currently one of Transcript, RegulatoryFeature, MotifFeature (or blank)",
    "fields": []
  },
  {
    "name": "One_Consequence",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The single consequence of the canonical transcript in  sequence ontology terms, eg missense_variant",
    "fields": []
  },
  {
    "name": "Consequence",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Consequence type of this variant; sequence ontology terms",
    "fields": []
  },
  {
    "name": "cDNA_position",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Relative position of base pair in the cDNA sequence as a fraction. A - symbol is displayed as the numerator if the variant does not appear in cDNA",
    "fields": []
  },
  {
    "name": "CDS_position",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Relative position of base pair in coding sequence. A - symbol is displayed as the numerator if the variant does not appear in coding sequence",
    "fields": []
  },
  {
    "name": "Protein_position",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Relative position of affected amino acid in protein. A - symbol is displayed as the numerator if the variant does not appear in coding sequence",
    "fields": []
  },
  {
    "name": "Amino_acids",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Amino acid substitution caused by the mutation. Only given if the variation affects the protein-coding sequence",
    "fields": []
  },
  {
    "name": "Codons",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The alternative codons with the variant base in upper case",
    "fields": []
  },
  {
    "name": "Existing_variation",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Known identifier of existing variation",
    "fields": []
  },
  {
    "name": "DISTANCE",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Shortest distance from the variant to transcript",
    "fields": []
  },
  {
    "name": "TRANSCRIPT_STRAND",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The DNA strand (1 or -1) on which the transcript/feature lies",
    "fields": []
  },
  {
    "name": "SYMBOL",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Eg TP53, LRP1B, etc (same as Hugo_Symbol field except blank instead of Unknown",
    "fields": []
  },
  {
    "name": "SYMBOL_SOURCE",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The source of the gene symbol, usually HGNC, rarely blank, other sources include Uniprot_gn, EntrezGene, etc",
    "fields": []
  },
  {
    "name": "HGNC_ID",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Gene identifier from the HUGO Gene Nomenclature Committee if applicable",
    "fields": []
  },
  {
    "name": "BIOTYPE",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Biotype of transcript",
    "fields": []
  },
  {
    "name": "CANONICAL",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "A flag (YES) indicating that the VEP-based canonical transcript, the longest translation, was used for this gene. If not, the value is null",
    "fields": []
  },
  {
    "name": "CCDS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The  CCDS identifier for this transcript, where applicable",
    "fields": []
  },
  {
    "name": "ENSP",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The Ensembl protein identifier of the affected transcript",
    "fields": []
  },
  {
    "name": "SWISSPROT",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "UniProtKB/Swiss-Prot accession",
    "fields": []
  },
  {
    "name": "TREMBL",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "UniProtKB/TrEMBL identifier of protein product",
    "fields": []
  },
  {
    "name": "UNIPARC",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "UniParc identifier of protein product",
    "fields": []
  },
  {
    "name": "UNIPROT_ISOFORM",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Direct mappings to UniProtKB isoforms",
    "fields": []
  },
  {
    "name": "RefSeq",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "RefSeq identifier for this transcript",
    "fields": []
  },
  {
    "name": "MANE",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "MANE (Matched Annotation by NCBI and EMBL-EBI) Transcript",
    "fields": []
  },
  {
    "name": "APPRIS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Annotates alternatively spliced transcripts as primary or alternate based on a range of computational methods",
    "fields": []
  },
  {
    "name": "FLAGS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Transcript quality flags",
    "fields": []
  },
  {
    "name": "SIFT",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The SIFT prediction and/or score, with both given as prediction (score)",
    "fields": []
  },
  {
    "name": "PolyPhen",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The PolyPhen prediction and/or score",
    "fields": []
  },
  {
    "name": "EXON",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The exon number (out of total number)",
    "fields": []
  },
  {
    "name": "INTRON",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The intron number (out of total number)",
    "fields": []
  },
  {
    "name": "DOMAINS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The source and identifier of any overlapping protein domains",
    "fields": []
  },
  {
    "name": "ThousG_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in 1000 Genomes",
    "fields": []
  },
  {
    "name": "ThousG_AFR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined African population",
    "fields": []
  },
  {
    "name": "ThousG_AMR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined American population",
    "fields": []
  },
  {
    "name": "ThousG_EAS_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined East Asian population",
    "fields": []
  },
  {
    "name": "ThousG_EUR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined European population",
    "fields": []
  },
  {
    "name": "ThousG_SAS_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in 1000 Genomes combined South Asian population",
    "fields": []
  },
  {
    "name": "ESP_AA_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in NHLBI-ESP African American population",
    "fields": []
  },
  {
    "name": "ESP_EA_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Non-reference allele and frequency of existing variant in NHLBI-ESP European American population",
    "fields": []
  },
  {
    "name": "gnomAD_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes combined population",
    "fields": []
  },
  {
    "name": "gnomAD_AFR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes African/American population",
    "fields": []
  },
  {
    "name": "gnomAD_AMR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes American population",
    "fields": []
  },
  {
    "name": "gnomAD_ASJ_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes Ashkenazi Jewish population",
    "fields": []
  },
  {
    "name": "gnomAD_EAS_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes East Asian population",
    "fields": []
  },
  {
    "name": "gnomAD_FIN_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes Finnish population",
    "fields": []
  },
  {
    "name": "gnomAD_NFE_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "tFrequency of existing variant in gnomAD exomes Non-Finnish European population",
    "fields": []
  },
  {
    "name": "gnomAD_OTH_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes other combined population",
    "fields": []
  },
  {
    "name": "gnomAD_SAS_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of existing variant in gnomAD exomes South Asian population",
    "fields": []
  },
  {
    "name": "MAX_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Maximum observed allele frequency in 1000 Genomes, ESP and ExAC/gnomAD",
    "fields": []
  },
  {
    "name": "MAX_AF_POPS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Populations in which maximum allele frequency was observed",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes combined non-cancer population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_AFR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer African/American population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_AMI_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Amish population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_AMR_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Latino population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_ASJ_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Ashkenazi Jewish population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_EAS_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer East Asian population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_FIN_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Finnish population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_MID_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Middle Eastern population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_NFE_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Non-Finnish European population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_OTH_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer Other population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_SAS_AF",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Frequency of exisiting variant in gnomAD genomes non-cancer South Asian population",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_MAX_AF_adj",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": "Maximum observed allele frequency in non-cancer gnomAD genomes populations after removing subpopulations with less than 2 allele counts",
    "fields": []
  },
  {
    "name": "gnomAD_non_cancer_MAX_AF_POPS_adj",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Non-cancer gnomAD genomes populations in which the maximum allele frequency was observed after removing those with less than 2 allele counts",
    "fields": []
  },
  {
    "name": "CLIN_SIG",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Clinical significance of variant from dbSNP",
    "fields": []
  },
  {
    "name": "SOMATIC",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Somatic status of each ID reported under Existing_variation (0, 1, or null)",
    "fields": []
  },
  {
    "name": "PUBMED",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Pubmed ID(s) of publications that cite existing variant",
    "fields": []
  },
  {
    "name": "TRANSCRIPTION_FACTORS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "List of transcription factors which bind to the transcription factor binding profile",
    "fields": []
  },
  {
    "name": "MOTIF_NAME",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The source and identifier of a transcription factor binding profile aligned at this position",
    "fields": []
  },
  {
    "name": "MOTIF_POS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The relative position of the variation in the aligned TFBP",
    "fields": []
  },
  {
    "name": "HIGH_INF_POS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "A flag indicating if the variant falls in a high information position of a transcription factor binding profile (TFBP) (Y, N, or null)",
    "fields": []
  },
  {
    "name": "MOTIF_SCORE_CHANGE",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The difference in motif score of the reference and variant sequences for the TFBP",
    "fields": []
  },
  {
    "name": "miRNA",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "SO terms of overlapped miRNA secondary structure feature(s)",
    "fields": []
  },
  {
    "name": "IMPACT",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The impact modifier for the consequence type",
    "fields": []
  },
  {
    "name": "PICK",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Indicates if this block of consequence data was picked by VEP's   pick feature (1 or null)",
    "fields": []
  },
  {
    "name": "VARIANT_CLASS",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Sequence Ontology variant class",
    "fields": []
  },
  {
    "name": "TSL",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Transcript support level, which is based on independent RNA analyses",
    "fields": []
  },
  {
    "name": "HGVS_OFFSET",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Indicates by how many bases the HGVS notations for this variant have been shifted",
    "fields": []
  },
  {
    "name": "PHENO",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Indicates if existing variant is associated with a phenotype, disease or trait (0, 1, or null)",
    "fields": []
  },
  {
    "name": "GENE_PHENO",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Indicates if gene that the variant maps to is associated with a phenotype, disease or trait (0, 1, or null)",
    "fields": []
  },
  {
    "name": "CONTEXT",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "The reference allele per VCF specs, and its five flanking base pairs",
    "fields": []
  },
  {
    "name": "tumor_submitter_uuid",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Unique GDC identifier for the tumor file submitter",
    "fields": []
  },
  {
    "name": "normal_submitter_uuid",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Unique GDC identifier for the normal file submitter",
    "fields": []
  },
  {
    "name": "case_id",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Unique GDC identifier for the underlying case",
    "fields": []
  },
  {
    "name": "GDC_FILTER",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "GDC filters applied universally across all MAFs",
    "fields": []
  },
  {
    "name": "COSMIC",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Overlapping COSMIC variants",
    "fields": []
  },
  {
    "name": "hotspot",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "description": "A flag indicating if the variant is a known hotspot (Y, N, or null)",
    "fields": []
  },
  {
    "name": "RNA_Support",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Indicates if the variant is found and alleles (Match), simply (Overlap), or is not supported (No) by tumor RNA-Seq. If it has not been checked against RNA-Seq data, the value will be 'Unknown'.",
    "fields": []
  },
  {
    "name": "RNA_depth",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Read depth at this locus if the variant is supported by tumor RNA-seq data.",
    "fields": []
  },
  {
    "name": "RNA_ref_count",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Read depth supporting the reference allele at this locus if the variant is supported by tumor RNA-seq data.",
    "fields": []
  },
  {
    "name": "RNA_alt_count",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Read depth supporting the variant allele at this locus if the variant is supported by tumor RNA-seq data.",
    "fields": []
  },
  {
    "name": "callers",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "|-delimited list of mutation caller(s) that agreed on this particular call, always in alphabetical order: muse, mutect, somaticsniper, varscan",
    "fields": []
  },
  {
    "name": "file_gdc_id",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "|-delimited list of unique GDC identifiers for underlying MAF file",
    "fields": []
  },
  {
    "name": "muse",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Muse caller identified the variant at this position",
    "fields": []
  },
  {
    "name": "mutect2",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Mutect2 caller identified the variant at this position",
    "fields": []
  },
  {
    "name": "pindel",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "pindel caller identified the variant at this position",
    "fields": []
  },
  {
    "name": "varscan2",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "Varscan2 caller identified the variant at this position",
    "fields": []
  },
  {
    "name": "sample_barcode_tumor",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "TCGA sample barcode for the tumor, eg TCGA-12-1089-01A. One sample may have multiple sets of CN segmentations corresponding to multiple aliquots; use GROUP BY appropriately in queries",
    "fields": []
  },
  {
    "name": "sample_barcode_normal",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "TCGA sample barcode for the normal control, eg TCGA-12-1089-01A. One sample may have multiple sets of CN segmentations corresponding to multiple aliquots; use GROUP BY appropriately in queries",
    "fields": []
  },
  {
    "name": "aliquot_barcode_tumor",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "TCGA aliquot barcode for the tumor, eg TCGA-12-1089-01A-01D-0517-01",
    "fields": []
  },
  {
    "name": "aliquot_barcode_normal",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": "TCGA aliquot barcode for the normal control, eg TCGA-12-1089-01A-01D-0517-01]",
    "fields": []
  }
]
];
    document.getElementById("test").appendChild(renderjson(example));
</script>
</div></div>
