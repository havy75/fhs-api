from fastapi import APIRouter, Depends, HTTPException, status
from schemas.salary import SalaryResp
from services.hrs_api import get_salary_by_empid

router = APIRouter()

@router.get("/{empid}/{year}/{month}", response_model=SalaryResp)
def get_salary(empid: str, year: str, month: str):
    try :
        data = get_salary_by_empid(empid, year, month)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ: " + str(e))