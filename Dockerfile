FROM python:3.10

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
