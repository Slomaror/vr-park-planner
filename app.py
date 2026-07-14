import streamlit as st
from datetime import datetime, timedelta

# --- База знаний (Ваши идеальные шаблоны) ---
TEMPLATES = {
    "Платина": {
        "Частый": [("Сбор", 15), ("Арена (цельная)", 90), ("Отдых", 15), ("Пиксель + Аура", 45), ("Поздравление", 10), ("Отдых, чаепитие", 35), ("Аттракционы", 30)],
        "Сбалансированный": [("Сбор", 15), ("Арена (ч.1)", 45), ("Отдых", 15), ("Пиксель + Аура", 60), ("Арена (ч.2)", 45), ("Поздравление", 10), ("Отдых, чаепитие", 35), ("Аттракционы", 30)]
    }
}

# --- Логика ---
def get_schedule(tariff, variant, start_time):
    # Берем шаблон, если есть, или дефолт
    blocks = TEMPLATES.get(tariff, {}).get(variant, [("Сбор", 15), ("Игра", 60), ("Поздравление", 10)])
    
    curr = datetime.combine(datetime.today(), start_time)
    lines = []
    for task, minutes in blocks:
        end = curr + timedelta(minutes=minutes)
        lines.append(f"{curr.strftime('%H:%M')}-{end.strftime('%H:%M')} - {task}")
        curr = end
    return "\n".join(lines)

# --- Интерфейс ---
tariff = st.selectbox("Тариф:", ["Платина", "Золото", "Серебро"])
start_time = st.time_input("Время начала:", value=datetime.strptime("12:00", "%H:%M").time())

cols = st.columns(3)
for i, var in enumerate(["Частый", "Активный", "Сбалансированный"]):
    with cols[i]:
        st.subheader(var)
        st.text(get_schedule(tariff, var, start_time))
        if st.button(f"🔄 Перегенерировать {var}", key=f"btn_{i}"): st.rerun()
