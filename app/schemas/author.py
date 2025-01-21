from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from app.schemas.book import BookResponse

class AuthorBase(BaseModel):
    name: str
    biography: Optional[str] = None
    birth_date: Optional[date] = None
    
class AuthorCreate(AuthorBase):
    pass

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int
    books: List[BookResponse] = []
    
    class Config:
        orm_mode = True