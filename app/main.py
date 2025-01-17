from fastapi import FastAPI
from app.api.v1 import users, books, authors, loans

app = FastAPI()

# регистрация маршрутов
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(loans.router, prefix="/loans", tags=["loans"])