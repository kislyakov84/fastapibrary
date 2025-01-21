from fastapi import FastAPI
from app.api.v1 import users, books, authors, loans, auth
from fastapi import BackgroundTasks
from app.models.loan import Loan
from sqlalchemy.orm import Session
from datetime import timedelta, datetime
from app.api.notifications import send_email_notification
from fastapi import BackgroundTasks

app = FastAPI()

# регистрация маршрутов
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(loans.router, prefix="/loans", tags=["loans"])
app.include_router(auth.router, tags=["auth"])

def check_loans_for_reminders(db: Session):
    today = datetime.utcnow().date()
    reminder_date = today + timedelta(days=3)
    loans = db.query(Loan).filter(Loan.return_date == reminder_date).all()

    for loan in loans:
        message = f"Reminder: Please return the book '{loan.book.title}' by {loan.return_date}."
        send_email_notification(loan.reader.email, message)