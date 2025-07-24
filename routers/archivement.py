from fastapi import APIRouter, Depends, HTTPException, status
from schemas.archivement import ArchivementResp
from typing import List

from services.hrs_api import get_archivement_by_empid  

router = APIRouter()

@router.get("/{empid}", response_model=List[ArchivementResp])
def get_archivement(empid: str):
    data = get_archivement_by_empid(empid)
    if not data:
        return {"error": "Không tìm thấy nhân viên"}
    return data