import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Display header images
st.image(['IMAGES/Insurers.png', 'IMAGES/background image.jpeg'], width=600, use_column_width='auto')

st.markdown("""
    <style>
    .stApp {
        background-image: url('IMAGES/802169.jpg');
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

# Load the trained Ensemble Stacking model
model = joblib.load('stacking_model.pkl')

# Load the dataset
df = pd.read_csv('CSV/deployment_data.csv')

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
years = df['Year'].unique()
selected_year = st.selectbox('Select Year', sorted(years))

# Quarter selection
quarters = df['Quarter'].unique()
selected_quarter = st.selectbox('Select Quarter', quarters)

# Filter data based on selections
filtered_data = df[(df['Insurer'] == selected_insurer) & 
                   (df['Year'] == selected_year) & 
                   (df['Quarter'] == selected_quarter)]

if filtered_data.empty:
    st.write("No data available for the selected period.")
else:
    # Extract features for prediction
    features = filtered_data[['Claims_revived',
                              'Claims_declined',
                              'Insurer_Encoded',
                              'Reliability_Label_Encoded',
                              'Quarter_Scaled']].values

    # Predict reliability score
    prediction = model.predict(features)

    # Get the reliability label and encoded value from the filtered data
    reliability_label = filtered_data['Reliability_Label'].values[0]
    reliability_label_encoded = filtered_data['Reliability_Label_Encoded'].values[0]

    # Display the results
    st.write(f"Predicted Reliability Score for {selected_insurer} in {selected_year} Q{selected_quarter}: {prediction[0]:.2f}")
    st.write(f"Reliability Label: {reliability_label} (Encoded: {reliability_label_encoded})")
