from fastapi import FastAPI, HTTPException
from typing import Optional
from .models import Account, Transaction

app = FastAPI()
accounts_db = {}

@app.post("/accounts/")
def create_account(account: Account):
    account_name = account.name
    accounts_db[account_name] = account.model_dump()
    return {"status": "account created", "account_name": account_name}

@app.get("/accounts/{account_name}")
def read_account(account_name: str):
    account = accounts_db.get(account_name)
    return account

@app.put("/accounts/{account_name}")
def update_account(account_name: str, account: Account):
    if account_name not in accounts_db:
        return {"error": "Account not found"}
    accounts_db[account_name] = account.model_dump()
    return {"status": "account updated"}

@app.delete("/accounts/{account_name}")
def delete_account(account_name: str):
    if account_name not in accounts_db:
        return {"error": "Account not found"}
    del accounts_db[account_name]
    return {"status": "account deleted"}

@app.post("/accounts/{account_name}/transactions/")
def add_transaction(account_name: str, transaction: Transaction):
    account = accounts_db.get(account_name)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    account['transactions'].append(transaction.model_dump())
    return {"status": "transaction added"}

@app.get("/accounts/{account_name}/transactions/")
def list_transactions(account_name: str):
    account = accounts_db.get(account_name)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account['transactions']

@app.get("/accounts/{account_name}/transactions/{transaction_id}")
def get_transaction(account_name: str, transaction_id: int):
    account = accounts_db.get(account_name)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        return account['transactions'][transaction_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Transaction not found")

@app.put("/accounts/{account_name}/transactions/{transaction_id}")
def update_transaction(account_name: str, transaction_id: int, transaction: Transaction):
    account = accounts_db.get(account_name)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        account['transactions'][transaction_id] = transaction.model_dump()
    except IndexError:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"status": "transaction updated"}

@app.delete("/accounts/{account_name}/transactions/{transaction_id}")
def delete_transaction(account_name: str, transaction_id: int):
    account = accounts_db.get(account_name)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    try:
        del account['transactions'][transaction_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"status": "transaction deleted"}
