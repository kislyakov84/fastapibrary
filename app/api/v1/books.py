from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookResponse
from app.api.database import get_db
from app.api.security import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book(
    book: BookCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()