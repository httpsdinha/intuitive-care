# Intuitive Care - Sistema de Busca de Operadoras

Este repositório foi desenvolvido como parte de um **teste de nivelamento para estágio na Intuitive Care**.

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas:

- **1. Web Scraping**: Scripts para extração de dados de fontes públicas.
- **2. Transformação de Dados**: Scripts para processamento e transformação de dados.
- **3. Banco de Dados**: Scripts SQL e Python para manipulação e carregamento de dados em um banco de dados PostgreSQL.
- **4. Teste de API**: Contém o backend (API) e o frontend para busca de operadoras.

## Funcionalidades

- **Backend**:
  - API desenvolvida com FastAPI para busca de operadoras.
  - Suporte a filtros por estado (UF) e limite de resultados.
  - Integração com arquivos CSV para carregamento de dados.

- **Frontend**:
  - Interface desenvolvida com Vue.js para busca e exibição de operadoras.
  - Filtros dinâmicos e exibição de resultados em tempo real.

- **Ferramentas Auxiliares**:
  - Scripts para web scraping e transformação de dados.
  - Scripts SQL para análise e carregamento de dados em banco de dados.

## Como Executar

### Backend
1. Acesse a pasta `4. Teste de API/Backend`.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Adicione o arquivo `Relatorio_cadop.csv` na pasta `data`.
4. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
   O backend estará disponível em `http://127.0.0.1:8000`.

### Frontend
1. Acesse a pasta `4. Teste de API/frontend`.
2. Instale as dependências:
   ```bash
   npm install
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run serve
   ```
   O frontend estará disponível em `http://localhost:8080`.

### Banco de Dados
1. Acesse a pasta `3. Banco de Dados`.
2. Execute o script `script.py` para pré-processar os arquivos CSV.
3. Utilize os comandos SQL do arquivo `Script-1.sql` para criar e popular as tabelas no PostgreSQL.

### Web Scraping
1. Acesse a pasta `1. Web Scraping`.
2. Execute o script `webScraping.py` para baixar os arquivos necessários.

### Transformação de Dados
1. Acesse a pasta `2. Transformação de Dados`.
2. Execute o script `data.py` para processar os arquivos PDF e gerar os arquivos CSV.

## Documentação

- [Backend](./4.%20Teste%20de%20API/Backend/README.md)
- [Frontend](./4.%20Teste%20de%20API/frontend/README.md)
- [Banco de Dados](./3.%20Banco%20de%20dados/README.md)

## Tecnologias Utilizadas

- **Backend**: FastAPI, Pandas, FuzzyWuzzy
- **Frontend**: Vue.js
- **Banco de Dados**: PostgreSQL
- **Outros**: Python, JavaScript, HTML, CSS

## Observações

Este projeto foi desenvolvido com o objetivo de demonstrar habilidades técnicas e organizacionais. Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato.

---
**Desenvolvido por Amanda**
