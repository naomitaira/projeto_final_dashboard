import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados - dataframe 1 - pra fazer filtros 

dados_mapa = pd.read_csv("./dados/vendas_geo.csv")

df = pd.DataFrame(dados_mapa)

###################################################################

st.title("🌎  Mapa de Vendas por Localização")

st.subheader("Visualize a distribuição geográfica das vendas e aplique filtros para explorar os dados.")

############################ COLORIR SIDEBAR ############################

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #20B2AA;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
    
    
############################ FILTROS ############################

############################ COLORIR FILTROS ############################ 
st.markdown("""
<style>
span[data-baseweb="tag"] {
  background-color: SteelBlue !important;
}
</style>
""", unsafe_allow_html=True) #colocar antes dos filtros pra dar cor

############################ FILTRO DE REGIÃO ############################

filtro_regiao = st.sidebar.multiselect(
    "Selecione as regiões",
    options=df["Região"].unique(),
    default=df["Região"].unique()
)

df_cidades_filtradas = df[df["Região"].isin(filtro_regiao)]

############################ FILTRO DE CIDADE ############################

filtro_cidade = st.sidebar.multiselect(
    "Filtrar por Cidade", 
    options=df_cidades_filtradas["Cidade"].unique(),
    default=df_cidades_filtradas["Cidade"].unique()
)

############################ FILTRO DE CATEGORIA ############################

filtro_categoria = st.sidebar.multiselect(
    "Selecione as categorias",
    options=df["Categoria"].unique(),
    default=df["Categoria"].unique()
)

############################ FILTRO DE PRODUTO ############################

filtro_produto = st.sidebar.multiselect(
    "Selecione os produtos",
    options=df["Produto"].unique(),
    default=df["Produto"].unique()
)

############################ FILTRO DE VENDEDOR ############################

filtro_vendedor = st.sidebar.multiselect(
    "Selecione os vendedores",
    options=df["Vendedor"].unique(),
    default=df["Vendedor"].unique()
)

############################ FILTRO DE DATA ############################

# transforma str data pra .to_datetime

df["Data"]=pd.to_datetime(df["Data"])

# transformar a data em padrao br

df["Data_formatada"] = df["Data"].dt.strftime("%d/%m/%Y %H:%M:%S")

# recupera as datas minimas e maximas do dataframe
data_min = df["Data"].min().date()
data_max = df["Data"].max().date()


############################ IMPLEMENTAR FILTRO DE DATA ############################


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

############################ COLORIR FILTRO DE PREÇO ############################

st.markdown("""
<style>
    /* 1. Cor da trilha (a barra que você arrasta) - Lilás */
    div[data-baseweb="slider"] > div > div > div:nth-child(1) {
        background: #9370DB !important;
    }

    /* 2. Cor do número que flutua (o valor do slider) */
    /* Tentamos vários seletores para garantir que o CSS encontre o número */
    div[data-testid="stThumbValue"], 
    div[data-testid="stThumbValue"] > div,
    span[data-baseweb="typography"] {
        color: #9370DB !important;
        font-weight: bold !important;
    }

    /* 3. Opcional: Cor das bolinhas para combinar com o lilás */
    div[role="slider"] {
        background-color: #9370DB !important;
        border: 2px solid white !important;
    }
</style>
""", unsafe_allow_html=True)

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
    (df["Custo"].between(filtro_preco[0], filtro_preco[1])) &
    (df["Cidade"].isin(filtro_cidade))
]

########################### METRICAS ###########################

########################### FUNCAO PRA FORMATAR VALORES ###########################

def format_brl(x):
    return f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# criar 4 colunas para as métricas

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric("Pontos no Mapa", len(df))

with col2:
    st.metric("Cidades", df["Cidade"].nunique())

with col3:
    receita = df["Vendas"].sum()
    st.metric("Receita", format_brl(receita))

with col4:
    lucro = df["Lucro"].sum()
    st.metric("Lucro", format_brl(lucro))


############################ MAPA ############################ 

if "Latitude" in df.columns and "Longitude" in df.columns:
    
    fig1 = px.scatter_mapbox(
        dados_filtrados,
        lat="Latitude",         
        lon="Longitude",
        size='Vendas',
        color='Lucro',
        hover_name="Região",     
        hover_data={
            "Vendas": True,
            "Lucro": True,
            "Latitude": False,  
            "Longitude": False
        },
        color_continuous_scale=px.colors.sequential.Darkmint,
        size_max=8,
        zoom=3,
        mapbox_style="open-street-map"
        )

# mostrar mapa 
st.plotly_chart(fig1,width='stretch')



########################### DATAFRAME - RESUMO POR CIDADE ###########################

st.subheader("Resumo por Cidade")

# mostrar dataframe

st.dataframe(dados_filtrados[["Cidade", "Região","Produto","Custo_formatado" , "Data_formatada" ,"Lucro"]])

with col1:
    
    st.metric("Pontos no Mapa", len(df2))

with col2:
    st.metric("Cidades", df2['Cidade'].count())

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

############################ MAPA ############################ 

if "Latitude" in df.columns and "Longitude" in df.columns:
    
    fig1 = px.scatter_mapbox(
        df,
        lat="Latitude",         
        lon="Longitude",
        size='Vendas',
        color='Lucro',
        hover_name="Região",     
        hover_data={
            "Vendas": True,
            "Lucro": True,
            "Latitude": False,  
            "Longitude": False
        },
        color_continuous_scale=px.colors.sequential.Darkmint,
        size_max=15,
        zoom=2,
        mapbox_style="open-street-map"
        )

st.plotly_chart(fig1,width='stretch')

# mostrar dataframe

st.subheader("Resumo por Cidade")

st.dataframe(dados_filtrados[["Produto","Custo_formatado", "Região", "Categoria", "Vendedor", "Data_formatada"]])

