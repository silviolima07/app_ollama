import streamlit as st
import ollama
import time

st.title("TESTE2")
# Input for the prompt
prompt = st.chat_input("Ask Anything")



if prompt:

    # Display input prompt from user
    #st.title("st.chat_message")
    with st.chat_message("user"):
        #st.title("first with")
        st.write(prompt)

    # Processing
    #st.title("st.spiner")
    with st.spinner("Processing..."):
       #st.title("ollama.list()")
       st.write(ollama.list())
       