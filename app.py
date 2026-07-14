import streamlit as st
import pandas as pd

st.title("Планировщик мероприятий")

# Ссылка на данные
SHEET_URL = "https://docs.google.com/spreadsheets/d/1SOkxp55acIcaTUt_dKMtoab0Vo2ntExiQAnwPgk9hFk/export?format=csv&gid=636493329"

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv(SHEET_URL, header=3)

df = load_data()
df_clean = df.dropna(subset=['Название зоны'])
df_final = df_clean[['Название зоны', 'Начало', 'Конец']]

st.table(df_final)

# Формируем текст для копирования
text_to_copy = df_final.to_string(index=False)

# Выводим текстовое поле, которое удобно выделить и скопировать
st.text_area("Скопируйте расписание отсюда (Ctrl+C):", value=text_to_copy, height=200)
