FROM python:3.10

WORKDIR /app

# Instaluj libpq-dev
RUN apt-get update && apt-get install -y libpq-dev

# Zaktualizuj libpq-dev do najnowszej wersji
RUN apt-get install -y --only-upgrade libpq-dev

# Instaluj psycopg2-binary
RUN pip install psycopg2-binary

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
