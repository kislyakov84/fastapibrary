from pydantic import BaseModel
from datetime import date
from typing import Optional

class LoanBase(BaseModel):
    book_id: int
    reader_id: int
    loan_date: Optional[date] = None
    return_date: Optional[date] = None
    
class LoanCreate(LoanBase):
    pass

class LoanResponse(LoanBase):
    id: int
    
    class Config:
        orm_mode = True