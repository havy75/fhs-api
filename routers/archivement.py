from fastapi import APIRouter, Depends, HTTPException, status
from schemas.archivement import ArchivementResponse
from typing import List

from services.hrs_api import get_archivement_by_empid  

router = APIRouter()

@router.get("/employee/{keyword}", response_model=List[ArchivementResponse])
def get_employee(keyword: str):
    data = get_archivement_by_empid(keyword)
    if not data:
        return {"error": "Không tìm thấy nhân viên"}
    return data