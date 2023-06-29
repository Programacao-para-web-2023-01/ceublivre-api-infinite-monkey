from sqlalchemy import Column, Integer, String, Float, Mapped, ForeignKey  # type: ignore
from sqlalchemy.orm import relationship, mapped_column
from app.utils.database import Base


class PaymentMethod(Base):
    __tablename__ = "payment_method"

    id: Column(Integer, primary_key=True, index=True)
    type: Column(String)
    service: Column(String)
    transaction_id: Mapped[int] = mapped_column(ForeignKey("transaction.id"))
    transaction: Mapped["Transaction"] = relationship(back_populates="transaction")


