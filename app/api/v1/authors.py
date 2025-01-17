from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorResponse
from app.api.database import get_db

router = APIRouter()

@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()