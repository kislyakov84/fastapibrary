from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.logging import log_action
from app.models import book
from app.models.book import Book
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.api.database import get_db
from app.api.security import admin_required, get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book(
    book: BookCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required),
):
    log_action(current_user, f"Created book: {book.title}")
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/", response_model=list[BookResponse])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Book).offset(skip).limit(limit).all()

@router.get("/search/")
def search_books(title: str, db: Session = Depends(get_db)):
    return db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()


@router.get("/{book_id}", response_model=list[BookResponse])
def get_book(book_id:int, db: Session = Depends(get_db)):
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
    
