import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu site")

@st.cache_data
def carregar_dadps():
    dados = pd.read_csv("resultados.csv")
    return dados

with st.container():
    st.title("Dashbord Contratos")
    st.write("Mês de Janeiro")
    st.write("[Link](https://www.google.com.br/)")
    st.write("---")

with st.container():
    qtd_dias = st.selectbox("Slecione o período", ["1D","15D","31D"])
    num_dias = int(qtd_dias.replace("D", ""))
    dados = carregar_dadps()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")

