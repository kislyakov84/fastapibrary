from pydantic import BaseModel
from datetime import date
from typing import Optional

class AuthorBase(BaseModel):
    name: str
    biography: Optional[str] = None
    birth_date: Optional[date] = None
    
class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    
    class Config:
        orm_mode = True