# API de Busca de Operadoras

## Como executar
1. `pip install -r requirements.txt`
2. Coloque seu CSV em `data/Relatorio_cadop.csv`
3. `uvicorn app.main:app --reload`

## Rotas
- `GET /api/v1/operadoras/?termo={termo}&limite={5}`