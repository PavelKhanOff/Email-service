from pydantic import BaseModel, EmailStr


class EmailSend(BaseModel):
    email: EmailStr
    template_name: str
    template_subject: str
    template_body: dict
