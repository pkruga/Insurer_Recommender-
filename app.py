pip install joblib

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Display header images
st.image(['Insurers.png', 'background image.jpeg'], width=600, use_column_width='auto')

st.markdown("""
    <style>
    .stApp {
        background-image: url('802169.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        background-color: lightblue;
        color: black;
    }
    h1, h2, h3 {
        font-family: 'Helvetica', sans-serif;
        color: darkblue;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the trained XGBoost model
model = joblib.load('en_model.pkl')

# Load the dataset
df = pd.read_csv('insurance_data_with_reliability.csv')

# Streamlit app
st.title("Insurance Provider Recommender")
st.write("""
This system helps Kenyan customers rate the reliability of insurance providers based on their non-liability claim settlement history.
""")

# User inputs
st.header("Select Insurer and Rating Metrics")

# Insurer selection
insurers = df['Insurer'].unique()
selected_insurer = st.selectbox('Pick Insurer', insurers)

# Year selection
years = df['Year']
selected_year = st.selectbox('Select Year', sorted(years))

# Quarter selection
quarters = ['Quarter']
selected_quarter = st.selectbox('Select Quarter', sorted(quarters))

# Filter data based on selections
filtered_data = df[(df['Insurer'] == selected_insurer) & (df['Year'] == selected_year) & (df['Quarter'] == quarters.index(selected_quarter) + 1)]

if filtered_data.empty:
    st.write("No data available for the selected period.")
else:
    # Extract features for prediction
    features = filtered_data[['Claims_outstanding_at_the_beginning_of_the_quarter',
                              'Claims_intimated_during_the_quarter', 
                              'Claims_revived', 
                              'Claims_paid',
                              'Claims_declined', 
                              'Claims_closed_as_no_claims',
                              'Claims_outstanding_at_the_end', 
                              'Claims_declined_ratio_(%)',
                              'Claims_closed_as_no_claims_ratio_(%)', 
                              'Claim_payment_ratio_(%)',
                              'Total_Claims_Payable', 
                              'Total_Claims_Action_during_the_Quarter',
                              'Claims_closed_as_no_claims_ratio (%)', 
                              'Insurer_Encoded', 
                              'Reliability_Score', 
                              'Reliability_Label_Encoded']].values

    # Predict reliability score
    prediction = model.predict(features)
    st.write(f"Predicted Reliability Score for {selected_insurer} in {selected_year} {selected_quarter}: {prediction[0]:.2f}")
