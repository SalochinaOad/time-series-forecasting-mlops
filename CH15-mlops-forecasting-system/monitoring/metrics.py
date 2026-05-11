import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

class Metrics:

    def compute(self, y_true, y_pred):

        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))

        return {"mae": mae, "rmse": rmse}