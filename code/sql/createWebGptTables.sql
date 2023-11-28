

drop table if exists web_gpt.gene_abstract;
create table web_gpt.gene_abstract as
select abstract.id as id, abstract.title as title, abstract.abstract as abstract, abstract.date_created as date_created, 
    abstract.gpt_run_id as gpt_run_id, search.id as search_id, search.gene as gene_code, search.pubmed_count as pubmed_count
from gene_gpt.pgpt_paper_abstract abstract, gene_gpt.pgpt_search search 
where abstract.search_top_level_of = search.id and abstract.gpt_run_id = 8;


create table web_gpt.fat_cell_gene as
select path.id, path.pathway_code, path_genes.id as gene_id, path_genes.gene_code
from data_pathway path, data_pathway_genes as path_genes 
where path.id = path_genes.pathway_id and path.pathway_code = 'GOBP_FAT_CELL_DIFFERENTIATION'
order by path_genes.gene_code;


select gpt.gene_code, gpt.pubmed_count
from gene_abstract gpt, fat_cell_gene fat_cell
where gpt.gene_code = fat_cell.gene_code
order by gpt.pubmed_count desc limit 20;


-- scratch
select abstract.id as id, abstract.title as title, abstract.abstract as abstract, abstract.date_created as date_created, 
    abstract.gpt_run_id as gpt_run_id, search.id as search_id, search.gene as gene_code
from gene_gpt.pgpt_paper_abstract abstract, gene_gpt.pgpt_search search 
where abstract.search_top_level_of = search.id and abstract.gpt_run_id = 8;


-- scratch pathway
select path.id, path.pathway_code, path_genes.id, path_genes.gene_code
from data_pathway path, data_pathway_genes as path_genes 
where path.id = path_genes.pathway_id and path.pathway_code = 'GOBP_FAT_CELL_DIFFERENTIATION'
order by path_genes.gene_code;

select path.id, path.pathway_code, path_genes.id, path_genes.gene_code
from data_pathway path, data_pathway_genes as path_genes 
where path.id = path_genes.pathway_id and path_genes.gene_code = 'PPARG'
order by path.pathway_code;


select path.id, path.pathway_code, path_genes.id, path_genes.gene_code
from data_pathway path, data_pathway_genes as path_genes 
where path.id = path_genes.pathway_id and path.pathway_code = 'GOBP_FAT_CELL_DIFFERENTIATION'
order by path_genes.gene_code;

select path.id, path.pathway_code, path_genes.id, path_genes.gene_code
from data_pathway path, data_pathway_genes as path_genes 
where path.id = path_genes.pathway_id and path_genes.gene_code = 'PPARG'
order by path.pathway_code;





