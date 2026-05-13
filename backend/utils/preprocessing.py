import pandas as pd

def prepare_features(data, bmi: float):

    df = pd.DataFrame([{
        "BMI": bmi,
        "Physical_Activity": data.physical_activity,
        "Smoking_History": data.smoking_history,
        "Alcohol_Frequency": data.alcohol_frequency,
        "Fruit_Consumption": data.fruit_consumption,
        "Vegetable_Consumption": data.vegetable_consumption,
        "Age": data.age
    }])

    return df

def prepare_features_for_diabetes(data, bmi: float):

    df = pd.DataFrame([{
        "BMI": bmi,
        "Physical_Activity": data.physical_activity,
        "Smoking_History": data.smoking_history,
        "Fruit_Consumption": data.fruit_consumption,
        "Vegetable_Consumption": data.vegetable_consumption,
        "Age": data.age
    }])

    return df