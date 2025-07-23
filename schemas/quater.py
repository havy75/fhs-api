from pydantic import BaseModel

class Quarter(BaseModel):
    FirstMonth: float
    SecondMonth: float
    ThirdMonth: float
    Percentage: float
    Work: float
    Pay: float
