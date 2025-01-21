from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorResponse, AuthorUpdate
from app.api.database import get_db

router = APIRouter()

# Создание автора
@router.post("/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

# Получение всех авторов
@router.get("/", response_model=list[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

# Получение автора по ID
@router.put("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Обновление автора
@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author_update: AuthorUpdate, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")    
    for key, value in author_update.dict(exclude_unset=True).items():
        setattr(author, key, value)        
    db.commit()
    db.refresh(author)
    return author

# Удаление автора
@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return {"message": f"Author with id {author_id} deleted"}