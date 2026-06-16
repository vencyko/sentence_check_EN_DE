import streamlit as str
from google import genai  # <--- Новият начин за импортиране

# Настройка на страницата в браузъра
str.set_page_config(page_title="Езиков Учител AI", page_icon="📝", layout="centered")

# Инициализиране на клиента с новия пакет
try:
    # Новият пакет автоматично знае как да обработи "AQ" ключа през Streamlit Secrets
    client = genai.Client(api_key=str.secrets["GEMINI_API_KEY"])
except Exception as e:
    str.error(f"⚠️ Грешка при настройката на ключа: {e}")
    str.stop()

# Заглавие на сайта
str.title("📝 Интелигентен Езиков Учител")
str.write("Напишете изречение на немски или английски и изкуственият интелект ще го провери за грешки!")

# Избор на език
language = str.radio("Изберете език за проверка:", ("Немски (DE)", "Английски (EN)"), horizontal=True)

# Текстово поле за въвеждане
user_sentence = str.text_input("Въведете изречението тук:", placeholder="Например: Ich gehen zu hause...")

# Бутон за проверка
if str.button("Провери изречението", type="primary"):
    if not user_sentence.strip():
        str.warning("Моля, въведете някакъв текст преди да натиснете бутона.")
    else:
        with str.spinner("Учителят мисли и проверява... Моля, изчакайте."):
            
            if "Немски" in language:
                system_instruction = (
                    "Ти си строг, но полезен учител по немски език. Твоята задача е да проверяваш изречения. "
                    "Ако изречението е вярно, напиши 'Правилно!'. Ако има грешки (граматика, правопис, словоред, падежи), "
                    "напиши поправената версия и обясни накратко каква е грешката на български език."
                )
            else:
                system_instruction = (
                    "Ти си строг, но полезен учител по английски език. Твоята задача е да проверяваш изречения. "
                    "Ако изречението е вярно, напиши 'Правилно!'. Ако има грешки (времена, правопис, предлози, словоред), "
                    "напиши поправената версия и обясни накратко каква е грешката на български език."
                )
            
            try:
                # Новият синтаксис за извикване на Gemini 1.5 Flash
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=f"Провери това изречение: {user_sentence}",
                    config=genai.types.GenerateContentConfig(
                        system_instruction=system_instruction
                    )
                )
                
                # Показване на резултата
                str.subheader("Резултат от проверката:")
                str.info(response.text)
                
            except Exception as e:
                str.error(f"⚠️ Възникна грешка при връзката с Gemini: {e}")
