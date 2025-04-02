FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install flask

EXPOSE 6500
CMD ["python3", "app.py"]
