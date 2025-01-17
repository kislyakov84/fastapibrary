from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.api.database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    biogarphy = Column(String)
    birth_date = Column(Date)
    
    books = relationship("Book", secondary="book_author", back_populates="author") 
    