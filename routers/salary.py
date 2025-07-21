from fastapi import APIRouter, Depends, HTTPException, status
from schemas.salary import SalaryResponse
from services.hrs_api import get_salary_by_empid

router = APIRouter()

@router.get("/salary/{keyword}/{year}/{month}", response_model=SalaryResponse)
def get_salary(keyword: str, year: str, month: str):
    data = get_salary_by_empid(keyword, year, month)
    if not data:
        return {"error": "Không tìm thấy nhân viên"}
    return data