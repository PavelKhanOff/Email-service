from eduone_mail.app.task_app.celery_app import app
from fastapi_mail import FastMail, MessageSchema
from eduone_mail.app.core.config import conf
from pydantic import EmailStr
from eduone_mail.app.core.aws import delete_file


@app.task
async def send_email(
    email: EmailStr, template_body: dict, template_name: str, template_subject: str
):
    message = MessageSchema(
        subject=template_subject, recipients=[email], template_body=template_body
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name=template_name)
    await delete_file(template_name)
    return "200"
