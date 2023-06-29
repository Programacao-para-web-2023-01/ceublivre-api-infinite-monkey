from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic.dataclasses import Generator

from app.schemas.payment_method import PaymentMethodCreate, PaymentMethodBase
from app.utils.database import Base, engine, SessionLocal

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

Base.metadata.create_all(bind=engine)


def get_db() -> Generator:
    """
    Retorna a sessão de conexão do banco de dados.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_payment_method(product: PaymentMethodCreate, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.get("/")
def read_categories(product: PaymentMethodBase, db: Session = Depends(get_db)):
    return {"id": 0,
            "name": "teste",
            "description": "",
            "payment_method": "",
            "price": 0.00}


@router.get("/{payment_method_id}")
def read_payment_method(payment_method_id: int, product: PaymentMethodBase, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.put("/{payment_method_id}")
def update_payment_method(payment_method_id: int, product: PaymentMethodBase, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.delete("/{payment_method_id}")
def delete_payment_method(payment_method_id: int, product: PaymentMethodBase, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.get("/{payment_method_id}/products")
def read_payment_method_products(payment_method_id: int, product: PaymentMethodBase, db: Session = Depends(get_db)):
    return {}