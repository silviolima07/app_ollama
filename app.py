import streamlit as st
import ollama
import time



try:
    # Chame uma função da biblioteca
    result = ollama.list()
    st.write("A biblioteca ollama está funcionando corretamente.")
except Exception as e:
    st.write(f"Erro ao chamar a função: {e}")


#st.title("TESTE2")
# Input for the prompt
#prompt = st.text_input("Ask Anything")



#if prompt:

    # Display input prompt from user
    #with st.chat_message("user"):
    #    st.write(prompt)

    # Processing
    #with st.spinner("Processing..."):
    #   try:
    #     result = ollama.list()
    #     st.write(result)
         
    #   except Exception as e:
    #     st.error(f'Error: {e}')