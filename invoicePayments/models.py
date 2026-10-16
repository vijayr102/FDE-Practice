from pydantic import BaseModel

class Invoice(BaseModel):
    invoice_id: str
    vendor: str
    amount: float
    status: str
    date: str

class Payment(BaseModel):
    invoice_id: str
    paid: float