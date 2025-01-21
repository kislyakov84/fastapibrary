from sqlalchemy import Column, Integer, String
from app.api.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="reader") # роль пользователя (администратор или читатель)
    loans = relationship("Loan", back_populates="reader") # Связь с выдачами книг (loan)