import boto3
import eduone_mail.app.settings.config as Envs
import os
from eduone_mail.app.exceptions import TemplateNotFound


session = boto3.session.Session()
client = session.client(
    's3',
    region_name=Envs.AWS_REGION_NAME,
    endpoint_url=Envs.AWS_ENDPOINT_URL,
    aws_access_key_id=Envs.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Envs.AWS_SECRET_ACCESS_KEY,
)


def download_from_cdn(template_name: str):
    try:
        client.download_file(
            Envs.BUCKET_TEMPLATES,
            template_name,
            f'/eduone_mail/templates/{template_name}',
        )
    except Exception as e:
        print("111111111111", e)
        raise TemplateNotFound(name=template_name)
    return "OK"


async def delete_file(template_name: str):
    dir = f'/eduone_mail/templates/{template_name}'
    if os.path.exists(dir):
        os.remove(dir)


def upload_file_to_cdn(tmp_path: str, name: str):
    try:
        client.upload_file(
            tmp_path, Envs.BUCKET_TEMPLATES, name, ExtraArgs={'ACL': 'public-read'}
        )
    except Exception as e:
        print(e)
    finally:
        if tmp_path:
            os.unlink(tmp_path)
    return "File is uploaded"
