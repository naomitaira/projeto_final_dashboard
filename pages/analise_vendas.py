import streamlit as st
import pandas as pd
import plotly_express as px

def carregar_dados():
    df = pd.read_csv('dados/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# carregar os dados
dados_vendas = carregar_dados()

st.title("Análise detalhada de vendas")

st.sidebar.header("Filtros de vendas")

