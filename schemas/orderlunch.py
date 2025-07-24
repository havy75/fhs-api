from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime, date

class OrderLunchResp(BaseModel):
    id_emp: str
    name: str
    time: str
    node: str
    dept: str

# class OrderLunchRequest(BaseModel):
#     date: str
#     place: str

#     @field_validator("date", mode="before")
#     @classmethod
#     def validate_date_format(cls, v):
#         try:
#             datetime.strptime(v, "%Y/%m/%d")
#         except ValueError:
#             # Đây là cách đúng: ném ra lỗi rõ ràng để FastAPI hiểu
#             raise ValueError("Sai định dạng ngày. Dùng YYYY/MM/DD")
#         return v