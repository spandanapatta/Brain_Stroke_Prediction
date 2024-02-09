import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import time
import pickle
import joblib
import warnings

warnings.filterwarnings("ignore")

model = joblib.load('rf_clf.joblib')
scaler = joblib.load('scaler.joblib')

tabs = ["Home", "Prediction", "Precautions"]
page = st.sidebar.radio("Tabs", tabs)

if page == "Prediction":
    st.markdown(
        "<h1 style='text-align:center;'>Brain Stroke Prediction</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='text-align:center;'>Personal Information</h2>",
        unsafe_allow_html=True,
    )
    age_ = st.slider("**Age**", 0, 100)
    married_ = st.radio("**Marital Status**", ["Yes", "No"], horizontal=True)


    st.markdown(
        "<h2 style='text-align:center;'>Health Information</h2>", unsafe_allow_html=True
    )

    if st.checkbox("**Don't Know BMI?**"):
        height = st.slider(
            "*Enter User's Height in cm*", value=200.0, step=1.0, format="%.2f"
        )
        weight = st.slider(
            "*Enter User's Weight in kgs*", value=200.0, step=1.0, format="%.2f"
        )
        bmi_ = weight / (height / 100) ** 2
        st.write(f"BMI of user is {bmi_} and will be auto-updated")
    else:
        bmi_ = st.slider(
            "**Enter User's BMI**", min_value=10.0, max_value=50.0, step=0.01, format="%.2f"
        )

    glucose_level_ = st.slider(
        "**Glucose Level(eAG)**", min_value=50.0, max_value=300.0, step=1.0, format="%.2f"
    )
    heart_ = st.radio("**Do you have heart disease?**", ["Yes", "No"], horizontal=True)
    hypertension_ = st.radio("**Do you have hypertension?**", ["Yes", "No"], horizontal=True)
    button = st.button("Predict")

    if button == True:
        info = st.info("Please wait, prediction is in progress:hourglass:")
        progress_bar = st.progress(0)
        for perc_completed in range(100):
            time.sleep(0.05)
            progress_bar.progress(perc_completed + 1)
        info.empty()
        cols = [
            "age",
            "hypertension",
            "heart_disease",
            "ever_married",
            "avg_glucose_level",
            "bmi",
            
        ]

        row = np.array(
            [
                age_,
                hypertension_,
                heart_,
                married_,
                glucose_level_,
                bmi_,
            ]
        )
        X = pd.DataFrame(data=[row], columns=cols)
        X["age"] = X["age"].astype("float")
        X["avg_glucose_level"] = X["avg_glucose_level"].astype("float")
        X["bmi"] = X["bmi"].astype("float")

        X["ever_married"] = [1 if i == "Yes" else 0 for i in X["ever_married"]]
        X["hypertension"] = [1 if i == "Yes" else 0 for i in X["hypertension"]]
        X["heart_disease"] = [1 if i == "Yes" else 0 for i in X["heart_disease"]]


        X = scaler.transform(X)

        prediction = model.predict(X)

        if prediction == 1:
            st.error("You have higher chances of having a stroke:disappointed:")
        else:
            st.success("You have lower chances of having a stroke🥳")

if page == "Precautions":
    st.title("Precautions for Brain Stroke")
    st.markdown("""
            Brain stroke is a serious medical condition that requires immediate attention. 
            Here are some precautions to help you prevent brain strokes:
        """)

    precautions = [
        "Maintain a healthy lifestyle with a balanced diet.",
        "Exercise regularly to keep your body and mind active.",
        "Monitor and control high blood pressure.",
        "Quit smoking and limit alcohol consumption.",
        "Manage stress through relaxation techniques.",
        "Maintain a healthy weight.",
        "Regularly check cholesterol levels.",
        "Stay hydrated by drinking an adequate amount of water.",
        "Get regular check-ups and screenings.",
        "Know and manage your diabetes if applicable.",
    ]

    st.markdown("### Precautionary Measures:")
    for precaution in precautions:
        st.write(f"- {precaution}")

if page == "Home":
    st.title("Brain Stroke Prediction App")
    st.write(
        "Welcome to the Brain Stroke Prediction App! This app helps you predict the likelihood of having a stroke based on your personal and health information.")
    st.write("Please select an option from the sidebar to proceed")
