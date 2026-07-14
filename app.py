import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("VR-Парк: Конструктор расписания")

# 1. Интерфейс ввода
with st.sidebar:
    st.header("Настройки мероприятия")
    start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())
    total_hours = st.number_input("Общая длительность (часы):", 1, 8, 3)
    total_mins = st.number_input("Дополнительные минуты:", 0, 59, 0)
    
    st.write("---")
    st.subheader("Добавьте зоны:")
    zones_input = []
    # Добавляем 5 слотов для зон
    for i in range(5):
        c1, c2, c3 = st.columns([2, 1, 1])
        z_name = c1.text_input(f"Зона {i+1}", key=f"n_{i}")
        z_h = c2.number_input("Ч", 0, 5, 0, key=f"h_{i}")
        z_m = c3.number_input("М", 0, 59, 0, key=f"m_{i}")
        if z_name and (z_h > 0 or z_m > 0):
            zones_input.append((z_name, z_h * 60 + z_m))

# 2. Логика генератора
total_duration = total_hours * 60 + total_mins
sbor = 15
pozdrav = 10
occupied_time = sum([z[1] for z in zones_input])
rest_time = total_duration - sbor - pozdrav - occupied_time

# 3. Вывод расписания
st.subheader("Сгенерированный тайминг:")
curr = datetime.combine(datetime.today(), start_time)

# Блок сбора
st.text(f"{curr.strftime('%H:%M')} - { (curr + timedelta(minutes=sbor)).strftime('%H:%M')} - Сбор гостей")
curr += timedelta(minutes=sbor)

# Блоки зон
for name, mins in zones_input:
    end = curr + timedelta(minutes=mins)
    st.text(f"{curr.strftime('%H:%M')} - {end.strftime('%H:%M')} - {name}")
    curr = end

# Блок отдыха (если осталось время)
if rest_time > 0:
    end = curr + timedelta(minutes=rest_time)
    st.text(f"{curr.strftime('%H:%M')} - {end.strftime('%H:%M')} - Комната отдыха (свободное время)")
    curr = end

# Поздравление
st.text(f"{curr.strftime('%H:%M')} - { (curr + timedelta(minutes=pozdrav)).strftime('%H:%M')} - Поздравление")
