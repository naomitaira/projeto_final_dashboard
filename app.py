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

# analise_vendas = st.Page('./pages/analise_vendas.py',
#                          title='Análise de Vendas',
#                          icon=':moneybag:'
#                         )

# analise_produtos = st.Page('./pages/analise_produtos.py',
#                          title='Análise de Produtos',
#                          icon=':package:'
#                         )

# sobre = st.Page('./pages/sobre.py',
#                          title='Sobre',
#                          icon=':information_source:'
#                         )

# configurando a navegacao

pg = st.navigation(
    [
    visao_geral
    ]
)

pg.run()

