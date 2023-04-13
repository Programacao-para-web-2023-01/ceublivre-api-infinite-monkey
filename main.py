from fastapi import FastAPI
from src.rotas import api_router

app = FastAPI(title='Infinity Monkey - API')

app.include_router(api_router)