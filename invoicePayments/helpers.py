def normalize_invoice_data(invoices):
    normalized_invoices = []
    for i, invoice in enumerate(invoices):
        if invoice.get("amount") is None:
            print(f"Warning: Invoice at index {i} has a null amount. Setting to 0.")
        else:
            try:
                invoice["amount"] = float(invoice.get("amount", 0))
            except ValueError:
                print(f"Warning: Invoice at index {i} has a non-numeric amount. Setting to 0.")
                invoice["amount"] = 0
            normalized_invoice = {
                "invoice_id": invoice.get("invoice_id"),
                "vendor": invoice.get("vendor").strip().lower(),
                "amount": float(invoice.get("amount", 0)),
                "status": invoice.get("status").strip().upper(),
                "date": invoice.get("date", "1970-01-01")
            }
        normalized_invoices.append(normalized_invoice)
    normalized_invoices=remove_duplicate_invoices(normalized_invoices)
    suspected_duplicates(normalized_invoices)
    normalized_invoices=invoice_cancel(normalized_invoices)
    return normalized_invoices

def remove_duplicate_invoices(invoices):
    seen = set()
    unique_invoices = []
    for invoice in invoices:
        invoice_id = invoice.get("invoice_id")
        if invoice_id not in seen :
            seen.add(invoice_id)
            unique_invoices.append(invoice)
    return unique_invoices

def suspected_duplicates(invoices):
    duplicates = []
    seen = {}
    for i, invoice in enumerate(invoices):
         if invoice.get("vendor") in seen:
             duplicates = check_duplicate(invoices,invoice, seen[invoice.get("vendor")], duplicates)
         else:
            seen[invoice.get("vendor")] = invoice.get("invoice_id")
    print(f"Suspected duplicates: {duplicates}")

def check_duplicate(invoices, invoice, seen_invoice_id, duplicates):
    for inv in invoices:
        if inv.get("invoice_id") == seen_invoice_id:
            if invoice.get("amount") == inv.get("amount") and invoice.get("date") == inv.get("date"):
                duplicates.append(f"{invoice.get("invoice_id")} ` {inv.get("invoice_id")}")
    return duplicates

def invoice_cancel(invoices):
    for invoice in invoices:
        if invoice.get("amount") < 0:
            is_cancelled, invoice_id, invoices = invoice_cancellation(invoices, invoice.get("vendor"),invoice.get("amount"))
            if is_cancelled:
                invoice["status"] = "CANCELLED"
                print(f"Invoice {invoice_id} and {invoice.get('invoice_id')} has been cancelled.")
    return invoices

def invoice_cancellation(invoices, vendor, amount):
    for invoice in invoices:
        if invoice.get("vendor") == vendor and invoice.get("amount") == abs(amount):
            invoice["status"] = "CANCELLED"
            return (True, invoice.get("invoice_id"),invoices)
        else:
            return (False, None,invoices)

def reconcile_invoices_and_payments(invoices, payments):
    for invoice in invoices:
        if invoice.get("status") == "PAID":
            continue
        for payment in payments:
            if (invoice.get("invoice_id") == payment.get("invoice_id") and
                invoice.get("amount") == payment.get("paid") ):
                invoice["status"] = "PAID"
                print(f"Invoice {invoice.get('invoice_id')} has been reconciled with payment {payment.get('payment_id')}.")
                break
    return invoices