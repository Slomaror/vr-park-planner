import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("VR-Парк: Умный планировщик")

# --- Справочники ---
TARIFF_DATA = {"Серебро": 120, "Золото": 180, "Платина": 240, "Титан": 240, "Изумруд": 240, "Бриллиант": 360}
ADD_ONS = ["Нет", "10 катаний", "Безлимит на аттракционы"]
VARIANTS = ["Частый", "Активный", "Сбалансированный"]

# --- Интерфейс ---
mode = st.radio("Режим:", ["Готовый тариф", "Индивидуальный"], horizontal=True)

if mode == "Готовый тариф":
    c1, c2, c3 = st.columns(3)
    tariff = c1.selectbox("Тариф:", list(TARIFF_DATA.keys()))
    add_on = c2.selectbox("Доп. опция:", ADD_ONS)
    duration = c3.number_input("Длительность (мин):", 60, 480, TARIFF_DATA[tariff])
else:
    c1, c2 = st.columns(2)
    zones = c1.multiselect("Выберите зоны:", ["Арена", "Аура", "Пиксель", "Аттракционы"])
    duration = c2.number_input("Длительность (мин):", 60, 480, 180)

start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())

# --- Логика генерации ---
def get_blocks(variant, total_dur):
    # Сбор всегда за 15 минут до начала (внутри 15-мин блока)
    blocks = [("Сбор гостей", 15)]
    game_time = total_dur - 15 - 10 # 10 - Поздравление
    
    if variant == "Частый":
        blocks += [("Арена (цельная)", game_time * 0.7), ("Аура+Катания", game_time * 0.3)]
    elif variant == "Сбалансированный":
        blocks += [("Арена ч.1", game_time * 0.35), ("Перекус", 15), ("Арена ч.2", game_time * 0.35), ("Аура", game_time * 0.2)]
    else:
        blocks += [("Активный нон-стоп", game_time)]
    
    blocks.append(("Поздравление", 10))
    return blocks

st.write("---")
cols = st.columns(3)

# Инициализация сессии для кнопок "Другой формат"
if 'rerun_count' not in st.session_state: st.session_state.rerun_count = 0

for i, var in enumerate(VARIANTS):
    with cols[i]:
        with st.container(border=True):
            st.subheader(var)
            curr = datetime.combine(datetime.today(), start_time)
            for task, minutes in get_blocks(var, duration):
                end = curr + timedelta(minutes=minutes)
                st.text(f"{curr.strftime('%H:%M')}-{end.strftime('%H:%M')} - {task}")
                curr = end
            
            if st.button("✅ Подходит", key=f"ok_{i}"): st.success("Скопировано!")
            if st.button("🔄 Другой формат", key=f"alt_{i}"): st.rerun()
