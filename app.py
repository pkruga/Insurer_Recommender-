import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Display header images
st.image(['IMAGES/Insurers.png', 'IMAGES/background image.jpeg'], width=600, use_column_width=True)

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

# Load the trained model
model = joblib.load('en_model.pkl')

# Load the dataset
df = pd.read_csv('CSV/concatenated_df')

# Streamlit app
st.title("Insurance Provider Recommender")
st.write("""
This system helps Kenyan customers rate the reliability of insurance providers based on their non-liability claim settlement history.
""")

# User inputs
st.header("Select Insurer and Rating Metrics")

# Insurer section
# Read the years from the markdown file
with open('insurers.md', 'r') as f:
  insurers_list = [line.strip('- ').strip() for line in f.readlines() if line.strip()]

# Check if the number of insurers matches the number of encoded values

# Get unique encoded values for Insurer_Encoded
unique_insurers_encoded = df['Insurer_Encoded'].unique()

# Check if the number of insurers matches the number of encoded values
if len(insurers_list) == len(unique_insurers_encoded):
  # Create a dictionary mapping encoded values to original insurer names
  insurer_mapping = dict(zip(unique_insurers_encoded, insurers_list))

  # Insurer selection using Insurer_Encoded
  selected_insurer_encoded = st.selectbox('Pick Insurer (Encoded)', unique_insurers_encoded)

  # Get the corresponding original insurer name
  selected_insurer = insurer_mapping.get(selected_insurer_encoded, "Unknown Insurer")

  # Display the selected insurer
  st.write("You selected:", selected_insurer)
else:
  st.error("Mismatch in number of insurers and encoded values. Please check your data.")

# Year section
# Read the years from the markdown file
with open('years.md', 'r') as f:
  years_list = [int(line.strip('- ').strip()) for line in f.readlines() if line.strip() and line.strip('- ').strip().isdigit()]

# Year selection
# Check if the number of years matches the number of unique values in the 'Year' column
unique_years = df['Year'].unique()
if len(years_list) == len(unique_years):
  # Create a dictionary mapping unique years to years from the list
  year_mapping = dict(zip(unique_years, years_list))

  # Year selection using the 'Year' column
  selected_year = st.selectbox('Select Year', unique_years)

  # Get the corresponding year from the list
  selected_year_label = year_mapping.get(selected_year, "Unknown Year") # Assign the selected year label here

  # Display the selected year
  st.write("You selected:", selected_year_label)
else:
  st.error("Mismatch in number of years and values in the 'Year' column. Please check your data.")

# Quarter section
# Read the quarters from the markdown file
with open('quarters.md', 'r') as f:
  quarters_list = [int(line.strip('- ').strip()) for line in f.readlines() if line.strip() and line.strip('- ').strip().isdigit()]

# Quarter selection
# Check if the number of quarters matches the number of unique values in the 'Quarter' column
unique_quarters = df['Quarter'].unique()
if len(quarters_list) == len(unique_quarters):
  # Create a dictionary mapping unique quarters to quarters from the list
  quarter_mapping = dict(zip(unique_quarters, quarters_list))

  # Quarter selection using the 'Quarter' column
  selected_quarter = st.selectbox('Select Quarter', unique_quarters)

  # Get the corresponding quarter from the list
  selected_quarter_label = quarter_mapping.get(selected_quarter, "Unknown Quarter")

  # Display the selected quarter
  st.write("You selected:", selected_quarter_label)
else:
  st.error("Mismatch in number of quarters and values in the 'Quarter' column. Please check your data.")

# Reliability section
# Read the reliability labels from the markdown file
with open('reliability_labels.md', 'r') as f:
  reliability_labels_list = [line.strip('- ').strip() for line in f.readlines() if line.strip()]

# Reliability section
# Read the reliability labels from the markdown file
with open('reliability_labels.md', 'r') as f:
  reliability_labels_list = [line.strip('- ').strip() for line in f.readlines() if line.strip() and not line.startswith('#')]

# Reliability label selection
# Check if the number of reliability labels matches the number of unique values in the 'Reliability_Label_Encoded' column
unique_reliability_labels_encoded = df['Reliability_Label_Encoded'].unique()
if len(reliability_labels_list) == len(unique_reliability_labels_encoded):
  # Create a dictionary mapping encoded values to original reliability labels
  reliability_label_mapping = dict(zip(unique_reliability_labels_encoded, reliability_labels_list))

  # Reliability label selection using 'Reliability_Label_Encoded'
  selected_reliability_label_encoded = st.selectbox('Select Reliability Label (Encoded)', unique_reliability_labels_encoded)

  # Get the corresponding original reliability label
  selected_reliability_label = reliability_label_mapping.get(selected_reliability_label_encoded, "Unknown Reliability Label")

  # Display the selected reliability label
  st.write("You selected:", selected_reliability_label)
else:
  st.error("Mismatch in number of reliability labels and encoded values. Please check your data.")

# Filter data based on selections
filtered_data = df[(df['Insurer_Encoded'] == selected_insurer) & (df['Year'] == selected_year_label) & (df['Quarter'] == selected_quarter_label) & (df['Reliability_Label_Encoded'] == selected_reliability_label_encoded + 1)]

if filtered_data.empty:
    st.write("No data available for the selected period.")
else:
    # Extract features for prediction
    features = filtered_data[['Claims_revived',
                              'Claims_declined',
                              'Insurer_Encoded',
                              'Quarter',
                              'Reliability_Label_Encoded',
                              'Reliability_Score',
                              'Year']].values
    # Predict reliability score
    prediction = model.predict(features)
    st.write(f"Predicted Reliability Score for {selected_insurer} in {selected_year} {selected_quarter}: {prediction[0]:.2f}")
