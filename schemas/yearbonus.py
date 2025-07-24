from pydantic import BaseModel
from typing import Optional

class YearBonusResp(BaseModel):
    id: Optional[int] = None
    mnv: Optional[str] = None           # Mã nhân viên
    tlcb: Optional[str] = None          # Tỷ lệ cơ bản
    stdltbtn: Optional[str] = None      # Số tiền được lĩnh theo bậc thang
    capbac: Optional[str] = None        # Cấp bậc
    tile: Optional[str] = None          # Tỷ lệ
    ktsongay: Optional[str] = None      # Khen thưởng số ngày
    ktsotien: Optional[str] = None      # Khen thưởng số tiền
    xpsongay: Optional[str] = None      # Xử phạt số ngày
    xpsotien: Optional[str] = None      # Xử phạt số tiền
    stienthuong: Optional[str] = None   # Số tiền thưởng
    tpnttt: Optional[str] = None        # Thưởng phạt nội tình thực tế
    tpntst: Optional[str] = None        # Thưởng phạt nội tình số tiền

    class Config:
        from_attributes = True  # nếu bạn dùng với ORM như SQLAlchemy
