class ForecastService:

    def predict(self, model, df, features):
        return model.predict(df[features])