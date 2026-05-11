class FeatureStore:

    def build_features(self, df):

        df = df.copy()

        df["dayofweek"] = df["date"].dt.dayofweek
        df["month"] = df["date"].dt.month

        df["lag_1"] = df["sales"].shift(1)
        df["lag_7"] = df["sales"].shift(7)

        df["rolling_mean"] = df["sales"].rolling(7).mean()

        return df.dropna()
