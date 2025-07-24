from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from schemas.orderlunch import OrderLunchResp
from services.hrs_api import get_user_lunch_by_date_place
from datetime import datetime

router = APIRouter()


@router.get("/lunch", response_model=OrderLunchResp)
async def get_user_lunch(
    date: str = Query(..., description="Ngày dạng YYYY/MM/DD"),
    place: str = Query(..., description="Tên địa điểm"),
):

    # Custom validate
    try:
        datetime.strptime(date, "%Y/%m/%d")
    except ValueError:
        raise HTTPException(
            status_code=422, detail="Sai định dạng ngày. Dùng YYYY/MM/DD"
        )

    try:
        return get_user_lunch_by_date_place(date, place)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Lỗi máy chủ: " + str(e))


@router.get("/test")
def test(
    date: str = Query(..., description="Ngày dạng YYYY/MM/DD"),
    place: str = Query(..., description="Tên địa điểm"),
):
    # Custom validate
    try:
        datetime.strptime(date, "%Y/%m/%d")
    except ValueError:
        raise HTTPException(
            status_code=422, detail="Sai định dạng ngày. Dùng YYYY/MM/DD"
        )

    return {"date": date, "place": place}
