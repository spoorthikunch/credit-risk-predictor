import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("credit_risk_model.pkl")

st.title("Credit Risk Prediction App")
st.write("Enter customer details to predict default risk.")

# -----------------------
# User Inputs
# -----------------------

person_age = st.number_input("Age", min_value=18, max_value=100, value=30)
person_income = st.number_input("Annual Income", min_value=0.0, value=50000.0)
person_emp_length = st.number_input("Employment Length (years)", min_value=0.0, value=5.0)
loan_amnt = st.number_input("Loan Amount", min_value=0.0, value=10000.0)
loan_int_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=10.0)
loan_percent_income = st.number_input("Loan Percent Income", min_value=0.0, value=0.2)
cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=0.0, value=5.0)

loan_grade = st.selectbox("Loan Grade", ["A","B","C","D","E","F","G"])
person_home_ownership = st.selectbox(
    "Home Ownership",
    ["RENT","OWN","MORTGAGE","OTHER"]
)
loan_intent = st.selectbox(
    "Loan Intent",
    ["PERSONAL","EDUCATION","MEDICAL","VENTURE","HOMEIMPROVEMENT","DEBTCONSOLIDATION"]
)

# If pipeline expects it
loan_status = st.number_input("Loan Status (numeric)", value=0)

# Convert grade to numeric
risk_level = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}
loan_grade_numeric = risk_level[loan_grade]

# -----------------------
# Prediction
# -----------------------

if st.button("Predict Risk"):

    input_df = pd.DataFrame({
        "person_age": [person_age],
        "person_income": [person_income],
        "person_emp_length": [person_emp_length],
        "loan_amnt": [loan_amnt],
        "loan_int_rate": [loan_int_rate],
        "loan_percent_income": [loan_percent_income],
        "cb_person_cred_hist_length": [cb_person_cred_hist_length],
        "loan_grade": [loan_grade_numeric],
        "person_home_ownership": [person_home_ownership],
        "loan_intent": [loan_intent],
        "loan_status": [loan_status]
    })

    proba = model.predict_proba(input_df)[0][1]

    threshold = 0.4   # You can adjust this
    prediction = 1 if proba >= threshold else 0

    st.write("Default Probability:", round(proba, 3))
    st.write("Threshold Used:", threshold)

    if prediction == 1:
        st.error("High Risk of Default ⚠️")
    else:
        st.success("Low Risk of Default ✅") 