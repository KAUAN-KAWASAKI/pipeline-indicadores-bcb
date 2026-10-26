CREATE DATABASE IF NOT EXISTS indicadores_bcb;

USE indicadores_bcb;

CREATE TABLE IF NOT EXISTS indicadores (
    serie  VARCHAR(20)    NOT NULL,
    data   DATE           NOT NULL,
    valor  DECIMAL(12,4)  NOT NULL,
    PRIMARY KEY (serie, data)
);
