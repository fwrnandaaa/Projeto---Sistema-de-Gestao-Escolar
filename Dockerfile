FROM python:3.10
WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .


RUN mkdir -p /app/db

EXPOSE 8000


CMD ["python", "gestao_escolar/manage.py", "runserver", "0.0.0.0:8000"]