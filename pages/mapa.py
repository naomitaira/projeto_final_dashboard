import streamlit as st
import pandas as pd
import plotly.express as px

# carregar dados
dados_vendas = pd.read_csv("./dados/vendas.csv")

st.title("🌎 Mapa de vendas por região")

# criar um dataframe resumido
mapa_df = dados_vendas.groupby('Região').agg(
    Vendas=('Vendas','sum'),
    Lucro=('Lucro','sum')
).reset_index()

# adicionar coordenadas fictícias para plot
coordenadas = {
    'Norte': {'lat': -1.0, 'lon': -50.0},
    'Sul': {'lat': -30.0, 'lon': -52.0},
    'Leste': {'lat': -10.0, 'lon': -40.0},
    'Oeste': {'lat': -15.0, 'lon': -60.0}
}

mapa_df['lat'] = mapa_df['Região'].apply(lambda x: coordenadas[x]['lat'])
mapa_df['lon'] = mapa_df['Região'].apply(lambda x: coordenadas[x]['lon'])

# criar gráfico de bolhas
fig = px.scatter_mapbox(
    mapa_df,
    lat='lat',
    lon='lon',
    size='Vendas',          # tamanho da bolha proporcional às vendas
    color='Lucro',          # cor da bolha proporcional ao lucro
    hover_name='Região',
    hover_data={'Vendas': True, 'Lucro': True, 'lat': False, 'lon': False},
    color_continuous_scale=px.colors.sequential.Sunset,
    size_max=50,
    zoom=3,
    mapbox_style='carto-positron'
)

st.plotly_chart(fig, use_container_width=True)