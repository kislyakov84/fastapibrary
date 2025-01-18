from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.api.database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    biography = Column(String)
    birth_date = Column(Date)
    
    # Связь с книгами через таблицу book_author
    books = relationship("Book", secondary="book_author", back_populates="authors") 
    