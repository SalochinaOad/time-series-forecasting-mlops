import pandas as pd
import numpy as np

class DataPipeline:

    def ingest(self):
        np.random.seed(42)
        dates = pd.date_range("2022-01-01", periods=600)

        df = pd.DataFrame({
            "date": dates,
            "promotion": np.random.choice([0,1], 600, p=[0.8,0.2]),
            "holiday": np.random.choice([0,1], 600, p=[0.95,0.05]),
        })

        df["base"] = 200 + np.sin(np.arange(600)/14)*25

        df["sales"] = (
            df["base"]
            + df["promotion"]*35
            + df["holiday"]*60
            + np.random.normal(0, 12, 600)
        )

        return df

    def validate(self, df):
        assert df.isnull().sum().sum() == 0
        assert df["sales"].std() > 1
        return df