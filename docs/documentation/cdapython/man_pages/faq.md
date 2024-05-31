title: Frequently Asked Questions
---

## CDA Python Usage

### 1. Why do I get different answers if I switch which table is the 'table' and which is linked? For example, why do these two queries give different answers? And which one is correct?

`fetch_rows(table='subject', link_to_table='file', match_all=['subject_id = "TCGA.TCGA-E2-A10A"'])`

`fetch_rows(table='file', link_to_table='subject', match_all=['subject_id = "TCGA.TCGA-E2-A10A"'])`

Whatever you input as the "table" is a declaration of what kind of information you want returned. If you want subject data, you would use the first code snippet, if you want file data you would want the second one. Whatever you list as "link_to_table" is information you want joined/appended to your search after the search is done.

So, in the first instance, you will get back your one subject ID and all the files associated with that one subject. In the second instance, you will get back all of the files that match that subject ID, and then all the subject info associated with those files.

In some instances, those two returned dataframes will be exactly the same.

In other instances, the two dataframes will be wildly different. 

The difference is because many files at CDA are aggregated files, like GWAS data or VCFs. There can be hundreds or thousands of subjects associated with one GWAS file.

Let's say we have two subjects, Bob and Jane. Each of these subjects have exactly 10 files associated with them.

Bob has 10 records of doctors visits. Each one is exclusively about him. In that case these two searches will give exactly the same results:

```
fetch_rows(table='subject', link_to_table='file', match_all=['subject_id = "Bob"'])
fetch_rows(table='file', link_to_table='subject', match_all=['subject_id = "Bob"'])
```

Jane has 9 records of doctors visits, and one GWAS file. That GWAS file has results that include Jane, and 100 other subjects. 

The query `fetch_rows(table='subject', link_to_table='file', match_all=['subject_id = "Jane"'])` will search for Jane in the subject table to get her subject information, and then join that to her files. This will result in 10 rows of data, with Janes subject info repeated for each one.

The query `fetch_rows(table='file', link_to_table='subject', match_all=['subject_id = "Jane"'])` will search for Jane in the file table, to get all of the information for files she is part of. Then it will join those files to their subjects. This will return 109 rows of data: 10 with Janes subject information, and 99 with the subject information for the 99 other subjects that share her GWAS file.

Both of these results are correct, in that they give back true information, but which you should use depends on your use case. If you really just care about Jane, then you should search by subject and join other tables to that. If you want to replicate some analysis that Jane was part of, you'll need the data for all of the other subjects as well, and would search by file, then join to subject.

### 2. How do I merge/join together data from multiple searches?

This depends on both what data you're joining. 

#### join two tables
If you just want to join any two tables, cda-python will do that for you:

`fetch_rows(table='subject', link_to_table='diagnosis')` will return a joint table of subject and diagnosis data, put any two table names in, and whatever search terms you want to add to get your desired result.

Similarly, if you just want to get data about where we got the data, you can have cda-python add the provenance data to any table:

`fetch_rows(table='subject', provenance = True)` will return the subject table joined to a table of provenance info (original data center, IDs, etc)

#### join more than two tables

If you want to join information from more than two tables, you will need to do that outside of cda-python. We have constrained the number of automatic joins cda-python can provide because multi-table joins require more supervision to provide accurate answers. Depending on what specific data you have searched, it can be very easy to introduce false joins. However, supervised joins are relatively easy to do using Pandas. If you are joining three or more tables, we recommend running a search for the most specific table joined to each of your less specific tables in turn, and then using pandas to join in the appropriate directions using as many overlapping variables as possible. 
