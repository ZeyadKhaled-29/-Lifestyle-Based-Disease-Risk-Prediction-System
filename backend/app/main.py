from fastapi import FastAPI

from app.schemas import HealthInput

from utils.helpers import calculate_bmi
from utils.preprocessing import prepare_features, prepare_features_for_diabetes
from utils.model_loader import (
    diabetes_model, diabetes_scaler,
    hypertension_model, hypertension_scaler,
    heart_model, stroke_model
)

from services.predictor import predict

app = FastAPI()

@app.post("/predict/diabetes")
def diabetes(data: HealthInput):

    bmi = calculate_bmi(data.weight_kg, data.height_cm)
    df = prepare_features_for_diabetes(data, bmi)

    return predict(diabetes_model, diabetes_scaler, df)


@app.post("/predict/hypertension")
def hypertension(data: HealthInput):

    bmi = calculate_bmi(data.weight_kg, data.height_cm)
    df = prepare_features(data, bmi)

    return predict(hypertension_model, hypertension_scaler, df)


@app.post("/predict/heart")
def heart(data: HealthInput):

    bmi = calculate_bmi(data.weight_kg, data.height_cm)
    df = prepare_features(data, bmi)

    return predict(heart_model, None, df)


@app.post("/predict/stroke")
def stroke(data: HealthInput):

    bmi = calculate_bmi(data.weight_kg, data.height_cm)
    df = prepare_features(data, bmi)

    return predict(stroke_model, None, df)