from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.api.database import Base

# Таблица для связи книг с авторами
book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True)
)

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    publication_date = Column(Date)
    available_copies = Column(Integer, default=0)
    
    authors = relationship("Author", secondary=book_author, back_populates="books")