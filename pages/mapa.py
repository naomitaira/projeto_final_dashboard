import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
dados_localizacoes = pd.read_csv("./dados/vendas_geolocalizacao.csv")

df = pd.DataFrame(dados_localizacoes)

st.title("🌎  Mapa de Vendas por Localização")

st.subheader("Visualize a distribuição geográfica das vendas e aplique filtros para explorar os dados.")


# criar 4 colunas para as métricas

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Pontos no Mapa", 2000)

with col2:
    st.metric("Cidades", 38)

with col3:
    st.metric("Receita", f"R$ {df['Vendas'].sum():.2f}")

with col4:
    st.metric("Lucro", f"R$ {df['Lucro'].sum():.2f}")
    
    
############################ FILTROS ############################

############################ FILTRO DE REGIÃO ############################

filtro_regiao = st.sidebar.multiselect(
    "Selecione as regiões",
    options=df["Região"].unique(),
    default=df["Região"][0]
)

############################ FILTRO DE CATEGORIA ############################

filtro_categoria = st.sidebar.multiselect(
    "Selecione as categorias",
    options=df["Categoria"].unique(),
    default=df["Categoria"][0]
)

############################ FILTRO DE PRODUTO ############################

filtro_produto = st.sidebar.multiselect(
    "Selecione os produtos",
    options=df["Produto"].unique(),
    default=df["Produto"][0]
)

############################ FILTRO DE VENDEDOR ############################

filtro_vendedor = st.sidebar.multiselect(
    "Selecione os vendedores",
    options=df["Vendedor"].unique(),
    default=df["Vendedor"][0]
)

############################ FILTRO DE DATA ############################

# transforma str data pra .to_datetime

df["Data"]=pd.to_datetime(df["Data"])

# transformar a data em padrao br

df["Data_formatada"] = df["Data"].dt.strftime("%d/%m/%Y %H:%M:%S")

# recupera as datas minimas e maximas do dataframe
data_min = df["Data"].min().date()
data_max = df["Data"].max().date()

filtro_data = st.sidebar.date_input(
    "Selecione o período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max
)


# garantir que existem duas datas selecionadas
if len(filtro_data) == 2:
    data_inicio = pd.to_datetime(filtro_data[0])
    data_fim = pd.to_datetime(filtro_data[1])
else:
    st.warning("Selecione uma data inicial e final no filtro.")
    st.stop()

############################ FILTRO DE PREÇO ############################

filtro_preco = st.sidebar.slider(
    "Faixa de Valor da Venda (R$)",
    min_value=157,
    max_value=11997,
    value=(157, 11997)
)
# formatar o custo pra melhorar a visualização

df["Custo_formatado"] = df["Custo"].apply(
    lambda x: f"R$ {x:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ',')
)

# # aplicar os filtros e montar um DF

dados_filtrados = df[
    (df["Região"].isin(filtro_regiao)) &
    (df["Categoria"].isin(filtro_categoria)) &
    (df["Vendedor"].isin(filtro_vendedor)) &
    (df["Data"].between(data_inicio, data_fim)) &
    (df["Custo"].between(filtro_preco[0], filtro_preco[1]))
]

# Gráfico de bolhas
# fig = px.scatter_mapbox(
#     df,
#     lat=df['Latitude'],
#     lon=df['Longitude'],
#     size='Vendas',
#     color='Lucro',
#     hover_name='Região',
#     hover_data={'Vendas': True, 'Lucro': True, 'lat': False, 'lon': False},
#     color_continuous_scale=px.colors.sequential.Magma,
#     size_max=20,
#     zoom=2,
#     mapbox_style="open-street-map"
# )

# st.plotly_chart(fig,width='stretch')

# mostrar dataframe

st.subheader("Resumo por Cidade")

st.dataframe(dados_filtrados[["Produto","Custo_formatado", "Região", "Categoria", "Vendedor", "Data_formatada"]])