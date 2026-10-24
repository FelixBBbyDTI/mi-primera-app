import streamlit as st

st.title("Mi primera aplicación en Streamlit")

st.write("¡Hola! Estoy aprendiendo Python para Ciencia de Datos en la PUCP.")

nombre = st.text_input("¿Cómo te llamas?")

if st.button("Saludar"):
    if nombre:
        st.success(f"¡Bienvenido, {nombre}!")
    else:
        st.warning("Por favor, escribe tu nombre.")
