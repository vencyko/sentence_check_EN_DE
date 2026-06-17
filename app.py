# from gemini -> Flask и Streamlit: Кога и как?
'''
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
'''
import streamlit as st
import requests

st.set_page_config(page_title="ESP8266 Контролер", page_icon="💡")

st.title("💡 Контрол на ESP8266 през Wi-Fi")
st.write("Управлявай светодиода на твоята платка в реално време.")

# Текстово поле, където въвеждаш IP адреса на ESP8266
esp_ip = st.text_input("Въведи IP адреса на ESP8266:", value="192.168.1.50")

# Базов URL адрес за заявките
base_url = f"http://{esp_ip}"

st.subheader("Управление:")

# Създаваме две колони за бутоните един до друг
col1, col2 = st.columns(2)

with col1:
    if st.button("🔴 ВКЛЮЧИ СВЕТОДИОДА", use_container_width=True):
        try:
            # Изпращаме GET заявка към ESP8266
            response = requests.get(f"{base_url}/led/on", timeout=3)
            if response.status_code == 200:
                st.success("Сигналът е изпратен: Светодиодът свети!")
        except requests.exceptions.RequestException:
            st.error("Грешка: Неуспешна връзка с ESP8266. Провери IP адреса.")

with col2:
    if st.button("⚪ ИЗКЛЮЧИ СВЕТОДИОДА", use_container_width=True):
        try:
            response = requests.get(f"{base_url}/led/off", timeout=3)
            if response.status_code == 200:
                st.info("Сигналът е изпратен: Светодиодът е изгасен.")
        except requests.exceptions.RequestException:
            st.error("Грешка: Неуспешна връзка с ESP8266. Провери IP адреса.")
