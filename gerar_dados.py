import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000
datas = pd.date_range('2023-01-01', '2025-12-31', freq='D')

# gerar dados de vendas

dados = pd.DataFrame({
    'Data': np.random.choice(datas,n),
    'Produto': np.random.choice(['Headset', 'Mouse', 'Teclado', 'Headphone', 'Webcam', 'SSD', 'Memória RAM'], n),
    'Categoria': np.random.choice(['Informática', 'Armazenamento', 'Periféricos'], n),
    'Região': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], n),
    'Vendedor': np.random.choice(['Ana Silva', 'Bruno Costa', 'Carla Dias', 'Diego Lima', 'Eva Santos'], n),
    'Vendas':np.random.randint(150, 12000, n),
    'Quantidade': np.random.randint(1, 30, n),
    'Custo': np.random.uniform(80, 8000, n)

})

dados['Lucro']=dados['Vendas'] - dados['Custo'].round(2)

# transformar em df + salvar em csv

df = pd.DataFrame(dados)

df.to_csv("./dados/vendas.csv", index=False)

print("Sucesso! Dados salvos em csv ./dados/vendas.csv")