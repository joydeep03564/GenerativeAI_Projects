import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()
os.environ['LANGCHAIN_API_KEY']=os.environ.get('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACKING_V2']= "true"
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A chatbot with OpenAI"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "yor are a helfull assistant.please response to the user queries"),
        ('user','Question: {questions}')
    ]
)
def generate_response(questions,api_key,llm,temperature,max_tokens):
    openai.api_key=api_key
    llm = ChatOpenAI(model=llm)
    output_parser= StrOutputParser()
    chain=prompt|llm|output_parser
    answer = chain.invoke({'questions': questions})
    return answer

st.title('Enhanced Q&A Chatbot with OpenAI')
st.sidebar.title('Settings')
api_key=st.sidebar.text_input("Enter your Open AI API Key:",type="password")
llm=st.sidebar.selectbox("Select an Open AI Model",["gpt-4o","gpt-4-turbo","gpt-4"])

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens =st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

st.write("Go ahead and ask your questions")
user_input=st.text_input('you:')

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")

  
     