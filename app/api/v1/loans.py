from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.loan import Loan
from app.models.book import Book
from app.schemas.loan import LoanCreate, LoanResponse, LoanUpdate
from app.api.database import get_db
from datetime import date

router = APIRouter()

# Выдача книги
@router.post("/", response_model=LoanResponse)
def issue_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == loan.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book is not found")    
    if book.available_copies < 1:
        raise HTTPException(status_code=400, detail="No available copies of this book")    
    new_loan = Loan(**loan.dict())
    book.available_copies -= 1 # Уменьшаем доступное количество копий
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan

# Возврат книги
@router.put("/{loan_id}/return", response_model=LoanResponse)
def return_loan(loan_id: int, loan_update: LoanUpdate, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan is not found")
    if loan.return_date is not None:
        raise HTTPException(status_code=400, detail="Loan is already returned")
    loan.return_date = loan_update.return_date
    
    # Увеличиваем количество доступных копий после возврата
    book = db.query(Book).filter(Book.id == loan.book_id).first()
    if book:
            book.available_copies += 1
    db.commit()
    db.refresh(loan)
    return loan

# Удаление записи  о выдаче
@router.delete("/{loan_id}")
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan is not found")
    db.delete(loan)
    db.commit()
    return {"message": f"Loan with id {loan_id} deleted"}
