import os

from starlette.responses import JSONResponse
from eduone_mail.app.core.tasks import send_email
from fastapi import APIRouter, File, UploadFile, HTTPException
from pydantic import EmailStr
from eduone_mail.app.core.aws import download_from_cdn, upload_file_to_cdn, delete_file
import tempfile
import eduone_mail.app.settings.config as Envs
import shutil
from eduone_mail.app.schemas import EmailSend
from eduone_mail.app.exceptions import TemplateNotFound


router = APIRouter()


@router.post("/email/send")
async def send_email_format(email_sch: EmailSend) -> JSONResponse:
    template_body = email_sch.template_body
    template_name = email_sch.template_name
    template_subject = email_sch.template_subject
    try:
        download_from_cdn(template_name)
    except TemplateNotFound:
        return JSONResponse(status_code=404, content={"message": "Template not found"})
    await send_email.apply_async(
        args=(email_sch.email, template_body, template_name, template_subject),
        queue='queue2',
    )
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.post("/email/register/send")
async def send_email_register(email: EmailStr) -> JSONResponse:
    template_body = {"title": 'g', 'name': 'ge'}
    template_name = "test.html"
    template_subject = "Subject"
    await send_email.apply_async(
        args=(email, template_body, template_name, template_subject), queue='queue2'
    )
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.post("/email/upload/template", tags=["Upload template to server"])
async def upload_file(file: UploadFile = File(...)):
    try:
        f = tempfile.NamedTemporaryFile(dir=Envs.TEMPLATE_FOLDER, delete=False)
        tmp_path = f.name
        print(file.filename)
        with open(tmp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        upload_file_to_cdn(tmp_path, file.filename)

    except Exception:
        raise HTTPException(status_code=500, detail="Some error in uploading")
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
