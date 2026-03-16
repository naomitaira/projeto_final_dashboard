import streamlit as st
import pandas as pd
import plotly_express as px

def carregar_dados():
    df = pd.read_csv('dados/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# carregar os dados
dados_vendas = carregar_dados()

st.title("🔬 Análise detalhada de vendas 🔬")

# filtros para analise
st.sidebar.header("Filtros de vendas")

st.markdown("""
<style>
span[data-baseweb="tag"] {
  background-color: green !important;
}
</style>
""", unsafe_allow_html=True)

regioes = st.sidebar.multiselect(
    "Selecione as regiões",
    options=dados_vendas["Região"].unique(),
    default=dados_vendas["Região"].unique()
)

categorias = st.sidebar.multiselect(
    "Selecione as categorias",
    options=dados_vendas["Categoria"].unique(),
    default=dados_vendas["Categoria"].unique()
)

# recupera as datas minimas e maximas do dataframe
data_min = dados_vendas["Data"].min().date()
data_max = dados_vendas["Data"].max().date()

# filtro de periodo
data_range = st.sidebar.date_input(
    "Selecione o período",
    value=(data_min, data_max),
    min_value=data_min,
    max_value=data_max
)

# garantir que existem duas datas selecionadas
if len(data_range) == 2:
    data_inicio = pd.to_datetime(data_range[0])
    data_fim = pd.to_datetime(data_range[1])
else:
    st.warning("Selecione uma data inicial e final no filtro.")
    st.stop()

# aplicar os filtros
dados_filtrados = dados_vendas[
    (dados_vendas["Região"].isin(regioes)) &
    (dados_vendas["Categoria"].isin(categorias)) &
    (dados_vendas["Data"].between(data_inicio, data_fim))
]

# métricas
col1, col2, col3 = st.columns(3)

col1.metric("Receita Filtrada", f"R$ {dados_filtrados['Vendas'].sum():.2f}")
col2.metric("Lucro Filtrado", f"R$ {dados_filtrados['Lucro'].sum():.2f}")

# calcula margem média
margem_media = "N/A"

if dados_filtrados['Vendas'].sum() > 0:
    margem_media = dados_filtrados['Lucro'].sum() / dados_filtrados['Vendas'].sum() * 100
    margem_media = f"{margem_media:.2f}"

col3.metric("Margem Média", f"{margem_media} %")


# vendas por vendedor

st.subheader(":green[Performance por vendedor]")
vendas_vendedor = dados_filtrados.groupby("Vendedor").agg(
Receita=("Vendas", "sum"),
Lucro=("Lucro", "sum"),
Transacoes=("Vendas", "count"),
Ticket_medio=("Vendas", "mean") 
).round(2).sort_values(by="Receita", ascending=False)

def format_brl(x):
    return f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Aplica direto nas colunas monetárias
vendas_vendedor[["Receita", "Lucro", "Ticket_medio"]] = vendas_vendedor[["Receita", "Lucro", "Ticket_medio"]].applymap(format_brl)


# criar grafico de barras pra visualizar dados

v_col1, v_col2 = st.columns(2)

with v_col1:
    st.write("🗃️ ***Tabela de dados por vendedor*** 🗃️")
    st.dataframe(vendas_vendedor, width='stretch')

with v_col2:

    fig = px.bar(
        vendas_vendedor.reset_index(),
        x="Vendedor",
        y="Receita",
        title="👩🏻‍💼Receita e Lucro por vendedor  👩🏻‍💼",
        color="Lucro",
        color_continuous_scale=px.colors.sequential.Sunset,
        )
    st.plotly_chart(fig, use_container_width=True)

# cria nova coluna mes no dataframe - extraindo o mes e o ano da coluna 'data'
st.subheader("📅 Análise Temporal 📅")

dados_filtrados['Mês'] = dados_filtrados['Data'].dt.to_period('M').astype(str)
mensal = dados_filtrados.groupby('Mês').agg(
    Receita=("Vendas", "sum"),
    Lucro=("Lucro", "sum"),
).reset_index()

# cria grafico de barras para comparar a receita e o lucro mensal - usando a coluna 'mes'

fig_2 = px.bar(
    mensal, x="Mês",
    y=['Receita', 'Lucro'],
    barmode='group', title='Receita x Lucro Mensal'
)

st.plotly_chart(fig_2, width='stretch')

# fazer expander com download dos dados

df = dados_filtrados

# Função para converter os dados para CSV e permitir download
@st.cache_data
def convert_for_download(df):
    return df.to_csv(index=False).encode("utf-8") 

csv = convert_for_download(df)

# Expander com título
with st.expander("👁️👁️ Visualizar dados e baixar CSV 📥"):
    st.dataframe(df) 
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="analise_vendas.csv",
        mime="text/csv",
        icon="📥"  
    )

