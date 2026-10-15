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
    Hello, I'm Fatemeh Gorji!
    I'm a Python Developer and a Master's student in Private Law.
    I'm passionate about programming and web development, and I enjoy turning ideas into functional applications through code.
    I'm always eager to learn new technologies, improve my skills, and explore creative ways to solve problems.
    My goal is to develop useful, user-friendly applications that meet people's needs while continuously growing as a programmer.
    """
    st.write(content)
content2 = """
Below you can find some of the apps I have built in Python. feel free to Contact.py me!
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