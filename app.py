import streamlit as st
import ollama
import time

st.title("TESTE2")
# Input for the prompt
prompt = st.chat_input("Ask Anything")

if prompt:

    # Display input prompt from user
    with st.chat_message("user"):
        st.write(prompt)

    # Processing
    with st.spinner("Processing..."):
       st.write(ollama.list())        