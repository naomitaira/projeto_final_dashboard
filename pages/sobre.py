import streamlit as st
import pandas
import plotly.express as px

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


st.markdown("""
# 📊 Dashboard de Vendas e Produtos

Bem-vindo ao **Dashboard Interativo de Vendas**, projetado para fornecer uma visão completa do desempenho da sua empresa. Aqui você pode explorar **vendas, lucros, produtos e performance da equipe** de forma dinâmica.

---

## 🔹 Funcionalidades Principais

- **Filtros Interativos:** selecione regiões, categorias e períodos para atualizar automaticamente gráficos e métricas.  
- **Métricas Chave:**
  - 💰 **Receita Filtrada:** total de vendas no período selecionado  
  - 📈 **Lucro Filtrado:** lucro acumulado das vendas filtradas  
  - 📊 **Margem Média:** porcentagem de rentabilidade média  
- **Performance por Vendedor:** identifique os melhores colaboradores com base em receita, lucro, número de vendas e ticket médio.  
- **Análise Temporal:** visualize tendências e sazonalidades de vendas mês a mês.  
- **Exportação de Dados:** filtre, visualize e baixe os dados para análises externas em CSV 📥

---

## 🌟 Benefícios do Dashboard

- Tomada de decisão mais rápida e baseada em dados confiáveis  
- Comparação de produtos, categorias e regiões em tempo real  
- Monitoramento detalhado da performance da equipe de vendas  
- Identificação de oportunidades de crescimento e otimização de recursos

---
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    st.image("pages/dvader.jpeg", caption="Meme de dados engraçado", width='content')