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
    if transaction.payment_method.type == 'ONLINE_SERVICES':
        if transaction.payment_method.service == 'PAYPAL':
            response = paypal.create_payment(transaction.value, 'R$')
            if response.get('status') == 'succesful':
                return {"status": "successful"}
        elif transaction.payment_method.service == 'STRIPE':
            response = stripe.create_payment(transaction.value, 'R$')
            if response.get('status') == 'succesful':
                return {"status": "successful"}
        elif transaction.payment_method.service == 'WISE':
            response = wise.create_payment(transaction.value, 'R$')
            if response.get('status') == 'succesful':
                return {"status": "successful"}
    
    return {"status": "failed"}


@router.get("/")
def read_transactions(db: Session = Depends(get_db)):
    return {"message": "Read all transactions"}


@router.get("/{transaction_id}")
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return {"message": f"Read transaction {transaction_id}"}


@router.put("/{transaction_id}")
def update_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return {"message": f"Update transaction {transaction_id}"}


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return {"message": f"Delete transaction {transaction_id}"}


@router.get("/{transaction_id}/payment-method")
def read_transaction_payment_method(transaction_id: int, db: Session = Depends(get_db)):
    return {"message": f"Read payment method for transaction {transaction_id}"}


@router.get("/{transaction_id}/transactions")
def read_transaction_payment_methods(transaction_id: int, db: Session = Depends(get_db)):
    return {"message": f"Read transactions associated with transaction {transaction_id}"}