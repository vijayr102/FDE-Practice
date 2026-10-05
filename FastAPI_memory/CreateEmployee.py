from datastore import Employees
from EmployeeModel import Employee
from fastapi import APIRouter

router = APIRouter()

@router.post("/employee")
def create_employee(employee: Employee):
    new_employee = employee.model_dump()
    Employees.append(new_employee)
    return employee