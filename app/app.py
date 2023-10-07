# imports
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "test_app_gpt"

@app.route("/genes")
def index():
    return render_template("index.html")


@app.route("/submit_genes", methods=["POST"])
def submit_genes():
    # initialize 
    list_genes = []
    list_genes_missing = []
    list_temp = []
    list_abstracts = []
    abstract_gpt = "no absract"
    prompt_gpt = "no prompt"

    # get the input
    input_genes = str(request.form["input_gene_set"])

    # split the genes into list
    if input_genes:
        list_temp = input_genes.split(",")

        # for each entry, strip spaces, search for gene search, get final abstract
        for value in list_temp:
            gene = value.strip()

            # TODO get the abstract from the DB
            abstract = None

            if abstract:
                list_genes.append(gene)
                list_abstracts.append(abstract)

            else:
                list_genes_missing.append(gene)


    else:
        print("no input genes")

    # add data for return 
    flash(list_genes, 'list_genes')
    flash(list_genes_missing, 'list_missing')
    flash(prompt_gpt, 'prompt')
    flash(abstract_gpt, 'abstract')

    return render_template("index.html")

