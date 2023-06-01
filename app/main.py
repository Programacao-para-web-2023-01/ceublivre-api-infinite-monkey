import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.rotas import api_router

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI(title='Infinity Monkey - API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)