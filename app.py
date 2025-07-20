# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load('iris_model.pkl')

# --- App title and instructions ---
st.set_page_config(page_title="Iris Classifier", layout="centered")
st.title("🌸 Iris Flower Classifier")
st.write("Adjust the flower measurements below to predict its species.")

# User inputs
sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 1.0)

# --- Format input data ---
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
features = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']

# Prediction
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)[0]
proba = model.predict_proba(input_data)


species = ['Setosa', 'Versicolor', 'Virginica']
st.subheader("Prediction")
st.success(f"The predicted species is **{species[prediction]}** 🌼")


# Probability bar chart
st.subheader("Prediction Probability")
fig, ax = plt.subplots()
ax.bar(species, proba[0], color=['#ffa07a', '#20b2aa', '#9370db'])
ax.set_ylabel("Probability")
st.pyplot(fig)

# --- Visualize Input Features ---
st.subheader("📈 Input Feature Visualization")
fig2, ax2 = plt.subplots()
ax2.bar(features, input_data[0], color='orchid')
ax2.set_ylabel("Value (cm)")
st.pyplot(fig2)




