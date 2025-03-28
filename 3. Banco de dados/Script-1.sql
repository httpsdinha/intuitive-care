--CRIAÇÃO DA TABELA E EXPORTAÇÃO DE DADO
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

BEGIN;
--colocar esse comando no psql e verificar diretório do arquivo .csv
\copy operadoras_ativas FROM 'C:/temp/Relatorio_cadop.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')

--QUETY ANALITICA

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE not NULL,
    registro_ans INTEGER not NULL,
    conta_contabil VARCHAR(100),
    descricao TEXT,
    saldo_inicial NUMERIC(15,2), 
    saldo_final NUMERIC(15,2),
    constraint uk_reg_ans_conta UNIQUE(registro_ans, conta_contabil, data)
);



-- Comando apenas para o psql
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P1T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/1T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P2t2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P2T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P3T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P3T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P4T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis FROM 'C:/temp/contabeis/P4T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')



COMMIT;

\copy demonstracoes_contabeis(data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P1T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')

drop table demonstracoes_contabeis ;

