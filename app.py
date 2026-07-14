import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("VR-Парк: Планировщик")

# --- Настройки зон ---
ZONES = ["VR-Арена (1)", "VR-Арена (2)", "VR-Арена (Объединенная)", "Аура", "Пиксель", "Аттракционы", "Комната отдыха"]
PACKAGES = ["Серебро", "Золото", "Платина"]

# --- Интерфейс ---
mode = st.radio("Режим:", ["Готовый тариф", "Индивидуальный"])

if mode == "Готовый тариф":
    pkg = st.selectbox("Тариф:", PACKAGES)
    duration = st.number_input("Длительность мероприятия (мин):", 60, 300, 120)
else:
    selected_zones = st.multiselect("Выберите зоны:", ZONES)
    duration = st.number_input("Длительность (мин):", 60, 300, 120)

start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())

# --- Логика генерации ---
if st.button("Сгенерировать 3 варианта"):
    cols = st.columns(3)
    variants = ["Частый", "Активный", "Сбалансированный"]
    
    for i, var in enumerate(variants):
        with cols[i]:
            st.subheader(var)
            # Здесь мы будем вызывать функцию генерации расписания
            st.write(f"Сценарий для {var}")
            
            # Кнопки оценки
            if st.button(f"Подходит", key=f"btn_ok_{i}"):
                st.success("Скопировано!")
            st.button(f"Другой формат", key=f"btn_alt_{i}")
            st.button(f"Плохой", key=f"btn_bad_{i}")
