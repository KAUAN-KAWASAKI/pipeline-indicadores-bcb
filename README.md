# Pipeline de Indicadores do Banco Central

Pipeline ETL em Python que coleta indicadores econômicos da API pública do Banco Central (SGS), trata os dados com pandas e carrega em um banco SQL.

## Indicadores

| Indicador | Série SGS | Frequência |
|---|---|---|
| Meta da Selic (% a.a.) | 432 | diária |
| IPCA (variação % mensal) | 433 | mensal |
| Dólar PTAX venda (R$) | 1 | diária |

Fonte: [API de dados abertos do Banco Central](https://dadosabertos.bcb.gov.br/) (`https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json`).

## Etapas do projeto

- [ ] **Extração:** buscar as séries na API e salvar em CSV
- [ ] **Carga:** gravar os dados tratados em um banco MySQL
- [ ] **Agendamento:** rodar o pipeline todo dia com GitHub Actions
- [ ] **Docker:** empacotar o pipeline e o banco para rodar em qualquer máquina

## Estrutura

```
src/        código do pipeline
dados/      arquivos gerados (não versionados)
```

## Como rodar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
python src/extrair.py
```

## Tecnologias

Python · requests · pandas · SQL
