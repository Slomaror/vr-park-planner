import streamlit as st
import pandas as pd

st.title("Планировщик мероприятий")

# Ссылка на CSV-экспорт
SHEET_URL = "https://docs.google.com/spreadsheets/d/1SOkxp55acIcaTUt_dKMtoab0Vo2ntExiQAnwPgk9hFk/export?format=csv&gid=636493329"

@st.cache_data(ttl=60)
def load_data():
    # header=3, так как заголовки начинаются с 4-й строки (индекс 3)
    return pd.read_csv(SHEET_URL, header=3)

df = load_data()

# Оставляем только строки, где есть название зоны
df_clean = df.dropna(subset=['Название зоны'])

# Выбираем для отображения только нужные столбцы
df_final = df_clean[['Название зоны', 'Начало', 'Конец']]

st.write("### Текущее расписание:")
st.table(df_final)

# Добавляем возможность скачать данные
csv = df_final.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Скачать расписание (CSV)",
    data=csv,
    file_name='raspisanie.csv',
    mime='text/csv',
)
