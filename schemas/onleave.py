from pydantic import BaseModel, Field
from typing import Optional


class OnLeaveResp(BaseModel):
    code: Optional[str]
    name: Optional[str]
    quantity: Optional[float]
