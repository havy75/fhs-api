# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class EmployeeResp(BaseModel):
    chinese_name: Optional[str]
    vietnamese_name: Optional[str]
    date_of_birth: Optional[date]
    date_of_joining: Optional[date]
    department: Optional[str]
    position: Optional[str]
    date_of_appointment: Optional[date]
    rank: Optional[str]
    rank_start_date: Optional[date]
    employee_id: Optional[str]
    last_updated: Optional[date]
    room_code: Optional[str]
    effective_date: Optional[date]
    basic_salary: Optional[float]
    contract_date: Optional[date]
    official_date: Optional[date]
    exp_date: Optional[date]
    current_address: Optional[str]
    household_registration: Optional[str]
    phone_1: Optional[str]
    phone_2: Optional[str]
    spouse_name: Optional[str]

class EmployeeCreate(EmployeeResp):
    pass  # Bạn có thể thêm field bắt buộc nếu cần

class EmployeeUpdate(EmployeeResp):
    pass  # Dùng cho cập nhật nhân viên

class EmployeeResponse(EmployeeResp):
    id: int

    class Config:
        from_attributes  = True
