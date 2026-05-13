import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models")

# --------------------
# Diabetes
# --------------------
diabetes_model = pickle.load(
    open(os.path.join(MODEL_PATH, "diabetes_model.pkl"), "rb")
)

diabetes_scaler = pickle.load(
    open(os.path.join(MODEL_PATH, "diabetes_scaler.pkl"), "rb")
)

# --------------------
# Hypertension
# --------------------
hypertension_model = pickle.load(
    open(os.path.join(MODEL_PATH, "hypertension_model.pkl"), "rb")
)

hypertension_scaler = pickle.load(
    open(os.path.join(MODEL_PATH, "hypertension_scaler.pkl"), "rb")
)

# --------------------
# Heart Disease
# --------------------
heart_model = pickle.load(
    open(os.path.join(MODEL_PATH, "heart_disease_model.pkl"), "rb")
)

# --------------------
# Stroke
# --------------------
stroke_model = pickle.load(
    open(os.path.join(MODEL_PATH, "stroke_model.pkl"), "rb")
)