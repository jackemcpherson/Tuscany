from fastapi import FastAPI
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
