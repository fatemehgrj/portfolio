import streamlit as st
import pandas
st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/Picsart_26-10-08_10-03-32-931.jpg")

df = pandas.read_csv("./data.csv", sep=";")
with col2:
    st.title("_Fatemeh Gorji_")
    #تو خونه به فارسی درباره خودت تحصیلاتت و
    #تجربه برنامه نویسی برای هوش مصنوعی می نویسی
    #بعدش به انگلیسی تبدیلش میکنی واینجا پیست میکنی

    content="""
    Hi I am Fatemeh! I am Python programme and student.
    """
    st.write(content)
content2 = """
Below you can find some of the apps I have built in Python. feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])