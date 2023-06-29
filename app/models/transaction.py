from typing import List

from sqlalchemy import Column, Integer, String, Mapped, DateTime, Float  # type: ignore
from sqlalchemy.orm import relationship

from app.utils.database import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id: Column(Integer, primary_key=True, index=True)
    value: Column(Float)
    datetime: Column(DateTime)
    status: Column(String)
    payment_method: Mapped[List["PaymentMethod"]] = relationship(back_populates="transaction")