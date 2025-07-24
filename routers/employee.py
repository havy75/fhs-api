from fastapi import APIRouter, Depends, HTTPException, status
from schemas.employee import EmployeeResp


from services.hrs_api import get_employee_by_keyword  

router = APIRouter()

@router.get("/{empid}", response_model=EmployeeResp)
def get_employee(empid: int):
    data = get_employee_by_keyword(empid)
    if not data:
        return {"error": "Không tìm thấy nhân viên"}
    return data