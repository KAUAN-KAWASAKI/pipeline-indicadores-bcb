# Extrair.py
import requests
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from banco import salvar


def criar_sessao():
    tentativas = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    sessao = requests.Session()
    sessao.mount("https://", HTTPAdapter(max_retries=tentativas))
    return sessao


SESSAO = criar_sessao()


def extrair_serie(codigo, nome):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/20?formato=json"

    # Buscar os dados:
    resposta = SESSAO.get(url, timeout=30)
    resposta.raise_for_status()
    dados = resposta.json()

    # Criação da Tabela:
    tabela = pd.DataFrame(dados)
    tabela["data"] = pd.to_datetime(tabela["data"], format="%d/%m/%Y")
    tabela["valor"] = pd.to_numeric(tabela["valor"])

    # Salvar o CSV
    tabela.to_csv(f"dados/{nome}.csv", index=False)
    print(f"{len(tabela)} linhas salvas em dados/{nome}.csv")
    print(f"{salvar(tabela, nome)} linhas gravadas no banco ({nome})")


extrair_serie(432, "selic")
extrair_serie(433, "ipca")
extrair_serie(1, "dolar")
