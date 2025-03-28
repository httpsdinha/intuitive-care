import pandas as pd
from fuzzywuzzy import fuzz
from app.core.config import settings


class OperadoraRepository:
    def __init__(self):
        self._data = self._load_data()

    def _load_data(self) -> pd.DataFrame:
        return pd.read_csv(settings.CSV_PATH, delimiter=';').astype(str)

    def buscar(self, termo: str, limite: int = 5) -> list[dict]:
        resultados = []
        for _, row in self._data.iterrows():
            score = fuzz.token_set_ratio(termo.lower(), " ".join(row.values).lower())
            if score > 50:
                resultados.append({**row.to_dict(), "score": score})
        return sorted(resultados, key=lambda x: x["score"], reverse=True)[:limite]

# teste
if __name__ == "__main__":
    repo = OperadoraRepository()
    print("Primeira linha do CSV:", repo._data.iloc[0].to_dict())
    print("Busca por 'Amil':", repo.buscar("Amil", 1))