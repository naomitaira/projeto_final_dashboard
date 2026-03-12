import streamlit as st

# config inicial

st.set_page_config(
    page_title="Dashboard de vendas",
    page_icon=":bar_chart",
    layout="wide"
)

# colorir a pagina 

st.markdown("""
<style>
.stApp {
    background-color: #CFF9E7;
}
</style>
""", unsafe_allow_html=True)


# definindo as pags

visao_geral = st.Page("./pages/visao_geral.py",
                    title = "Visão Geral",
                    default=True
                )

analise_vendas = st.Page('./pages/analise_vendas.py',
                         title='Análise de Vendas',
                        )

# analise_produtos = st.Page('./pages/analise_produtos.py',
#                          title='Análise de Produtos'
#                         )

# sobre = st.Page('./pages/sobre.py',
#                          title='Sobre'
#                         )

# configurando a navegacao

pg = st.navigation(
    [
    visao_geral,
    analise_vendas
    ]
)

pg.run()

