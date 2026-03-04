FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lab2/main.py .

EXPOSE 8002

CMD ["python", "main.py"]
