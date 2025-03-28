from pydantic import BaseModel

class OperadoraResponse(BaseModel):
    registro_ans: str | None
    nome_fantasia: str | None
    score: float | None