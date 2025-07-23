from fastapi import APIRouter, Depends, HTTPException, status
from schemas.quater import Quarter
from services.hrs_api import get_quater_by_empid

router = APIRouter()

from fastapi import HTTPException

@router.get("/quater/{keyword}/{year}/{quater}", response_model=Quarter)
def get_quater(keyword: str, year: int, quater: int):
    try:
        data = get_quater_by_empid(keyword, year, quater)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ: " + str(e))
