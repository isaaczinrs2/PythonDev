# título
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

import streamlit as st
from openai import OpenAI

modelo = OpenAI(
    api_key="sua_chave_de_api_aqui", 
)

st.write("ChatBot com IA")

# sessoin_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state.lista_mensagens = []


# Exibir mensagens anteriores
for mensagem in st.session_state.lista_mensagens:
    if mensagem["role"] == "user":
        st.chat_message("user").write(mensagem["content"])
    else:
        st.chat_message("assistant").write(mensagem["content"])

mensagem_usuario = st.chat_input("Digite sua mensagem:", key="chat_input")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state.lista_mensagens.append(mensagem)

# resposta da ia
    resposta_modelo = modelo.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.lista_mensagens
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content

    resposta_ia = "Você quis dizer: " + mensagem_usuario

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state.lista_mensagens.append(mensagem_ia)

    print(st.session_state.lista_mensagens)