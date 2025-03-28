from fastapi import APIRouter, Query, Depends
from pydantic import BaseModel
from .repository import OperadoraRepository
from .schemas import OperadoraResponse

router = APIRouter()
class BuscarOperadorasRequest(BaseModel):
    termo: str
    limite: int = 5
    
@router.post("/", response_model=list[OperadoraResponse])
async def buscar_operadoras(
    request: BuscarOperadorasRequest,
    repo: OperadoraRepository = Depends(OperadoraRepository)  # Corrigido para instanciar a dependência
):
    return repo.buscar(request.termo, request.limite)

#teste uvicorn app.main:app --reload