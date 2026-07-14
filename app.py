import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title("VR-Парк: Умный конструктор")

# Справочник доступных зон
AVAILABLE_ZONES = ["VR-Арена", "Зона Ауры", "Пиксель", "Аттракционы", "Шоу ведущего", "Квиз", "Мафия"]

# 1. Боковая панель
with st.sidebar:
    st.header("Настройки")
    start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())
    total_minutes = st.number_input("Общая длительность (минут):", 60, 480, 180)
    
    st.write("---")
    st.subheader("Зоны мероприятия")
    # Динамический список зон
    if 'zones_list' not in st.session_state:
        st.session_state.zones_list = [{"name": "VR-Арена", "time": 60}]

    for i, z in enumerate(st.session_state.zones_list):
        c1, c2 = st.columns([2, 1])
        st.session_state.zones_list[i]["name"] = c1.selectbox(f"Зона {i+1}", AVAILABLE_ZONES, index=AVAILABLE_ZONES.index(z["name"]), key=f"n_{i}")
        st.session_state.zones_list[i]["time"] = c2.number_input("Мин", 0, 300, z["time"], key=f"t_{i}")

    if st.button("➕ Добавить зону"):
        st.session_state.zones_list.append({"name": "VR-Арена", "time": 30})
        st.rerun()

# 2. Логика расчёта
sbor = 15
pozdrav = 10
occupied = sum(z["time"] for z in st.session_state.zones_list)
rest = total_minutes - sbor - pozdrav - occupied

# 3. Вывод расписания
st.subheader("Сгенерированный тайминг:")
curr = datetime.combine(datetime.today(), start_time)

# Пошаговая сборка
schedule = [(curr, "Сбор гостей", sbor)]
curr += timedelta(minutes=sbor)

for z in st.session_state.zones_list:
    schedule.append((curr, z["name"], z["time"]))
    curr += timedelta(minutes=z["time"])

if rest > 0:
    schedule.append((curr, "Комната отдыха (свободное время)", rest))
    curr += timedelta(minutes=rest)

schedule.append((curr, "Поздравление", pozdrav))

# Отображение
for t, name, dur in schedule:
    st.text(f"{t.strftime('%H:%M')} - {(t + timedelta(minutes=dur)).strftime('%H:%M')} — {name}")
