import streamlit as st
import plotly.express as px
import pandas as pd

from api_client import predict
from ui_components import info_box, create_gauge_chart

st.set_page_config(
    page_title="Health Risk Predictor",
    page_icon="🩺",
    layout="wide" # Changed to wide for better chart fitting
)

# =========================
# HEADER & SIDEBAR
# =========================
# Adding a placeholder hero image (You can replace this URL with a local image)
st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80", width =True)

st.title("🩺 AI Health Risk Prediction System")
st.markdown("Predict your risk for **Diabetes, Hypertension, Heart Disease, and Stroke** based on advanced machine learning algorithms.")
st.warning("⚠️ **Disclaimer:** This tool is for educational purposes only and does not replace professional medical advice.")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=100)
st.sidebar.title("ℹ️ Instructions")
st.sidebar.info("""
1. Enter your vitals.
2. Be honest about lifestyle factors.
3. Click a disease button below to calculate risk.
""")

# =========================
# USER INPUT SECTION
# =========================
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 Vitals & Basics")
    
    # Put inputs in an expander or container to keep it clean
    with st.container(border=True):
        age = st.slider("Age", 1, 100, 30)
        c1, c2 = st.columns(2)
        with c1:
            height = st.number_input("Height (cm)", 100, 220, 170)
        with c2:
            weight = st.number_input("Weight (kg)", 30, 200, 70)
        
        # LIVE METRIC: Calculate BMI instantly
        bmi = weight / ((height / 100) ** 2)
        st.metric(label="Your Calculated BMI", value=f"{bmi:.1f}")

    info_box("Height & Weight", "These are used to automatically calculate your Body Mass Index (BMI), a key factor in predicting metabolic risks.", "📏")

with col2:
    st.header("🏃 Lifestyle Factors")
    
    with st.container(border=True):
        sc1, sc2 = st.columns(2)
        with sc1:
            physical_activity = st.selectbox("Exercise regularly?", ["Yes", "No"])
        with sc2:
            smoking = st.selectbox("Smoking history?", ["Yes", "No"])
            
        alcohol = st.slider("🍺 Alcohol (times/month)", 0, 30, 5)
        fruit = st.slider("🍎 Fruit (servings/month)", 0, 100, 20)
        vegetables = st.slider("🥦 Vegetables (servings/month)", 0, 100, 25)

# =========================
# PREPARE PAYLOAD
# =========================
payload = {
    "height_cm": height,
    "weight_kg": weight,
    "age": age,
    "physical_activity": 1 if physical_activity == "Yes" else 0,
    "smoking_history": 1 if smoking == "Yes" else 0,
    "alcohol_frequency": alcohol,
    "fruit_consumption": fruit,
    "vegetable_consumption": vegetables
}

# =========================
# PREDICTION SECTION
# =========================
st.markdown("---")
st.header("🔍 Run Risk Analysis")

# We use tabs to make it feel like a unified dashboard rather than clunky buttons
tab1, tab2, tab3, tab4 = st.tabs(["Diabetes", "Hypertension", "Heart Disease", "Stroke"])

def handle_prediction(disease_id, disease_name):
    # Call your API
    result = predict(disease_id, payload)
    
    # Assuming your API returns a dict like: {"prediction": 1, "risk_probability": 0.85}
    # If it returns a string, you'll need to adjust this parsing logic.
    if isinstance(result, dict) and 'risk_probability' in result:
        prob = result['risk_probability']
        
        col_chart, col_text = st.columns([1, 1])
        
        with col_chart:
            # Draw the beautiful gauge chart
            fig = create_gauge_chart(prob, disease_name)
            st.plotly_chart(fig, use_container_width=True)
            
        with col_text:
            st.write("### AI Diagnostic Summary")
            if prob > 0.7:
                st.error(f"**High Risk Detected.** The model indicates a {prob*100:.1f}% probability. Please consult a physician.")
            elif prob > 0.3:
                st.warning(f"**Moderate Risk.** The model indicates a {prob*100:.1f}% probability. Consider lifestyle improvements.")
            else:
                st.success(f"**Low Risk.** The model indicates a {prob*100:.1f}% probability. Keep up the good habits!")
    else:
        # Fallback if your API returns something else
        st.write(result)

with tab1:
    if st.button("Run Diabetes Analysis", type="primary"):
        handle_prediction("diabetes", "Diabetes")

with tab2:
    if st.button("Run Hypertension Analysis", type="primary"):
        handle_prediction("hypertension", "Hypertension")

with tab3:
    if st.button("Run Heart Disease Analysis", type="primary"):
        handle_prediction("heart", "Heart Disease")

with tab4:
    if st.button("Run Stroke Analysis", type="primary"):
        handle_prediction("stroke", "Stroke")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Built with FastAPI + Streamlit | ML Medical Risk System")