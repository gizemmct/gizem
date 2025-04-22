import streamlit as st
import pickle
import numpy as np

st.title("Maaş Tahmin Uygulaması")
st.subheader("Linear Regresyonla Tahmin")

experience = st.number_input("Tecrübe (yıl)", min_value=0.0, step=0.1)

try:
    with open("linear_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model dosyası bulunamadı. Lütfen önce modeli eğitin.")
    st.stop()

# Tahmin
if st.button("Tahmin Et"):
    input_array = np.array([[experience]]) 
    prediction = model.predict(input_array)
    st.success(f" Tahmini Maaş: {prediction[0]:,.2f} ₺")
