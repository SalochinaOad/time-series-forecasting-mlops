from data_pipeline.pipeline import DataPipeline
from features.feature_store import FeatureStore
from training.model_pipeline import ModelPipeline
from inference.forecast_service import ForecastService
from monitoring.metrics import Metrics
from monitoring.drift import DriftDetector
from pipelines.retraining_trigger import RetrainingPipeline

# INIT
data_pipeline = DataPipeline()
feature_store = FeatureStore()
model_pipeline = ModelPipeline()

metrics = Metrics()
drift_detector = DriftDetector()
retrain = RetrainingPipeline()

# DATA
df = data_pipeline.ingest()
df = data_pipeline.validate(df)

# FEATURES
df = feature_store.build_features(df)

# SPLIT
split = int(len(df) * 0.8)
train = df[:split]
test = df[split:]

# TRAIN
model, features = model_pipeline.train(train)

# PREDICT
service = ForecastService()
preds = service.predict(model, test, features)

# EVALUATE
print(metrics.compute(test["sales"], preds))

# DRIFT
drift_flag = drift_detector.detect(train, test)

# RETRAIN
retrain.trigger(drift_flag)