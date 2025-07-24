from pydantic import BaseModel, Field

class ArchivementResp(BaseModel):
    year: str
    score: str
