
# imports
import os 
import openai
import json

# constants
KEY_CHATGPT = os.environ.get('CHAT_KEY')
openai.api_key = KEY_CHATGPT
MODEL_CHATGPT="gpt-3.5-turbo-0301"

# prompts
PROMPT_PATHWAYS = """
Below are the abstracts from different research papers on the genes {}. 
Please read through the abstracts and as a genetics researcher write a 200 word summary that synthesizes the key findings on the commonality of biological pathways of the genes {}
{}
"""

PROMPT_THERAPEUTICS = """
Below are the abstracts from different research papers on the genes {}. 
Please read through the abstracts and as a genetics researcher write a 200 word summary that synthesizes the key findings on possible therapeutics for diseases linked to the genes {}
{}
"""

PROMPT_BIOLOGY = """
Below are the biological research summaries on the genes {}. 
Please read through the summaries and as a genetics researcher write a 300 word summary that synthesizes the key findings on the common biology of the genes {}
{}
"""
# PROMPT_BIOLOGY = """
# Below are the abstracts from different research papers on the genes {}. 
# Please read through the abstracts and as a genetics researcher write a 200 word summary that synthesizes the key findings on the common biology of the genes {}
# {}
# """

# methods
def get_prompt(prompt_template, str_gene, str_abstract, log=False):
    '''
    build out the prompt
    '''
    # result = prompt.format({'genes': str_gene, 'abstracts': str_gene})
    result = prompt_template.format(str_gene, str_gene, str_abstract)

    # log
    if log:
        print("got prompt: {}".format(result))

    # return
    return result


def call_llm(prompt_template, str_gene, str_abstract, log=False):
    '''
    call chat gpt 
    '''
    # initialize
    str_chat = ""

    # get the prompt
    str_prompt = get_prompt(prompt_template=prompt_template, str_gene=str_gene, str_abstract=str_abstract, log=log)

    # get the result
    str_chat = call_chatgpt(str_query=str_prompt, log=True)

    # log
    if log:
        print("for genes: {}, got result: \n{}".format(str_gene, str_chat))

    # return
    return str_chat

def call_chatgpt(str_query, log=False):
    '''
    makes the api call to chat gpt service
    '''
    # initialize
    str_result = ""
    list_conversation = []

    # build the payload
    # list_conversation.append({'role': 'system', 'content': MODEL_PROMPT_SUMMARIZE.format(str_query)})
    list_conversation.append({'role': 'system', 'content': str_query})

    if log:
        print("using chat input: {}\n".format(json.dumps(list_conversation, indent=1)))

    # query
    response = openai.ChatCompletion.create(
        model = MODEL_CHATGPT,
        messages = list_conversation
    )

    # get the response
    str_response = response.choices
    # log
    if log:
        print("got chatGPT response: {}".format(str_response))

    # get the text response
    str_result = str_response[0].get('message').get('content')

    # return
    return str_result
