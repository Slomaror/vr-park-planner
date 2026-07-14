import streamlit as st

st.set_page_config(layout="wide")
st.title("VR-Парк: Планировщик")

# --- Справочники ---
TARIFF_DURATIONS = {
    "Серебро": 120,
    "Золото": 180,
    "Платина": 240,
    "Титан": 240,
    "Изумруд": 240,
    "Бриллиант": 360
}
ALL_TARIFFS = list(TARIFF_DURATIONS.keys())
ADD_ONS = ["Нет", "10 катаний", "Безлимит на аттракционы"]
ZONES = ["VR-Арена (1)", "VR-Арена (2)", "VR-Арена (Объединенная)", "Аура", "Пиксель", "Аттракционы", "Комната отдыха"]

# --- Логика состояния ---
if 'duration' not in st.session_state:
    st.session_state.duration = TARIFF_DURATIONS[ALL_TARIFFS[0]]

# --- Интерфейс ---
mode = st.radio("Режим:", ["Готовый тариф", "Индивидуальный"], horizontal=True)

if mode == "Готовый тариф":
    col1, col2, col3 = st.columns(3)
    with col1:
        # При смене тарифа обновляем длительность
        pkg = st.selectbox("Тариф:", ALL_TARIFFS)
        if st.button("Применить тариф"):
            st.session_state.duration = TARIFF_DURATIONS[pkg]
    with col2:
        add_on = st.selectbox("Доп. опция:", ADD_ONS)
    with col3:
        # Поле ввода, которое можно менять вручную
        duration = st.number_input("Длительность (мин):", 60, 480, st.session_state.duration)
        st.session_state.duration = duration
else:
    selected_zones = st.multiselect("Выберите зоны:", ZONES)
    duration = st.number_input("Длительность (мин):", 60, 480, st.session_state.duration)

st.write("---")

# --- Логика генерации ---
cols = st.columns(3)
variants = ["Частый", "Активный", "Сбалансированный"]

for i, var in enumerate(variants):
    with cols[i]:
        with st.container(border=True):
            st.subheader(var)
            st.write(f"Длительность: {st.session_state.duration} мин")
            
            if st.button("✅ Подходит", key=f"ok_{var}"):
                st.success("Скопировано!")
            if st.button("🔄 Другой формат", key=f"alt_{var}"):
                st.rerun()
            if st.button("❌ Плохой", key=f"bad_{var}"):
                st.rerun()
