from fastapi import APIRouter
from repositorio.servicos import buscar_histórico
from src.dominio.pix import PixData
router = APIRouter()

@router.post('/transacoes')
async def buscar_historico_transacoes(id_conta:int):
    data = buscar_histórico(id_conta)
    return {"transacoes":data}

