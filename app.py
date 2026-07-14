import streamlit as st
import pandas as pd

# Заголовок вашего сайта
st.title("Планировщик мероприятий")

# Ссылка на вашу таблицу (вставьте свою ссылку сюда)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1SOkxp55acIcaTUt_dKMtoab0Vo2ntExiQAnwPgk9hFk/edit?gid=636493329#gid=636493329"

@st.cache_data(ttl=60)
def load_data():
    csv_url = SHEET_URL.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

# Загрузка данных из листа "Конструктор"
df = load_data()

st.write("Текущее расписание:")
st.dataframe(df)

# Кнопка для копирования
if st.button("Копировать расписание"):
    st.success("Расписание готово к копированию из таблицы ниже!")
