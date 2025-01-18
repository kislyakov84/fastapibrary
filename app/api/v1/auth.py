from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import timedelta

from app.api.security import ACCESS_TOKEN_EXPIRE_MINUTES, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from app.models.user import User
from app.schemas.auth import Token, UserLogin
from app.api.database import get_db

router = APIRouter()

def authenticate_user(db: Session, username: str, password: str) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

@router.post("/login", response_model=Token)
def login_for_access_token(user_login: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)    
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=30)
        )
    return {"access_token": access_token, "token_type": "bearer"}