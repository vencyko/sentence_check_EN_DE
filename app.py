# from gemini -> Flask и Streamlit: Кога и как?

import streamlit as st

st.title("Просто приложение със Streamlit")

# Създава текстово поле на екрана
name = st.text_input("Въведи името си (Streamlit):", placeholder="Име...")

# Бутон, който проверява дали има въведено име
if st.button("Поздрави ме"):
    if name:
        st.success(f"Здравей, {name}! 👋")
    else:
        st.warning("Моля, първо въведи име.")
