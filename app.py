import streamlit as st
import pandas as pd

st.title("Планировщик мероприятий")

# Ссылка на вашу Google Таблицу
SHEET_URL = "https://docs.google.com/spreadsheets/d/1SOkxp55acIcaTUt_dKMtoab0Vo2ntExiQAnwPgk9hFk/export?format=csv"

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv(SHEET_URL)

# Загружаем данные
df = load_data()

# Берем только нужные колонки
df_clean = df[['Название зоны', 'Начало', 'Конец']].dropna(how='all')

st.write("### Текущее расписание:")
st.table(df_clean)
