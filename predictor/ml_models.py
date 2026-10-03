import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "construction_risk_pipeline.joblib"
)

model = joblib.load(MODEL_PATH)