import streamlit as st
import pandas as pd

st.title("VR-Парк: Генератор сценариев")

# 1. Ввод времени начала
start_time = st.time_input("Время начала мероприятия:", value=pd.to_datetime("12:00").time())

# 2. Кнопка генерации
if st.button("Сгенерировать 3 варианта"):
    # Здесь логика генерации (пока имитация)
    variants = ["Частый", "Активный", "Сбалансированный"]
    
    cols = st.columns(3)
    for i, var in enumerate(variants):
        with cols[i]:
            st.subheader(var)
            # Имитация таблицы расписания
            st.text("12:00-13:00 VR-Арена\n13:00-13:15 Гонки")
            
            # Кнопки оценки
            if st.button(f"Подходит ({var})"):
                st.write("✅ Скопировано в буфер!")
                st.write(f'<script>navigator.clipboard.writeText("Расписание {var}...")</script>', unsafe_allow_html=True)
            
            st.button(f"Другой формат ({var})", key=f"other_{i}")
            st.button(f"Плохой ({var})", key=f"bad_{i}")

st.sidebar.info("Система обучается на ваших оценках!")
