from fastapi import APIRouter, Depends, HTTPException, status
from schemas.employee import EmployeeBase


from services.hrs_api import get_employee_by_keyword  

router = APIRouter()

@router.get("/employee/{keyword}", response_model=EmployeeBase)
def get_employee(keyword: str):
    data = get_employee_by_keyword(keyword)
    if not data:
        return {"error": "Không tìm thấy nhân viên"}
    return data