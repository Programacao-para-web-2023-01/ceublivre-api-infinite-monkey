from pydantic import BaseModel


class ProductBase(BaseModel):
    type: str
    service: str


class ProductCreate(BaseModel):
    type: str
    service: str