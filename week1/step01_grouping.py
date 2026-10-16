import json
from models import Invoice

DATA_FILE = 'data/invoices.json'

with open(DATA_FILE, 'r') as file:
    invoices_data = json.load(file)

customer_invoice_total = {}
for invoice_dict in invoices_data:
    invoice = Invoice(**invoice_dict)
    customer_invoice_total[invoice.customer] = customer_invoice_total.get(invoice.customer, 0) + invoice.amount

print(customer_invoice_total)