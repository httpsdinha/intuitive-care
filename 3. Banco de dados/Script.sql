--tabela de operadoras
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

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(20),
    conta_contabil VARCHAR(100),
    descricao TEXT,
    saldo_final NUMERIC(15,2)
);

