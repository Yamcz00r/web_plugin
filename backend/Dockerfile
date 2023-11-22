FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -r requirments.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]