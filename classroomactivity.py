"""Classroom Activities

invoice_amount = 50000
invoice_approver => Manager / Supervisor / Director

amount < 1000 -> Sup
amount > 25000 -> Manager 
amount > 50000 -> Manager and Director

1) Write python program using if condition block and convert to match case
2) List of employee id, name, salary and then print only those names with length > 6 and salary < 250000"""

from re import match


invoice_amount = 50000

if invoice_amount < 1000:
    print("Approved by Supervisor")
elif invoice_amount > 25000 and invoice_amount <= 50000:
    print("Approved by Manager")
elif invoice_amount > 50000:
    print("Approved by Manager and Director")
else:
    print("Invoice amount is not in the approval range")

match invoice_amount:
    case amount if amount < 1000:
        print("Approved by Supervisor")
    case amount if amount > 25000 and amount <= 50000:
        print("Approved by Manager")
    case amount if amount > 50000:
        print("Approved by Manager and Director")
    case _:
        print("Invoice amount is not in the approval range")

employees =[{"id":1,"name":"alice","salary":10000},
           {"id":2,"name":"thomson","salary":40000},
           {"id":3,"name":"tom cruise","salary":30000},]

for employee in employees:
     if len(employee["name"])>6 and employee["salary"]>25000:
      print(f"Employee id:{employee["id"]}, Emplyoee name: {employee["name"]}, Employee salary: {employee["salary"]}")
     else:
         print(f"Employee with id {employee["id"]} does not meet the criteria")

