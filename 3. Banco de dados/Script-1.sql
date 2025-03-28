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
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P1T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P1T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P2t2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P2T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P3T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P3T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P4T2024.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')
\copy demonstracoes_contabeis (data, registro_ans, conta_contabil, descricao, saldo_inicial, saldo_final) FROM 'C:/temp/contabeis/P4T2023.csv' WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '')



COMMIT;

--QUETY ANALITICA

--10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre? 

with ultimo_trimestre as (
	select MAX(data) as data_maxima
	from demonstracoes_contabeis
)
select 
	o.razao_social, 
	o.nome_fantasia, 
	o.uf, 
	SUM(d.saldo_final - d.saldo_inicial) as total_despesas

from
	demonstracoes_contabeis d
join 	
	operadoras_ativas o on d.registro_ans::VARCHAR = o.registro_ans
cross join
	ultimo_trimestre
where d.descricao ilike '%EVENTOS/SINISTRO CONHECIDOS OU AVISADOS DE ASSIST%' 
	or d.descricao ilike '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSIST%'
	and d.data >= (ultimo_trimestre.data_maxima - INTERVAL '3 months')
group by
	o.razao_social, o ,nome_fantasia, o.uf
order by
	total_despesas desc
limit 10;

--10 operadoras com maiores despesas nessa categoria no último ano? 

with ultimo_ano as (
	select MAX(data) as data_maxima
	from demonstracoes_contabeis
)
select 
	o.razao_social, 
	o.nome_fantasia, 
	o.uf, 
	SUM(d.saldo_final - d.saldo_inicial) as total_despesas

from
	demonstracoes_contabeis d
join 	
	operadoras_ativas o on d.registro_ans::VARCHAR = o.registro_ans
cross join
	ultimo_ano
where d.descricao ilike '%EVENTOS/SINISTRO CONHECIDOS OU AVISADOS DE ASSIST%' 
	or d.descricao ilike '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSIST%'
	and d.data >= (ultimo_ano.data_maxima - INTERVAL '1 year')
group by
	o.razao_social, o ,nome_fantasia, o.uf
order by
	total_despesas desc
limit 10;

