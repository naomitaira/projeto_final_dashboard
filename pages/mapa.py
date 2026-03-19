import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
dados_localizacoes = pd.read_csv("./dados/vendas_geo_resumo.csv")

st.title("🌎  Mapa de Vendas por Localização")

st.subheader("Visualize a distribuição geográfica das vendas e aplique filtros para explorar os dados.")

# Coordenadas

# coordenadas = {}

# criar 4 colunas 

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Pontos no Mapa", 2000)

with col2:
    st.metric("Cidades", 38)

with col3:
    st.metric("Receita Filtrada",f" R$ XXXX")

with col4:
    st.metric("Lucro Filtrado",f" R$ XXXX")

filtro_regiao = st.sidebar.selectbox("Região",
    ("Todas", "Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"),  index=None,placeholder="Escolha uma das opções",
)

filtro_categoria = st.sidebar.selectbox("Categoria",
    ("Todas", "Armazenamento", "Informática", "Periféricos"), index=None,placeholder="Escolha uma das opções"
)

filtro_produto = st.sidebar.selectbox("Produto",
    ("Todos", "Headset", "Mouse", "Teclado", "Headphone", "Webcam", "SSD", "Memória RAM"), index=None,placeholder="Escolha uma das opções"
)

filtro_vendedor = st.sidebar.selectbox("Vendedor",
    ('Todos', 'Ana Silva', 'Bruno Costa', 'Carla Dias', 'Diego Lima', 'Eva Santos'), index=None,placeholder="Escolha uma das opções"
)

# recupera as datas minimas e maximas do dataframe
# data_min = dados_vendas["Data"].min().date()
# data_max = dados_vendas["Data"].max().date()

# # filtro de periodo
# data_range = st.sidebar.date_input(
#     "Selecione o período",
#     value=(data_min, data_max),
#     min_value=data_min,
#     max_value=data_max
# )

# # garantir que existem duas datas selecionadas
# if len(data_range) == 2:
#     data_inicio = pd.to_datetime(data_range[0])
#     data_fim = pd.to_datetime(data_range[1])
# else:
#     st.warning("Selecione uma data inicial e final no filtro.")
#     st.stop()

# Gráfico de bolhas
# fig = px.scatter_mapbox(
#     mapa_df,
#     lat='lat',
#     lon='lon',
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