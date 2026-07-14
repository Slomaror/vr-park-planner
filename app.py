import streamlit as st
import random

# Настройка страницы
st.set_page_config(layout="wide")
st.title("VR-Парк: Планировщик")

# Инициализация состояния для каждого варианта
if 'scenarios' not in st.session_state:
    st.session_state.scenarios = {
        "Частый": "Сценарий: VR-Арена -> Гонки -> Поздравление",
        "Активный": "Сценарий: Гонки -> Арена -> Аттракционы",
        "Сбалансированный": "Сценарий: Арена (ч.1) -> Поздравление -> Арена (ч.2)"
    }

def regenerate_option(option_name):
    # Логика "генерации" (здесь будет ваш алгоритм)
    st.session_state.scenarios[option_name] = f"Новый сценарий {random.randint(1,100)} для {option_name}"

# Интерфейс ввода
col_input1, col_input2 = st.columns(2)
with col_input1:
    pkg = st.selectbox("Тариф:", ["Серебро", "Золото", "Платина"])
with col_input2:
    duration = st.number_input("Длительность (мин):", 60, 300, 120)

# Генерация карточек
st.write("---")
cols = st.columns(3)

for i, (name, content) in enumerate(st.session_state.scenarios.items()):
    with cols[i]:
        # Контейнер для фиксации размера
        with st.container(border=True):
            st.subheader(name)
            st.write(content)
            
            # Кнопки действия
            if st.button("✅ Подходит", key=f"ok_{name}"):
                st.success("Скопировано!")
                st.write(f'<script>navigator.clipboard.writeText("{content}")</script>', unsafe_allow_html=True)
            
            # Перегенерация только одного блока
            if st.button("🔄 Другой формат", key=f"alt_{name}"):
                regenerate_option(name)
                st.rerun()
            
            if st.button("❌ Плохой", key=f"bad_{name}"):
                regenerate_option(name)
                st.rerun()
