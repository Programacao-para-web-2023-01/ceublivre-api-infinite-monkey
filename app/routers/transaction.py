from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic.dataclasses import Generator

from app.schemas.transaction import TransactionCreate, TransactionBase
from app.utils.database import Base, engine, SessionLocal

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
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
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    if (transaction.payment_method.type == 'ONLINE_SERVICES') {
        if (transaction.payment_method.service == 'PAYPAL' and app.endpoints.paypal.create_payment(transaction.value, 'R$')) {
            return {"status": "succesful"}
        } elif (transaction.payment_method.service == 'STRIPE' and app.endpoints.stripe.create_payment(transaction.value, 'R$')) {
            return {"status": "succesful"}
        } elif (transaction.payment_method.service == 'WISE' and app.endpoints.wise.create_payment(transaction.value, 'R$')) {
            return {"status": "succesful"}
        }
    }
    return {"status": "failed"}


@router.get("/")
def read_categories(transaction: TransactionBase, db: Session = Depends(get_db)):
    return transaction.toString()


@router.get("/{transaction_id}")
def read_category(transaction_id: int, product: TransactionBase, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.put("/{transaction_id}")
def update_category(transaction_id: int, product: TransactionBase, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.delete("/{transaction_id}")
def delete_category(transaction_id: int, product: TransactionBase, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@router.get("/{transaction_id}/transactions")
def read_category_products(transaction_id: int, product: TransactionBase, db: Session = Depends(get_db)):
    return {}