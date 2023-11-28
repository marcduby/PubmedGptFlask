


select gene_code, abstract from gene_abstract where gene_code = 'TSKU';




select gene_code, abstract, pubmed_count from gene_abstract where gene_code in ('TSKU') order by pubmed_count desc
