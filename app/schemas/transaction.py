from pydantic import BaseModel

class TransactionBase(BaseModel):
    value: int
    datetime: str
    status: str
    payment_method: list[PaymentMethodBase] = []


class TransactionCreate(BaseModel):
    value: int
    datetime: str
    status: str
    payment_method: list[PaymentMethodBase] = []