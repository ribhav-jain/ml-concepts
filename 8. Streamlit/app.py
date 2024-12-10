import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("Streamlit Basic Features Demonstration")

# 1. Text display
st.header("1. Text Display")
st.write("This is an example of using Streamlit to display text in various formats.")
st.markdown("**Markdown:** You can style text using Markdown!")
st.code("print('This is a code block')", language="python")

# 2. User Input
st.header("2. User Input Widgets")
name = st.text_input("Enter your name:", value="John Doe")
age = st.slider("Select your age:", min_value=0, max_value=100, value=25)
gender = st.radio("Select your gender:", options=["Male", "Female", "Other"])
hobby = st.selectbox("Choose a hobby:", ["Reading", "Traveling", "Gaming", "Cooking"])
hobbies = st.multiselect(
    "Select multiple hobbies:", ["Reading", "Traveling", "Gaming", "Cooking"]
)
submit = st.button("Submit")

if submit:
    st.write(
        f"Hello, {name}! You are {age} years old, identify as {gender}, and enjoy {', '.join(hobbies)}."
    )

# 3. Data display
st.header("3. Data Display")
st.write("You can display dataframes, tables, and charts.")
data = pd.DataFrame(
    np.random.randn(10, 3), columns=["Feature A", "Feature B", "Feature C"]
)
st.write("### DataFrame:")
st.dataframe(data)
st.write("### Static Table:")
st.table(data.head())

# 4. Charts and plots
st.header("4. Charts and Plots")
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)

# 5. File Upload
st.header("5. File Upload")
uploaded_file = st.file_uploader("Upload a CSV file:")
if uploaded_file:
    uploaded_data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(uploaded_data)

# 6. Conditional Logic
st.header("6. Conditional Logic")
if st.checkbox("Show Random Number"):
    random_number = np.random.randint(1, 100)
    st.write(f"Random Number: {random_number}")

# 7. Sidebar
st.sidebar.header("Sidebar Widgets")
sidebar_name = st.sidebar.text_input("Enter your name (Sidebar):")
sidebar_age = st.sidebar.slider(
    "Select your age (Sidebar):", min_value=0, max_value=100, value=25
)
st.sidebar.write(f"Hello {sidebar_name}, age {sidebar_age}!")

# Footer
st.write("---")
st.write("This is a demonstration of Streamlit's basic features.")
