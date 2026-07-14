import streamlit as st
import pandas as pd
from datetime import datetime

st.title("VR-Парк: Планировщик")

# --- Настройки ---
ZONES = ["VR-Арена (1)", "VR-Арена (2)", "VR-Арена (Объединенная)", "Аура", "Пиксель", "Аттракционы"]
PACKAGES = ["Серебро", "Золото", "Платина"]
ADD_ONS = ["Нет", "10 катаний", "Безлимит на аттракционы"]

# --- Интерфейс ---
mode = st.radio("Режим:", ["Готовый тариф", "Индивидуальный"])

if mode == "Готовый тариф":
    col1, col2 = st.columns(2)
    with col1:
        pkg = st.selectbox("Тариф:", PACKAGES)
    with col2:
        add_on = st.selectbox("Доп. опция:", ADD_ONS)
    duration = st.number_input("Длительность (мин):", 60, 300, 120)
else:
    selected_zones = st.multiselect("Выберите зоны:", ZONES + ["Аттракционы"])
    duration = st.number_input("Длительность (мин):", 60, 300, 120)

start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())

# --- Логика генерации ---
if st.button("Сгенерировать 3 варианта"):
    st.write("---")
    cols = st.columns(3)
    variants = ["Частый", "Активный", "Сбалансированный"]
    
    for i, var in enumerate(variants):
        with cols[i]:
            st.subheader(var)
            # Здесь будет вызываться движок генерации расписания
            st.info(f"Сценарий: {var}\nДлительность: {duration} мин")
            
            if st.button(f"Подходит", key=f"btn_ok_{i}"):
                st.success("Скопировано в буфер!")
            st.button(f"Другой формат", key=f"btn_alt_{i}")
            st.button(f"Плохой", key=f"btn_bad_{i}")
