FROM python:3.8

ENV PYTHONBUFFERED=1

WORKDIR /django

COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000