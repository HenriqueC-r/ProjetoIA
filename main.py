
# Bibliotecas usadas no projeto
import streamlit as st
from openai import OpenAI

# Cliente da OpenAI
# Coloque sua própria chave da API aqui
modelo_ia = OpenAI(api_key="SUA KEY AQUI")

# Título da aplicação
st.write("# IA do Caio")

# Guarda o histórico da conversa
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Campo para o usuário digitar a mensagem
texto_usuario = st.chat_input("Digite sua mensagem")

# Mostra as mensagens anteriores
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # Mostra a mensagem do usuário
    st.chat_message("user").write(texto_usuario)

    # Adiciona a mensagem no histórico
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # Envia a conversa para a IA gerar resposta
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content

    # Mostra resposta da IA
    st.chat_message("assistant").write(texto_resposta_ia)

    # Salva a resposta no histórico
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)