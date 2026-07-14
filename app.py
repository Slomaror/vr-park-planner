import streamlit as st
import pandas as pd

st.title("Планировщик мероприятий")

# Ссылка на CSV-экспорт
SHEET_URL = "https://docs.google.com/spreadsheets/d/1SOkxp55acIcaTUt_dKMtoab0Vo2ntExiQAnwPgk9hFk/export?format=csv&gid=636493329"

@st.cache_data(ttl=60)
def load_data():
    # header=3 говорит pandas, что заголовки начинаются с 4-й строки
    return pd.read_csv(SHEET_URL, header=3)

df = load_data()

st.write("### Структура таблицы (что видит программа):")
st.write(df.columns.tolist())  # Это покажет нам реальные названия колонок

st.write("### Все данные:")
st.dataframe(df)
