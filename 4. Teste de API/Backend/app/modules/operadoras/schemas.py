from pydantic import BaseModel

class OperadoraResponse(BaseModel):
    registro_ans: str | None
    nome_fantasia: str | None
    score: float | None
    
    
    
# teste
if __name__ == "__main__":
    exemplo = OperadoraResponse(
        registro_ans="12345",
        nome_fantasia="Amil Saúde",
        score=95.0
    )
    print(exemplo.json(indent=2))