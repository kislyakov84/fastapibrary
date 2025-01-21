from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    publication_date: Optional[date] = None
    available_copies: int
    
class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    
    class Config:
        orm_mode = True