from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database import Base

class Loan(Base):
    __tablename__ = "loans"
    
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    loan_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    
    # Связь с книгой через book_id
    book = relationship("Book", back_populates="loans")
    
    # Связь с читателем через reader_id
    reader = relationship("User", back_populates="loans")