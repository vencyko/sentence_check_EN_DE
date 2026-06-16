#from gemini -> Създаване на софтуер за проверка на немски
import streamlit as str
import google.generativeai as genai
import os  # <--- Добавяме този модул за управление на системната среда

# Настройка на страницата в браузъра
str.set_page_config(page_title="Езиков Учител AI", page_icon="📝", layout="centered")

# Настройка на API ключа чрез Системна Променлива (Environment Variable)
try:
    current_key = str.secrets["GEMINI_API_KEY"]
    
    # Това казва директно на компютъра/сървъра: "Запомни този ключ глобално!"
    os.environ["GEMINI_API_KEY"] = current_key
    
    # Глобална конфигурация
    genai.configure(api_key=current_key)
except KeyError:
    str.error("⚠️ Грешка: Не е намерен GEMINI_API_KEY в настройките (Secrets) на Streamlit!")
    str.stop()

# Заглавие на сайта
str.title("📝 Интелигентен Езиков Учител")
str.write("Напишете изречение на немски или английски и изкуственият интелект ще го провери за грешки!")

# Избор на език чрез красиви бутони в уебсайта
language = str.radio("Изберете език за проверка:", ("Немски (DE)", "Английски (EN)"), horizontal=True)

# Текстово поле за въвеждане
user_sentence = str.text_input("Въведете изречението тук:", placeholder="Например: Ich gehen zu hause или He don't know nothing...")

# Бутон за проверка
if str.button("Провери изречението", type="primary"):
    if not user_sentence.strip():
        str.warning("Моля, въведете някакъв текст преди да натиснете бутона.")
    else:
        # Индикатор за зареждане (Spinner)
        with str.spinner("Учителят мисли и проверява... Моля, изчакайте."):
            
            # Определяне на инструкциите според езика
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
                # Инициализираме модела чисто (той сам ще си вземе ключа от os.environ)
                model = genai.GenerativeModel(
                    model_name='gemini-1.5-flash',
                    system_instruction=system_instruction
                )
                
                # Стандартна заявка без проблемни аргументи
                response = model.generate_content(f"Провери това изречение: {user_sentence}")
                
                # Показване на резултата в красива кутия
                str.subheader("Резултат от проверката:")
                str.info(response.text)
                
            except Exception as e:
                str.error(f"⚠️ Възникна грешка при връзката с Gemini: {e}")
