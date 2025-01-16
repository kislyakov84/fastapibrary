from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Настройки базы данных
DATABASE_URL = "postgresql+psycopg2://coder:password@localhost:5432/library_db"

# Создание подключения
engine = create_engine(DATABASE_URL)

# Создание сессии для взаимодействия с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для декларативных моделей
Base = declarative_base()

# Зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()