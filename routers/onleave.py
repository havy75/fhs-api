from fastapi import APIRouter, Depends, HTTPException, status
from schemas.onleave import OnLeaveResp
from services.hrs_api import get_on_leave_by_empid
from typing import List


router = APIRouter()

from fastapi import HTTPException

@router.get("/{empid}/{year}", response_model=List[OnLeaveResp])
def get_on_leave(empid: int, year: int):
    try:
        data = get_on_leave_by_empid(empid, year)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ: " + str(e))