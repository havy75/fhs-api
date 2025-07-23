from fastapi import APIRouter, Depends, HTTPException, status
from schemas.yearbonus import YearBonus
from services.hrs_api import get_year_bonus_by_empid

router = APIRouter()

@router.get("/{empid}/{year}", response_model=YearBonus)
def get_year_bonus(empid: int, year: int):
    try:
        data = get_year_bonus_by_empid(empid, year)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ: " + str(e))