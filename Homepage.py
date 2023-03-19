import streamlit as st
from PIL import Image
import pandas
#pandas reads the csv file and displays the data in a table (dataframe)

base = 'light'

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 2])

with col1:
    # image = Image.open('images/photo.png')
    # new_image = image.resize((400, 400))
    # new_image.save('images/photo.png')
    st.image("images/photo.png", width=300)

with col2:
    st.title("Florian Mihalcioiu")
    content = """
    description about me
    """
    st.info(content)  # info() looks better than write() for what we need

some_info = "<p style='font-family:Comic Sans; color:DarkBlue; font-size: 30px;'>" \
            "Below you can find some of the apps I have developed in Python:</p>"
st.markdown(some_info, unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #width ratio of columns

df = pandas.read_csv("data.csv", sep=';')
#create a dataframe

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source Code]({row["url"]})')

#iterrows() - methd that gives acces to the rows and iterates on them
#st.text() - you need to write the text that you want to display on the website
#st.write() -> displays the text from csv file
#st.write('[text disaplyed on the page that will became link when you click it}(the actual link)')