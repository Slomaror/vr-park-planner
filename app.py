import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("VR-Парк: Умный планировщик")

# --- Справочники ---
TARIFF_DATA = {
    "Серебро": 120, "Золото": 180, "Платина": 240, 
    "Титан": 240, "Изумруд": 240, "Бриллиант": 360
}
VARIANTS = ["Частый", "Активный", "Сбалансированный"]

# --- Интерфейс ---
col1, col2, col3 = st.columns(3)
with col1:
    tariff = st.selectbox("Тариф:", list(TARIFF_DATA.keys()))
with col2:
    duration = st.number_input("Длительность (мин):", 60, 480, TARIFF_DATA[tariff])
with col3:
    start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())

# --- Движок генерации (Логика) ---
def get_schedule(variant, duration, start_time):
    # Базовые блоки
    sbor = 15
    pozdrav = 10
    game_time = duration - sbor - pozdrav
    
    # Имитация сборки блоков (для примера "Золото")
    if variant == "Частый":
        return [("Сбор", sbor), ("Арена (цельная)", game_time * 0.7), ("Аура + Катания", game_time * 0.3), ("Поздравление", pozdrav)]
    elif variant == "Сбалансированный":
        return [("Сбор", sbor), ("Арена (ч.1)", game_time * 0.35), ("Перекус", 15), ("Арена (ч.2)", game_time * 0.35), ("Аура", game_time * 0.3), ("Поздравление", pozdrav)]
    else: # Активный
        return [("Сбор", sbor), ("Нон-стоп (Арена+Аура+Катания)", game_time), ("Поздравление", pozdrav)]

# --- Отображение ---
cols = st.columns(3)
for i, var in enumerate(VARIANTS):
    with cols[i]:
        with st.container(border=True):
            st.subheader(var)
            current_time = datetime.combine(datetime.today(), start_time)
            lines = []
            
            for task, minutes in get_schedule(var, duration, start_time):
                end_time = current_time + timedelta(minutes=minutes)
                lines.append(f"{current_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')} - {task}")
                current_time = end_time
            
            text_out = "\n".join(lines)
            st.text(text_out)
            
            if st.button("✅ Подходит (Скопировать)", key=f"copy_{var}"):
                st.info("Скопировано!") # Можно добавить JS для авто-копирования
