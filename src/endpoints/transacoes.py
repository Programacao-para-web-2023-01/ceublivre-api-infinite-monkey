from fastapi import APIRouter
from repositorio.servicos import buscar_historico
router = APIRouter()

@router.get('/transacoes/{id_conta}')
async def buscar_historico_transacoes(id_conta:int):
    data = buscar_historico(id_conta)
    return {"transacoes":data}

