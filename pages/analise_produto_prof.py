import streamlit as st
import pandas as pd
import plotly.express as px
import locale
import datetime

# Função para formatar valores em reais

def format_brl(value):
    # Set the locale to Brazilian Portuguese
    # On some systems, the locale string might be slightly different (e.g., 'pt_BR.UTF-8')
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        # Fallback for systems where 'pt_BR.UTF-8' is not available
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR')
        except locale.Error:
            print("Warning: Could not set pt_BR locale. Falling back to simple formatting.")
            return f"R$ {value:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')

    # Format the value as currency with grouping enabled
    # locale.currency() returns a string like 'R$ 1.234,56'
    formatted_value = locale.currency(value, symbol=True, grouping=True)
    return formatted_value

###################################################################################################

dados_vendas = pd.read_csv('dados/vendas.csv')

df = pd.DataFrame(dados_vendas)

st.title("🔬:rainbow[Análise detalhada de produtos - correção]🔬")

# produtos = st.multiselect(
#     "Favor selecionar os produtos desejados:",
#     ('Headset', 'Mouse', 'Teclado', 'Headphone', 'Webcam', 'SSD', 'Memória RAM'),
#     default=('Headset'),
# )

# TO-DO: MELHORAR AS OPCOES DO SELECTBOX PRA MOSTRAR OS PRODUTOS DISPONIVEIS NO DATAFRAME

# SELECTBOX DINÂMICO
produtos = st.selectbox(
    "Favor selecionar o produto:",
    df["Produto"].unique()
)

# FILTRO 
dados_filtrados = df[df["Produto"] == produtos]

# métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    receita = dados_filtrados['Vendas'].sum()
    st.metric("🗃️Receita",  value=format_brl(receita))

with col2:
    lucro = dados_filtrados['Lucro'].sum()
    st.metric("📈Lucro", value=format_brl(lucro))

with col3:
    qtd = dados_filtrados['Quantidade'].sum()
    st.metric("📊Quantidade vendida", f"{qtd} unidades")

# calcula margem média

custo_medio = receita / qtd 

with col4:
    st.metric("💵Custo Médio", value=format_brl(custo_medio))

 
# utilizar pra debuggar o codigo

col1, col2 = st.columns(2)

with col1:
    st.subheader("Gráfico")
    df_agrupado_regiao = df.groupby("Região")["Vendas"].sum().reset_index()
    # sempre fazer debug pra ver se esta tudo certo
    # st.dataframe(df_agrupado_regiao)
    fig1 = px.bar(df_agrupado_regiao,
                  x='Região',
                  y='Vendas',
                  title=f'Vendas por região - {produtos}',
                  color='Vendas',
                  color_continuous_scale='Sunset'

                    )
    
    st.plotly_chart(fig1, width='stretch')


with col2:

    st.subheader("Gráfico")
    df_agrupado_vendedor = dados_filtrados.groupby("Vendedor")["Vendas"].sum().reset_index()
  
    # sempre fazer debug pra ver se esta tudo certo
    # st.dataframe(df_agrupado_regiao)

    fig2 = px.pie(df_agrupado_vendedor,
                  values='Vendas', 
                  names='Vendedor', 
                  title='Vendas por vendedor',
                  color_discrete_sequence = ['LightCoral', 'RebeccaPurple', 'PaleTurquoise', 'MediumVioletRed', 'Plum']
                  )
    
    st.plotly_chart(fig2, width='stretch')

#### gerar grafico mes a mes ####

st.subheader("Gráfico")

# transformar a coluna data de str pra period 

dados_filtrados['Data']= pd.to_datetime(dados_filtrados['Data'])

# gerar a coluna mês

dados_filtrados['Mês']= dados_filtrados['Data'].dt.to_period('M').astype(str)

# criar variavel para usar como dataframe no grafico

df_agrupado_meses = dados_filtrados.groupby("Mês")["Vendas"].sum().reset_index()

fig3 = px.area(
    df_agrupado_meses,
    x="Mês",
    y="Vendas",
    color_discrete_sequence=['Plum']
)

st.plotly_chart(fig3, width='stretch')

