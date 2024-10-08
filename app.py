import streamlit as st 
import os 
import ast
import pandas as pd
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from scripts.agents import agent_1, agent_2, agent_3, agent_5
from scripts.services import services

os.environ['PINECONE_API_KEY'] = 'your_pinecone_api_key'

embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
vc = PineconeVectorStore(index_name='test', embedding=embeddings)
data = pd.read_csv('assets/csv/price.csv')

open('assets/prompts/agents/agent_3.txt' , 'w').write(
    open('assets/prompts/agents/agent_3.txt').read().format(list(data.columns) , {col: data[col].unique().tolist() for col in data.columns})
)

def answer(query) : 

    choice = agent_1.classifiying_agent(query)

    try : choice = ast.literal_eval(choice)
    except : choice = (1, 1)
    
    print('--------------------------------Agent 1----------------------------------')
    print(choice)

    rag_response = agent_2.run_rag(query , vc) if choice[0] else ''

    print('--------------------------------Agent 2-----------------------------------')
    print(rag_response)

    if choice[1] : 

        csv_response = agent_3.run_csv_agent(query)
        print('---------------------------------------Code-------------------------------------')
        print(csv_response)
        csv_response = services.execute_script_with_retry(csv_response, data)

    else : csv_response = ''

    print('--------------------------------Agent 3------------------------------------')
    print(csv_response)

    final_response = agent_5.beautify_response(query , rag_response , csv_response)

    print('--------------------------------Agent 5-------------------------------------')
    print(final_response)

    return final_response


if 'welcome_shown' not in st.session_state : 

    st.session_state.welcome_shown = True

def check_prompt(prompt) : 

    try : prompt.replace('', '') ; return True 
    except : return False

def check_mesaage() : 

    if 'messages' not in st.session_state : st.session_state.messages = []

check_mesaage()

for message in st.session_state.messages : 

    if message['role'] == 'user' : st.markdown(
        f'<div style="display: flex; align-items: center;">'
        f'<img src="https://i.imgur.com/u54ZDPk.png" width="30"/>'
        f'<div style="margin-left: 10px;">{message["content"]}</div>'
        '</div>' , unsafe_allow_html = True)

    else : st.markdown(
        f'<div style="display: flex; align-items: center;">'
        f'<img src="https://i.imgur.com/u54ZDPk.png" width="30"/>'
        f'<div style="margin-left: 10px;">{message["content"]}</div>'
        '</div>' , unsafe_allow_html = True)

for message in st.session_state.messages : 

    with st.chat_message(message['role']) : st.markdown(message['content'])

query = st.chat_input('Ask me anything')

if check_prompt(query) : 

    with st.chat_message('user') : st.markdown(query)

    st.session_state.messages.append({'role' : 'user' , 'content' : query})

    if query is not None and query != '' :  

        response = answer(query)

        with st.chat_message('assistant') : st.markdown(response)

        st.session_state.messages.append({'role' : 'assistant' , 'content' : response})