from fastapi import APIRouter, Depends, HTTPException, status
from schemas.quater import QuarterResp
from services.hrs_api import get_quater_by_empid

router = APIRouter()

from fastapi import HTTPException

@router.get("/{empid}/{year}/{quater}", response_model=QuarterResp)
def get_quater(empid: int, year: int, quater: int):
    try:
        data = get_quater_by_empid(empid, year, quater)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ: " + str(e))
