import os
import streamlit as st
import pandas as pd

# Configuração da página do Streamlit
st.set_page_config(page_title="Meu Aplicativo", layout="wide")

# Função para carregar dados (exemplo)
def carregar_dados():
    dados = pd.read_csv("dados.csv")
    return dados

# Corpo principal do aplicativo Streamlit
st.title('Meu Aplicativo')
st.write('Hello world!')

# Exemplo de uso de dados carregados
dados = carregar_dados()
if dados is not None:
    st.write(dados.head())

# Containers adicionais
with st.container():
    st.title("Dashboard Contratos")
    st.write("Hello **world**!")
    st.write("Mês de Janeiro")
    st.write("[Link](https://www.google.com.br/)")
    st.write("---")

with st.container():
    qtd_dias = st.selectbox("Selecione o período", ["1D", "15D", "31D"])
    num_dias = int(qtd_dias.replace("D", ""))

    dados = carregar_dados()
    if dados is not None:
        dados = dados[-num_dias:]
        st.area_chart(dados, x="Data", y="Contratos")
