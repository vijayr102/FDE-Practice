import json
from models import Invoice

DATA_FILE = 'data/invoices.json'
with open(DATA_FILE, 'r') as file:
    invoices_data = json.load(file)

invoice_Customer ={}
for index, invoice_dict in enumerate(invoices_data):
    if invoice_dict['customer'] in invoice_Customer:
        print(f"Duplicate customer found at index {index} and {invoice_Customer[invoice_dict['customer']]}  : {invoice_dict['customer']}")
    else:
        invoice_Customer[invoice_dict['customer']] = index