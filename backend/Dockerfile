FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev

RUN apt-get install -y --only-upgrade libpq-dev

RUN pip install psycopg2-binary

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
