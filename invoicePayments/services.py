import json

from fastapi import APIRouter
from repository import load_json
from helpers import normalize_invoice_data, reconcile_invoices_and_payments

router = APIRouter()

@router.get("/invoices")
async def get_invoices():
    invoices = load_json("data/invoices.json")
    return normalize_invoice_data(invoices)

@router.get("/payments")
async def get_payments():
    payments = load_json("data/payments.json")
    return payments

@router.get("/reconcile")
async def reconcile():
    invoices = load_json("data/invoices.json")
    payments = load_json("data/payments.json")
    normalized_invoices = normalize_invoice_data(invoices)
    reconciled_invoices = reconcile_invoices_and_payments(normalized_invoices, payments)
    return reconciled_invoices

@router.post("/invoices")
async def create_invoice(invoice_data: dict):
    invoices = load_json("data/invoices.json")
    invoices.append(invoice_data)
    with open("data/invoices.json", "w") as f:
        json.dump(invoices, f, indent=4)
    return {"message": "Invoice created successfully."}

@router.put("/invoices/{invoice_id}")
async def update_invoice(invoice_id: str, updated_data: dict):
    invoices = load_json("data/invoices.json")
    for invoice in invoices:
        if invoice.get("invoice_id") == invoice_id:
            invoice.update(updated_data)
            with open("data/invoices.json", "w") as f:
                json.dump(invoices, f, indent=4)
            return {"message": "Invoice updated successfully."}
    return {"error": "Invoice not found."}

@router.delete("/invoices/{invoice_id}")
async def delete_invoice(invoice_id: str): 
    invoices =load_json("data/invoices.json")
    for i,invoice in enumerate(invoices):
        if invoice.get("invoice_id")==invoice_id:
            del invoices[i]
            with open("data/invoices.json", "w") as f:
                json.dump(invoices, f, indent=4)
            return {"message" : f"Invoice {invoice_id} deleted successfully"}
    return {"error" : "Invoice not found"}


                
                