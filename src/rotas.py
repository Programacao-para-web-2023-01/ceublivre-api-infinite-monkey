from fastapi import APIRouter
from src.endpoints import pagamentos

api_router = APIRouter()

api_router.include_router(pagamentos.router, prefix='/pagamentos', tags=['payment'])
