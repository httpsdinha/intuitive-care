from pydantic import BaseModel

class OperadoraResponse(BaseModel):
    Registro_ANS: str | None
    Razão_Social: str | None
    Nome_Fantasia: str | None
    score: float | None
    
    class Config:
        allow_population_by_field_name = True


    
# teste python app/modules/operadoras/schemas.py
if __name__ == "__main__":
    exemplo = OperadoraResponse(
        registro_ans="12345",
        nome_fantasia="Amil Saúde",
        score=95.0
    )
    print(exemplo.json(indent=2))