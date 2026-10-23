# Extrair.py
# Buscar os dados
import requests

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/20?formato=json"

resposta = requests.get(URL, timeout=30)
resposta.raise_for_status()
dados = resposta.json()

print(dados[:3])

# Criação da Tabela:
import pandas as pd

tabela = pd.DataFrame(dados)
print(tabela.dtypes)

# Salvar o CSV
tabela.to_csv("dados/selic.csv", index=False)
print(f"{len(tabela)} linhas salvas em dados/selic.csv")