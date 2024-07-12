import os

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu site")


@st.cache
def carregar_dados():
    try:
        dados = pd.read_csv("resultados.csv")
        return dados
    except FileNotFoundError:
        st.error("Arquivo 'resultados.csv' não encontrado.")
        return None
    except pd.errors.EmptyDataError:
        st.error("O arquivo 'resultados.csv' está vazio.")
        return None
    except pd.errors.ParserError:
        st.error("Erro ao processar 'resultados.csv'. Verifique o formato dos dados.")
        return None


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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    st.set_option('server.port', port)
    st.set_page_config(layout="wide")
    st.title('Meu aplicativo Streamlit')
    st.write('Hello world!')