from fastapi import APIRouter
from src.dominio.pix import PixData

router = APIRouter()

@router.post('/pix')
async def handle_pix_payment(pixData:PixData):
    return { 'data':pixData}

