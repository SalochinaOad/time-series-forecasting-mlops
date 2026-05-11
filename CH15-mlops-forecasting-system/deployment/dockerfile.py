FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn scikit-learn pandas joblib numpy scipy

CMD ["uvicorn", "inference.api:app", "--host", "0.0.0.0", "--port", "8000"]