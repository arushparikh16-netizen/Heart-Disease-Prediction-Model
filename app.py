import streamlit as st
import pandas as pd
import joblib

model = joblib.load("heart_disease_pipeline.pkl")

st.title(" Heart Disease Prediction")
st.write(
    "Enter the patient's details below to get a prediction "
    "from the trained Machine Learning model."
)
st.subheader("🩺 Patient Details")
age = st.number_input("Age (Years)", min_value=1, max_value=100)
sex = st.selectbox("Sex", ['M', 'F'])
cpty = st.selectbox("Chest Pain Type", ['TA', 'ASY', 'NAP', 'ATA'])
restingbp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=200)
chol = st.number_input("Cholesterol (mg/dL)", min_value=0, max_value=1000)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL?", [0, 1])
restingecg = st.selectbox("Resting ECG Results", ['Normal', 'LVH', 'ST'])
maxhr = st.slider("Maximum Heart Rate", min_value=1, max_value=300)
exag = st.selectbox("Exercise-Induced Angina", ['True', 'False'])
oldpeak = st.number_input("Oldpeak", min_value=-5.0, max_value=10.0, step=0.1)
slope = st.selectbox("ST Slope", ['Flat', 'Up', 'Down'])

if st.button("🔍 Predict", use_container_width=True):
    input_df = pd.DataFrame([{
        'Age': age,
        'Sex': sex,
        'ChestPainType': cpty,
        'RestingBP': restingbp,
        'Cholesterol': chol,
        'FastingBS': fbs,
        'RestingECG': restingecg,
        'MaxHR': maxhr,
        'ExerciseAngina': exag,
        'Oldpeak': oldpeak,
        'ST_Slope': slope
    }])

    pred = model.predict(input_df)[0]

    st.subheader("📊 Prediction Result")

    if pred == 1:
        st.error("⚠️ The model predicts that heart disease may be present.")
    else:
        st.success("✅ The model predicts that heart disease may not be present.")

    with st.expander("📋 View Patient Input Details"):
        st.dataframe(input_df, use_container_width=True)

    st.caption(
        "Disclaimer: This prediction is for educational purposes only "
        "and is not a medical diagnosis."
    )



