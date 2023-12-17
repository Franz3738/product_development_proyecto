import streamlit as st
import requests

# URL de tu API de Flask
API_URL = "http://127.0.0.1:5000/predict"

def predict(data):
    response = requests.post(API_URL, json=data)
    return response.json()

# Título de la aplicación Streamlit
st.title("Aplicación de Predicción de Modelos")

# Definición de los mínimos y máximos para cada variable
min_values = {
    "Density": 1.0101,
    "Age": 22,
    "Weight": 118.5,
    "Height": 29.5,
    "Neck": 31.1,
    "Chest": 83.4,
    "Abdomen": 69.4,
    "Hip": 85,
    "Thigh": 47.2,
    "Knee": 33,
    "Ankle": 19.1,
    "Biceps": 24.8,
    "Forearm": 21,
    "Wrist": 15.8
}

max_values = {
    "Density": 1.1089,
    "Age": 81,
    "Weight": 363.15,
    "Height": 77.75,
    "Neck": 51.2,
    "Chest": 136.2,
    "Abdomen": 148.1,
    "Hip": 147.7,
    "Thigh": 87.3,
    "Knee": 49.1,
    "Ankle": 33.9,
    "Biceps": 45,
    "Forearm": 34.9,
    "Wrist": 21.4
}

# Crear un formulario para ingresar datos usando sliders
with st.form("form_model_predict", clear_on_submit=True):
    density = st.slider("Density", min_value=float(min_values["Density"]), max_value=float(max_values["Density"]), value=float(min_values["Density"]), format="%.4f")
    age = st.slider("Age", min_value=int(min_values["Age"]), max_value=int(max_values["Age"]), value=int(min_values["Age"]))
    weight = st.slider("Weight", min_value=float(min_values["Weight"]), max_value=float(max_values["Weight"]), value=float(min_values["Weight"]), format="%.2f")
    height = st.slider("Height", min_value=float(min_values["Height"]), max_value=float(max_values["Height"]), value=float(min_values["Height"]), format="%.2f")
    neck = st.slider("Neck", min_value=float(min_values["Neck"]), max_value=float(max_values["Neck"]), value=float(min_values["Neck"]), format="%.2f")
    chest = st.slider("Chest", min_value=float(min_values["Chest"]), max_value=float(max_values["Chest"]), value=float(min_values["Chest"]), format="%.2f")
    abdomen = st.slider("Abdomen", min_value=float(min_values["Abdomen"]), max_value=float(max_values["Abdomen"]), value=float(min_values["Abdomen"]), format="%.2f")
    hip = st.slider("Hip", min_value=float(min_values["Hip"]), max_value=float(max_values["Hip"]), value=float(min_values["Hip"]), format="%.2f")
    thigh = st.slider("Thigh", min_value=float(min_values["Thigh"]), max_value=float(max_values["Thigh"]), value=float(min_values["Thigh"]), format="%.2f")
    knee = st.slider("Knee", min_value=float(min_values["Knee"]), max_value=float(max_values["Knee"]), value=float(min_values["Knee"]), format="%.2f")
    ankle = st.slider("Ankle", min_value=float(min_values["Ankle"]), max_value=float(max_values["Ankle"]), value=float(min_values["Ankle"]), format="%.2f")
    biceps = st.slider("Biceps", min_value=float(min_values["Biceps"]), max_value=float(max_values["Biceps"]), value=float(min_values["Biceps"]), format="%.2f")
    forearm = st.slider("Forearm", min_value=float(min_values["Forearm"]), max_value=float(max_values["Forearm"]), value=float(min_values["Forearm"]), format="%.2f")
    wrist = st.slider("Wrist", min_value=float(min_values["Wrist"]), max_value=float(max_values["Wrist"]), value=float(min_values["Wrist"]), format="%.2f")

    submitted = st.form_submit_button("Predecir con Todos los Modelos")
    if submitted:
        data = {
            "Density": density, 
            "Age": age, 
            "Weight": weight, 
            "Height": height,
            "Neck": neck,
            "Chest": chest,
            "Abdomen": abdomen,
            "Hip": hip,
            "Thigh": thigh,
            "Knee": knee,
            "Ankle": ankle,
            "Biceps": biceps,
            "Forearm": forearm,
            "Wrist": wrist
        }
        prediction = predict(data)
        st.write("Predicciones:")
        st.json(prediction)
