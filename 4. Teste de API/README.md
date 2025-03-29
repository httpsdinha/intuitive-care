# Intuitive Care - API e Frontend

Este projeto contém uma API para busca de operadoras e um frontend para exibir os resultados.

## Como executar o Backend

1. **Instale as dependências do Python**:
   Certifique-se de ter o Python instalado. Em seguida, execute:
   ```bash
   pip install -r Backend/requirements.txt
   ```

2. **Adicione o arquivo CSV**:
   Coloque o arquivo `Relatorio_cadop.csv` no diretório `Backend/data`.

3. **Inicie o servidor**:
   Execute o seguinte comando no diretório `Backend`:
   ```bash
   uvicorn app.main:app --reload
   ```
   O backend estará disponível em `http://127.0.0.1:8000`.

## Como executar o Frontend

1. **Instale as dependências do Node.js**:
   Certifique-se de ter o Node.js instalado. Em seguida, execute:
   ```bash
   cd frontend
   npm install
   ```

2. **Inicie o servidor de desenvolvimento**:
   Execute o seguinte comando no diretório `frontend`:
   ```bash
   npm run serve
   ```
   O frontend estará disponível em `http://localhost:8080`.

## Fluxo de Uso

1. Acesse o frontend em `http://localhost:8080`.
2. Utilize a barra de busca para pesquisar operadoras.
3. Os resultados serão exibidos com base nos dados fornecidos pelo backend.

## Observações

- Certifique-se de que o backend esteja rodando antes de iniciar o frontend.
- O backend utiliza o arquivo CSV para realizar as buscas, então é essencial que o arquivo esteja no local correto.
- Caso encontre problemas, verifique os logs do terminal para identificar possíveis erros.

