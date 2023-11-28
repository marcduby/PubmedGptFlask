# imports
from flask import Flask, render_template, request, flash
from sql_utils import get_connection, get_list_abstracts
import ml_utils

app = Flask(__name__)
app.secret_key = "test_app_gpt"

@app.route("/genes")
def index():
    return render_template("index.html")


@app.route("/submit_genes", methods=["POST","GET"])
def submit_genes():
    # initialize 
    list_genes = []
    list_genes_missing = []
    list_temp = []
    list_abstracts = []
    abstract_gpt = "no abstract"
    prompt_gpt = "no prompt"

    # get the input
    input_genes = str(request.form["input_gene_set"])

    # split the genes into list
    if input_genes:
        list_temp = input_genes.split(",")
        list_select = []

        # for each entry, strip spaces, search for gene search, get final abstract
        for value in list_temp:
            gene = value.strip()
            print("got gene: -{}-".format(gene))
            list_select.append(gene)

            # TODO get the abstract from the DB
            abstract = None

            if abstract:
                list_genes.append(gene)
                list_abstracts.append(abstract)

            else:
                list_genes_missing.append(gene)

        # get the data
        conn = get_connection()
        list_abstracts = get_list_abstracts(conn=conn, list_genes=list_select, log=True)

        if list_abstracts and len(list_abstracts) > 0:
            # build the inputs for the LLM call
            list_gene_llm = []
            list_abstract_llm = []

            for item in list_abstracts:
                list_gene_llm.append(item.get('gene'))
                list_abstract_llm.append(item.get('abstract'))
            
            # build the prompt inputs
            str_gene = ",".join(list_gene_llm)
            str_abstract = "\n".join(list_abstract_llm)

            print("got genes: {}".format(str_gene))
            print("\ngot abstracts: {}".format(str_abstract))

            # call the LLM
            str_chat = ml_utils.call_llm(prompt_template=ml_utils.PROMPT_BIOLOGY, str_gene=str_gene, str_abstract=str_abstract, log=True)
            print("got LLM result: \n{}".format(str_chat))


    else:
        print("no input genes")

    # add data for return 
    flash(list_genes, 'list_genes')
    flash(list_genes_missing, 'list_missing')
    flash(prompt_gpt, 'prompt')
    flash(abstract_gpt, 'abstract')

    return render_template("index.html")

