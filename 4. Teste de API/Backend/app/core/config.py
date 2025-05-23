from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Busca de Operadoras"
    CSV_PATH: str = "data/Relatorio_cadop.csv"
    
settings = Settings()

# teste python -c "from app.core.config import settings; print(settings.APP_NAME)"
if __name__ == "__main__":
    print("Configurações carregadas:")
    print(f"Nome do App: {settings.APP_NAME}")
    print(f"Caminho do CSV: {settings.CSV_PATH}")