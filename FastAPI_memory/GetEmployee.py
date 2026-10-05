from  fastapi import APIRouter
from datastore import Employees

router = APIRouter()

# Employees= [
#     {"id": 1, "name": "John Doe", "position": "Software Engineer"},
#     {"id": 2, "name": "Jane Smith", "position": "Data Scientist"},
#     {"id": 3, "name": "Mike Johnson", "position": "Product Manager"},
#     {"id": 4, "name": "Emily Davis", "position": "UX Designer"},
# ]

@router.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    for employee in Employees:
        if employee["id"] == employee_id:
            return employee
    return {"error": "Employee not found"}

@router.get('/employees')
def get_employees():
    return Employees
