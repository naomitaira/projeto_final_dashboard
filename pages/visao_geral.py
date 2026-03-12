import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt

def carregar_dados():
    df = pd.read_csv('dados/vendas.csv')
    return df


# utiliza a funcao para carregar os dados + armazena em variavel + df do pandas q contem os dados das vendas

dados_vendas = carregar_dados()

st.title(":rainbow[Visão geral do negócio]", text_alignment='center')

# KPIs principais 

col1, col2, col3, col4 = st.columns(4)

# EXIBE A RECEIRA TOTAL FORMATADA
col1.metric('Receita Total', f"R$ {dados_vendas['Vendas'].sum():,.2f}")

# EXIBE O LUCRO TOTAL FORMATADO
col2.metric('Lucro Total',f"R$ {dados_vendas['Lucro'].sum():,.2f}")

# TOTAL DE TRANSAÇÕES 
col3.metric('Total de transações',f"{len(dados_vendas)}")

# TICKET MÉDIO
col4.metric('Ticket médio', f"R$ {dados_vendas['Vendas'].mean():,.2f}")

st.divider()

colA,colB = st.columns(2)

with colA:
    vendas_regiao = dados_vendas.groupby('Região')['Vendas'].sum().reset_index()

    fig = px.pie(vendas_regiao, names='Região', values='Vendas', 
                 title='Distribuição de vendas por região',
                 hole=0.4)
    
# EXIBIR O GRÁFICO USANDO STREAMLIT

    st.plotly_chart(fig, width='content')

with colB:

    # Converter coluna para data
    dados_vendas['Data'] = pd.to_datetime(dados_vendas['Data'])
    dados_vendas['Mês'] = dados_vendas['Data'].dt.to_period('M').astype(str)

    vendas_mes = dados_vendas.groupby('Mês')['Vendas'].sum().reset_index()

    fig_line = px.line(vendas_mes, x='Mês', y='Vendas', 
                 title='Vendas mensais',
                 markers=True)
    
# EXIBIR O GRÁFICO USANDO STREAMLIT

    st.plotly_chart(fig_line, width='content')