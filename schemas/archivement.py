from pydantic import BaseModel, Field

class ArchivementResponse(BaseModel):
    year: str
    score: str
    
class ArchivementListResponse(BaseModel):
    data: list[ArchivementResponse]