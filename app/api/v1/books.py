from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import book
from app.models.book import Book
from app.schemas.book import BookCreate, BookResponse, BookUpdate
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

@router.get("/{book_id}", response_model=list[BookResponse])
def get_books(book_id:int, db: Session = Depends(get_db)):
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int, 
    book_update: BookUpdate,
    db: Session = Depends(get_db)
    ):
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book_update.dict(exclude_unset=True).Items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": f"Boo with id {book_id} deleted"}
    
