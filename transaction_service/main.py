from fastapi import FastAPI

from .models import Transaction

app = FastAPI()

transactions_db = []


@app.post("/transactions/")
def create_transaction(transaction: Transaction):
    transactions_db.append(transaction.model_dump())
    return {"status": "transaction added", "transaction_id": len(transactions_db) - 1}


@app.get("/transactions/{transaction_id}")
def read_transaction(transaction_id: int):
    transaction = transactions_db[transaction_id]
    return transaction
