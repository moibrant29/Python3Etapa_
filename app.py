import streamlit as st
import pandas as pd

nome = "Moisés"
idade = 17

st.write("Olá, mundo")
st.write(nome, idade)

df = pd.DataFrame({
    'first column': ['Português', 'Matemática', 'Python', 'Frame'],
    'second column': [5, 9, 7, 10]
})

st.title("Meu primeiro dash")
st.subheader(nome)

st.write(df)

st.divider()

produto = st.selectbox(
    "Selecione um produto",
    ["Arroz", "Feijão", "Leite", "Macarrão"]
)

def calcular_preco(produto):
    if produto == "Arroz":
        return 25
    elif produto == "Feijão":
        return 10
    elif produto == "Leite":
        return 6
    elif produto == "Macarrão":
        return 5

preco = calcular_preco(produto)

st.metric("Preço da compra", f"R$ {preco},00")