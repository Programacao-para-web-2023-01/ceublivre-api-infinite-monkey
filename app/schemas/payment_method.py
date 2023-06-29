from pydantic import BaseModel


class PaymentMethodBase(BaseModel):
    type: str
    service: str


class PaymentMethodCreate(BaseModel):
    type: str
    service: str