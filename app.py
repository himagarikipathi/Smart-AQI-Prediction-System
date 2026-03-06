import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

# -------------------------------
# Step 0: Set background image
# -------------------------------
def set_bg(png_file):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{png_file}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("background.png")  # <-- your image file

# -------------------------------
# Step 1: Dummy model with 3 features
# -------------------------------
X = np.array([
    [0, 0, 0],
    [1, 0, 1],
    [2, 1, 0],
    [3, 1, 1]
])
y = np.array([0, 1, 2, 3])

model = LinearRegression()
model.fit(X, y)

# -------------------------------
# Step 2: Page title and description
# -------------------------------
st.title("Traffic Prediction App ")
st.write("Enter traffic features to see predictions.")

# -------------------------------
# Step 3: User Inputs
# -------------------------------
hour = st.number_input("Hour of the day (0-23):", min_value=0, max_value=23)
vehicle_count = st.number_input("Number of vehicles:", min_value=0)
platform = st.selectbox("Platform Type:", ["Snowflake", "Enterprise", "Other"])

# Convert categorical platform to numeric
platform_val = {"Snowflake": 0, "Enterprise": 1, "Other": 2}[platform]

# -------------------------------
# Step 4: Prediction
# -------------------------------
if st.button("Predict Traffic"):
    prediction = model.predict([[hour, vehicle_count, platform_val]])
    st.write(f"Predicted traffic value: {prediction[0]:.2f}")