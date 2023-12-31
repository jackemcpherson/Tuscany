from datetime import datetime
from typing import List

from pydantic import BaseModel


class Transaction(BaseModel):
    transaction_date: datetime
    description: str
    debit: float = None  # Either debit or credit will be None
    credit: float = None  # Either debit or credit will be None


class Account(BaseModel):
    name: str
    initial_balance: float
    transactions: List[Transaction] = []
