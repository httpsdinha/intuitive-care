/*--tabela de operadoras
CREATE TABLE operadoras_ativas(
    registro_ans VARCHAR(20),
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    data_registro_ans DATE
);
ALTER TABLE operadoras_ativas ADD COLUMN regiao_de_comercializacao VARCHAR(20);
ALTER TABLE operadoras_ativas ALTER COLUMN registro_ans TYPE VARCHAR(50);
ALTER TABLE operadoras_ativas ALTER COLUMN cnpj TYPE VARCHAR(20), ALTER COLUMN nome_fantasia TYPE VARCHAR(300), ALTER COLUMN email TYPE VARCHAR(150);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(20),
    conta_contabil VARCHAR(100),
    descricao TEXT,
    saldo_final NUMERIC(15,2)
);

--importação do arquivo .csv, colocar o arquivo .csv dentro de uma pasta temporaria para rodar
\copy operadoras_ativas FROM 'C:/temp/Relatorio_cadop.csv'
    WITH (
        FORMAT csv,
        DELIMITER ';',
        HEADER true,
        ENCODING 'UTF8',
        NULL ''
    );

DROP TABLE IF EXISTS demonstracoes_contabeis;
DROP TABLE IF EXISTS operadoras_ativas;*/


--tabela de operadoras
CREATE TABLE operadoras_ativas(
    registro_ans VARCHAR(50) PRIMARY KEY,
    cnpj VARCHAR(20) NOT NULL UNIQUE,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(300),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(150),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao VARCHAR(20),
    data_registro_ans DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(50) REFERENCES operadoras_ativas(registro_ans),
    conta_contabil VARCHAR(100),
    descricao TEXT,
    saldo_final NUMERIC(15,2)
);

BEGIN;
--colocar esse comando no psql e verificar diretório do arquivo .csv
\copy operadoras_ativas FROM 'C:/temp/Relatorio_cadop.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
