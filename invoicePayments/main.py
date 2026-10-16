from services import router as invoice_payments_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(invoice_payments_router)