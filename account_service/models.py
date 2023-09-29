from pydantic import BaseModel

class Account(BaseModel):
    name: str
    balance: float

class Transaction(BaseModel):
    account_name: str
    type: str  # Either 'credit' or 'debit'
    amount: float
