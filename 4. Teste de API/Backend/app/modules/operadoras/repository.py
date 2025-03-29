import pandas as pd
from fuzzywuzzy import fuzz
from app.core.config import settings
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

class OperadoraRepository:
    def __init__(self):
        self._data = self._load_data()

    def __call__(self):
        return self

    def _load_data(self) -> pd.DataFrame:
        data = pd.read_csv(settings.CSV_PATH, delimiter=';').astype(str)
        print("Loaded columns:", data.columns) 
        return data

    def buscar(self, termo: str, limite: int = 5, uf: str | None = None) -> list[dict]:
        resultados = []
        for _, row in self._data.iterrows():
            if uf and row["UF"].strip().upper() != uf.strip().upper():
                continue
            score = fuzz.token_set_ratio(termo.lower(), " ".join(row.values).lower())
            if score > 50:
                resultados.append({
                    "Registro_ANS": row["Registro_ANS"],
                    "Nome_Fantasia": row["Nome_Fantasia"],
                    "Razao_Social": row["Razao_Social"],
                    "Modalidade": row["Modalidade"],  
                    "Logradouro": row["Logradouro"],  
                    "Telefone": row["Telefone"],     
                    "Cidade": row["Cidade"],          
                    "UF": row["UF"],                 
                    "score": score
                })
        return sorted(resultados, key=lambda x: x["score"], reverse=True)[:limite]

# teste python app/modules/operadoras/repository.py
if __name__ == "__main__":
    repo = OperadoraRepository()
    print("Primeira linha do CSV:", repo._data.iloc[0].to_dict())
    print("Busca por 'Amil':", repo.buscar("Amil", 1))