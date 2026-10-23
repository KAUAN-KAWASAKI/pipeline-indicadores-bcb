# Extrair.py
import requests
import pandas as pd

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/20?formato=json"

# Buscar os dados:
resposta = requests.get(URL, timeout=30)
resposta.raise_for_status()
dados = resposta.json()

# Criação da Tabela:
tabela = pd.DataFrame(dados)
tabela["data"] = pd.to_datetime(tabela["data"], format="%d/%m/%Y")
tabela["valor"] = pd.to_numeric(tabela["valor"])


# Salvar o CSV
tabela.to_csv("dados/selic.csv", index=False)
print(f"{len(tabela)} linhas salvas em dados/selic.csv")