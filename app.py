import joblib
import pandas as pd 
import streamlit as st
from src.fraud_transaction_detection.pipeline.prediction_pipeline import PredictionPipeline


Failed_Transaction_Count_7d=st.sidebar.slider(label="Failed_Transaction_Count_7d",min_value=1,max_value=5)
Risk_Score=st.sidebar.number_input(label="Failed_Transaction_Count_7d")
Transaction_Type=st.sidebar.selectbox(label="Transaction_Type",options=['POS', 'Bank Transfer', 'Online', 'ATM Withdrawal'])
Card_Type=st.sidebar.selectbox(label="Transaction_Type",options=['Amex', 'Mastercard', 'Visa', 'Discover'])
Device_Type=st.sidebar.selectbox(label="Transaction_Type",options=['Laptop', 'Mobile', 'Tablet'])


if st.button("check"):
    data=pd.DataFrame({
        "Failed_Transaction_Count_7d":[Failed_Transaction_Count_7d],
        "Risk_Score":[Risk_Score],
        "Transaction_Type":[Transaction_Type],
        "Card_Type":[Card_Type],
        "Device_Type":[Device_Type]
    })

    pred=PredictionPipeline()

    prediction=pred.prediction(data)

    if prediction == 1:
        st.write("fraud")
    else:
        st.write("not fraud")
    

