from fastapi import FastAPI
from app.api.v1 import users

app = FastAPI()

# регистрация маршрутов
app.include_router(users.router, prefix='/users', tags=["users"])