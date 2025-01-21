from pydantic import BaseModel
from datetime import date
from typing import Optional

class LoanBase(BaseModel):
    book_id: int
    reader_id: int
    loan_date: date
    return_date: Optional[date] = None
    
class LoanCreate(LoanBase):
    pass

class LoanUpdate(LoanBase):
    return_date: date

class LoanResponse(LoanBase):
    id: int
    
    class Config:
        orm_mode = True