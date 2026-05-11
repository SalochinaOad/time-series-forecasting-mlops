import os
import joblib
from sklearn.ensemble import RandomForestRegressor

class ModelPipeline:

    def train(self, df):

        features = [
            "promotion",
            "holiday",
            "dayofweek",
            "month",
            "lag_1",
            "lag_7",
            "rolling_mean"
        ]

        X = df[features]
        y = df["sales"]

        model = RandomForestRegressor(
            n_estimators=150,
            max_depth=12,
            random_state=42
        )

        model.fit(X, y)

        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/forecast_model.pkl")

        return model, features