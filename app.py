import streamlit as st
import ollama
import time

st.title("TESTE2")
# Input for the prompt
prompt = st.text_input("Ask Anything")



if prompt:

    # Display input prompt from user
    with st.chat_message("user"):
        #st.title("first with")
        st.write(prompt)

    # Processing
    with st.spinner("Processing..."):
       try:
         result = ollama.list()
         st.write(result)
         
       except Exception as e:
         st.error(f'Error: {e}')