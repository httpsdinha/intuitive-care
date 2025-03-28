from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Busca de Operadoras"
    CSV_PATH: str = "data/Relatorio_cadop.csv"
    
settings = Settings()