from pydantic import BaseModel

class QuarterResp(BaseModel):
    FirstMonth: float
    SecondMonth: float
    ThirdMonth: float
    Percentage: float
    Work: float
    Pay: float
