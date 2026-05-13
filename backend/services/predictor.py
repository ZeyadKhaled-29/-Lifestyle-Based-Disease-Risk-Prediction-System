def predict(model, scaler, df):

    if scaler is not None:
        df = scaler.transform(df)

    prob = model.predict_proba(df)[0][1]
    pred = model.predict(df)[0]

    return {
        "prediction": int(pred),
        "risk_probability": round(float(prob), 4)
    }