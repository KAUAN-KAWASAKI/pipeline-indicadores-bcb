import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text

load_dotenv()


def conectar():
    endereco = URL.create(
        "mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
    )
    certificado = os.getenv("DB_SSL_CA")
    opcoes = {"ssl": {"ca": certificado}} if certificado else {}
    return create_engine(endereco, connect_args=opcoes)


def salvar(tabela, nome):
    registros = [
        {"serie": nome, "data": linha.data.date(), "valor": linha.valor}
        for linha in tabela.itertuples()
    ]
    sql = text("""
        INSERT INTO indicadores (serie, data, valor)
        VALUES (:serie, :data, :valor) AS novo
        ON DUPLICATE KEY UPDATE valor = novo.valor
    """)
    with conectar().begin() as conexao:
        conexao.execute(sql, registros)
    return len(registros)


if __name__ == "__main__":
    with conectar().connect() as conexao:
        print(conexao.execute(text("SELECT COUNT(*) FROM indicadores")).scalar())
