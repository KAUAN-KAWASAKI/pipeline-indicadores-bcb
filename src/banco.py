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
        database=os.getenv("DB_NAME"),
    )
    return create_engine(endereco)


if __name__ == "__main__":
    with conectar().connect() as conexao:
        print(conexao.execute(text("SELECT COUNT(*) FROM indicadores")).scalar())
