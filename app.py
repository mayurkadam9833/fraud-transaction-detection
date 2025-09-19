import joblib
import base64
import pandas as pd 
import streamlit as st
from src.fraud_transaction_detection.pipeline.prediction_pipeline import PredictionPipeline

# Function to set background image using base64 encoding
def get_background(image_file): 
    with open(image_file,"rb")as file: 
        data=file.read()
        encoded = base64.b64encode(data).decode()

        css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Setting background image
get_background(".streamlit\\background.png")

# App title 
st.title("`Fraud Detection Tool`")

# Description in Markdown
st.markdown("""
Enter the transaction details to check if it's fraudulent or legitimate.
            
🔢 **Failed Transactions** (Last 7 Days)\n
Use the slider to select how many times transactions have failed recently (0–10).

⚠️ **Risk Score**\n
Enter a number showing how risky the transaction is (e.g., 0.45, 0.75).
            
💳 **Transaction Type**\n
Choose how the transaction was made:
POS, Bank Transfer, Online, or ATM Withdrawal.

🏦 **Card Type**\n
Select the card used:
Amex, Mastercard, Visa, or Discover.

📱 **Device Type**\n
Pick the device used:
Laptop, Mobile, or Tablet.
""")

# user inputs
Failed_Transaction_Count_7d=st.sidebar.slider(label="Failed_Transaction_Count_7d",min_value=0,max_value=10)
Risk_Score=st.sidebar.number_input(label="Risk_Score")
Transaction_Type=st.sidebar.selectbox(label="Transaction_Type",options=['POS', 'Bank Transfer', 'Online', 'ATM Withdrawal'])
Card_Type=st.sidebar.selectbox(label="Card_Type",options=['Amex', 'Mastercard', 'Visa', 'Discover'])
Device_Type=st.sidebar.selectbox(label="Device_Type",options=['Laptop', 'Mobile', 'Tablet'])

# button for prediction
if st.button("check"):
    # create data frame of input data
    data=pd.DataFrame({
        "Failed_Transaction_Count_7d":[Failed_Transaction_Count_7d],
        "Risk_Score":[Risk_Score],
        "Transaction_Type":[Transaction_Type],
        "Card_Type":[Card_Type],
        "Device_Type":[Device_Type]
    })

    pred=PredictionPipeline()             # create obj of prediction pipeline

    prediction=pred.prediction(data)      # prediction on given data

    if prediction == 1:
        st.error("Fraudulent Transaction ")
    else:
        st.success("Legitimate Transaction")
    

