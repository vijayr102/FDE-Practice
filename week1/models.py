from pydantic import BaseModel

class Invoice(BaseModel):
    id: int
    customer: str
    amount: float
    status: str
