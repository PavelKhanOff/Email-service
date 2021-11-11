FROM python:3.8.5-slim-buster



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  apt-get update -y &&  apt-get install -y redis-server
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt



COPY . /eduone_mail

ENV PATH=$PATH:/eduone_mail/
ENV PYTHONPATH /eduone_mail/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9001"]
