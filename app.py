import streamlit as st

st.set_page_config(layout="wide")
st.title("VR-Парк: Планировщик")

# --- Справочники ---
ALL_TARIFFS = ["Серебро", "Золото", "Платина", "Титан", "Изумруд", "Бриллиант"]
ADD_ONS = ["Нет", "10 катаний", "Безлимит на аттракционы"]
ZONES = ["VR-Арена (1)", "VR-Арена (2)", "VR-Арена (Объединенная)", "Аура", "Пиксель", "Аттракционы", "Комната отдыха"]

# --- Интерфейс ---
mode = st.radio("Режим:", ["Готовый тариф", "Индивидуальный"], horizontal=True)

if mode == "Готовый тариф":
    col1, col2, col3 = st.columns(3)
    with col1:
        pkg = st.selectbox("Тариф:", ALL_TARIFFS)
    with col2:
        add_on = st.selectbox("Доп. опция:", ADD_ONS)
    with col3:
        duration = st.number_input("Длительность (мин):", 60, 300, 120)
else:
    col1, col2 = st.columns(2)
    with col1:
        selected_zones = st.multiselect("Выберите зоны:", ZONES)
    with col2:
        duration = st.number_input("Длительность (мин):", 60, 300, 120)

st.write("---")

# --- Логика генерации (Карточки) ---
cols = st.columns(3)
variants = ["Частый", "Активный", "Сбалансированный"]

for i, var in enumerate(variants):
    with cols[i]:
        with st.container(border=True):
            st.subheader(var)
            st.write(f"Сценарий: [Здесь будет логика для {var}]")
            
            # Кнопки с обновлением только этого блока
            if st.button("✅ Подходит", key=f"ok_{var}"):
                st.success("Скопировано!")
            
            if st.button("🔄 Другой формат", key=f"alt_{var}"):
                st.rerun() # Обновляет страницу для имитации перегенерации
            
            if st.button("❌ Плохой", key=f"bad_{var}"):
                st.rerun()
