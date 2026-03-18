import streamlit as st
import pandas as pd
import plotly.express as px

dados_vendas = pd.read_csv('dados/vendas.csv')

df = pd.DataFrame(dados_vendas)

st.title("🔬:rainbow[Análise detalhada de produtos - correção]🔬")

# produtos = st.multiselect(
#     "Favor selecionar os produtos desejados:",
#     ('Headset', 'Mouse', 'Teclado', 'Headphone', 'Webcam', 'SSD', 'Memória RAM'),
#     default=('Headset'),
# )

# TO-DO: MELHORAR AS OPCOES DO SELECTBOX PRA MOSTRAR OS PRODUTOS DISPONIVEIS NO DATAFRAME

produtos = st.selectbox(
    "Favor selecionar os produtos desejados:",
    ('Headset', 'Mouse', 'Teclado', 'Headphone', 'Webcam', 'SSD', 'Memória RAM')
)


# filtrar dados 
# dados_filtrados = dados_vendas[(dados_vendas["Produto"].isin(produtos))]

dados_filtrados = dados_vendas[(dados_vendas["Produto"] == produtos)]

# métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    receita = dados_filtrados['Vendas'].sum()
    st.metric("🗃️Receita", f"R$ {receita:.2f}")

with col2:
    lucro = dados_filtrados['Lucro'].sum()
    st.metric("📈Lucro", f"R$ {lucro:.2f}")

with col3:
    qtd = dados_filtrados['Quantidade'].sum()
    st.metric("📊Quantidade vendida", f"{qtd} unidades")

# calcula margem média

custo_medio = receita / qtd 

with col4:
    st.metric("💵Custo Médio", f"R$ {custo_medio:.2f}")

 
# utilizar pra debuggar o codigo

col1, col2 = st.columns(2)
with col1: 
    st.subheader("🔍 Dados filtrados ")
    st.dataframe(dados_filtrados)
with col2:
    st.subheader("Espaco pra graficos")






