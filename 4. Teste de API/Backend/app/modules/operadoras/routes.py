from fastapi import APIRouter, Query, Depends
from pydantic import BaseModel
from typing import Optional
from .repository import OperadoraRepository
from .schemas import OperadoraResponse

router = APIRouter()

class BuscarOperadorasRequest(BaseModel):
    termo: str
    limite: int = 5
    uf: Optional[str] = None

@router.post("/", response_model=list[OperadoraResponse])
async def buscar_operadoras(
    request: BuscarOperadorasRequest,
    repo: OperadoraRepository = Depends(OperadoraRepository)
):
    return repo.buscar(request.termo, request.limite, request.uf)

#teste uvicorn app.main:app --reload