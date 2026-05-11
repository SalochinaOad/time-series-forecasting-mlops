from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/forecast_model.pkl")

features = [
    "promotion",
    "holiday",
    "dayofweek",
    "month",
    "lag_1",
    "lag_7",
    "rolling_mean"
]

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame(data)

    preds = model.predict(df[features])

    return {"predictions": preds.tolist()}