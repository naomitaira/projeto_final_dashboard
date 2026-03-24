# projeto_final_dashboard
Este é um dashboard interativo desenvolvido em Python utilizando Streamlit e Plotly. O objetivo é facilitar a visualização geográfica de vendas e o monitoramento de métricas financeiras (Receita, Custo e Lucro) através de filtros inteligentes.

🚀 Funcionalidades
Mapa de Calor Geográfico: Visualização de vendas por Latitude e Longitude.

Métricas em Tempo Real: Cartões com totais de Receita, Lucro, Cidades e Pontos de Venda que se atualizam conforme os filtros.

Filtros Inteligentes (Sidebar):

Filtro por Região e Cidade (cascateado).

Filtro por Categoria de Produto e Vendedor.

Seletor de Período (Data).

Slider de Faixa de Preço.

Resumo por Cidade: Tabela detalhada com agrupamento de performance financeira formatada em BRL (R$).

🛠️ Tecnologias Utilizadas
Python

Streamlit (Interface Web)

Pandas (Manipulação de Dados)

Plotly Express (Gráficos e Mapas)

📦 Como Instalar e Rodar
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual (recomendado):

Bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

Bash
pip install streamlit pandas plotly
Prepare os dados:
Certifique-se de que o arquivo vendas_geo.csv esteja na pasta ./dados/.

Execute a aplicação:

Bash
streamlit run app.py
📊 Estrutura de Dados
O arquivo CSV deve conter as seguintes colunas para o funcionamento pleno:

Data, Região, Cidade, Categoria, Produto, Vendedor, Vendas, Custo, Lucro, Latitude, Longitude.

🎨 Personalização Visual
O projeto conta com estilização via CSS (Markdown) para:

Alteração da cor da barra lateral (Teal).

Customização de cores de tags e sliders (SteelBlue e MediumPurple).
