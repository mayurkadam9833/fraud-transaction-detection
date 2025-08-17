import os
import streamlit as st 
import numpy as np 
import pandas as pd
from src.transaction_fraud_detection.pipeline.prediction import PredictionPipeline

st.title("Transcation Fraud Detection")

step=st.number_input(label="Step (Represents a unit of time (usually 1 step = 1 hour) in the simulation.)")
type=st.selectbox(label="Type (The type of transaction.)",options=["CASH_OUT","PAYMENT","CASH_IN","TRANSFER","DEBIT"])
amount=st.number_input(label="Amount (The transaction amount)")
oldbalanceOrg=st.number_input(label="oldbalanceOrg (The originator’s account balance before the transaction.)")
newbalanceOrig=st.number_input(label="newbalanceOrig (The originator’s account balance after the transaction.)")
oldbalanceDest=st.number_input(label="oldbalanceDest (The recipient’s balance before the transaction.)")
newbalanceDest=st.number_input(label="newbalanceDest (The recipient’s balance after the transaction.)")
prediction=PredictionPipeline()


if st.button("check transcation"):
    data=pd.DataFrame({
        "step":[step],
        "type":[type],
        "amount":[amount],
        "oldbalanceOrg":[oldbalanceOrg],
        "newbalanceOrig":[newbalanceOrig],
        "oldbalanceDest":[oldbalanceDest],
        "newbalanceDest":[newbalanceDest],
        })
    
    pred=prediction.predict(data)[0]
    proba = prediction.predict_proba(data)

    if pred == 1:
        st.write("warning fraud transcation")
    else:
        st.write("safe transcation")


