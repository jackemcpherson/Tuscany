from pydantic import BaseModel

class Transaction(BaseModel):
    from_account: str
    to_account: str
    amount: float
