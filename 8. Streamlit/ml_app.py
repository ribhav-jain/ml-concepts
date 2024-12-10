import streamlit as st
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Title and Description
st.title("Diabetes Progression Prediction")
st.write(
    """
    This app demonstrates machine learning using **Streamlit** and **scikit-learn**. 
    The dataset predicts the progression of diabetes based on clinical features.
    """
)


# Load dataset and cache it
@st.cache_data
def load_data():
    diabetes = load_diabetes(as_frame=True)
    data = diabetes.frame
    X = data.drop(columns="target")
    y = data["target"]
    return X, y


X, y = load_data()

# Display dataset information
st.subheader("Dataset Overview")
if st.checkbox("Show raw dataset"):
    st.write(pd.concat([X, y], axis=1))

# Sidebar for user input
st.sidebar.header("Model Parameters")
test_size = st.sidebar.slider(
    "Test size (fraction)", min_value=0.1, max_value=0.5, value=0.2, step=0.1
)
n_estimators = st.sidebar.slider(
    "Number of trees in Random Forest", 10, 200, step=10, value=100
)
max_depth = st.sidebar.slider("Maximum depth of trees", 1, 20, step=1, value=5)


# Split the data
@st.cache_data
def split_data(X, y, test_size):
    return train_test_split(X, y, test_size=test_size, random_state=42)


X_train, X_test, y_train, y_test = split_data(X, y, test_size)


# Train the model
@st.cache_data
def train_model(X_train, y_train, n_estimators, max_depth):
    model = RandomForestRegressor(
        n_estimators=n_estimators, max_depth=max_depth, random_state=42
    )
    model.fit(X_train, y_train)
    return model


model = train_model(X_train, y_train, n_estimators, max_depth)

# Make predictions
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Display results
st.subheader("Model Evaluation")
st.write(f"Mean Squared Error: {mse:.2f}")

# Interactive Predictions
st.subheader("Make Predictions")
sample_input = {
    feature: st.number_input(
        f"{feature}",
        float(X[feature].min()),
        float(X[feature].max()),
        float(X[feature].mean()),
    )
    for feature in X.columns
}
sample_input_df = pd.DataFrame([sample_input])

if st.button("Predict Progression"):
    prediction = model.predict(sample_input_df)
    st.write(f"Predicted Diabetes Progression: {prediction[0]:.2f}")
