import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("VR-Парк: Генератор сценариев")

# 1. Ввод времени
start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())

if st.button("Сгенерировать 3 варианта"):
    # Логика генерации сценариев
    scenarios = {
        "Частый": ["VR-Арена", "Гонки", "Поздравление", "Комната отдыха"],
        "Активный": ["VR-Арена", "Гонки", "Комната отдыха", "Поздравление"],
        "Сбалансированный": ["VR-Арена", "Гонки (ч.1)", "Поздравление", "Гонки (ч.2)", "Комната отдыха"]
    }
    
    cols = st.columns(3)
    for col, (name, steps) in zip(cols, scenarios.items()):
        with col:
            st.subheader(name)
            # Отображение сценария
            for i, step in enumerate(steps, 1):
                st.write(f"{i}. {step}")
            
            # Кнопки оценки
            if st.button(f"✅ Подходит", key=f"ok_{name}"):
                st.success("Скопировано!")
                # В будущем здесь будет команда для буфера
            if st.button(f"🔄 Другой формат", key=f"other_{name}"):
                st.warning("Отмечено для другого")
            if st.button(f"❌ Плохой", key=f"bad_{name}"):
                st.error("Отмечено как плохо")
