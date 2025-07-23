from fastapi import APIRouter, Depends, HTTPException, status
from schemas.employee import EmployeeBase


from services.hrs_api import get_employee_by_keyword  

router = APIRouter()

@router.get("/{empid}", response_model=EmployeeBase)
def get_employee(empid: str):
    data = get_employee_by_keyword(empid)
    if not data:
        return {"error": "Không tìm thấy nhân viên"}
    return data