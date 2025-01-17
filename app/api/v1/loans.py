from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.loan import Loan
from app.models.book import Book
from app.schemas.loan import LoanCreate, LoanResponse
from app.api.database import get_db

router = APIRouter()

@router.post("/", response_model=LoanResponse)
def issue_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == loan.book_id).first()
    if not book or book.available_copies < 1:
        raise HTTPException(status_code=400, detail="Book is not available")
    
    book.available_copies -= 1
    new_loan = Loan(**loan.dict())
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan