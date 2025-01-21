from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="your_email@example.com",
    MAIL_PASSWORD="your_password",
    MAIL_FROM="your_email@example.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.example.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

async def send_email_notification(email: str, message: str):
    msg = MessageSchema(
        subject="Library Book Return Reminder",
        recipients=[email],
        body=message,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(msg)