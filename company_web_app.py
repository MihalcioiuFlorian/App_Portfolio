import streamlit as st
from PIL import Image
import pandas
import lorem

st.set_page_config(layout="wide")

p = lorem.text()
st.header("The best company")
st.text(p)

st.subheader("Our team: ")

#prepare the columns
col1, col2, col3 = st.columns(3)

#make a dataframe
df = pandas.read_csv("company_data.csv", sep=',')
rows_number = len(df)
a = rows_number // 3  # catul impartirii
b = rows_number % 3  # restul impartirii

image13 = Image.open('company_photos/13.png')
image13.thumbnail((200, 200))
image13.save('company_photos/13.png')
image14 = Image.open('company_photos/14.png')
image14.thumbnail((200, 200))
image14.save('company_photos/14.png')

#add data to the columns
if b == 0:
    with col1:
        for index, row in df[:a].iterrows():
            #add emplyee name
            st.header(row["first name"].title() + " " + row["last name"].title())
            #add employee role
            st.write(row["role"])
            #add employee image
            st.image("company_photos/" + row["image"])

    with col2:
        for index, row in df[a:a * 2].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])

    with col3:
        for index, row in df[a * 2:a * 3].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])
elif b == 1:
    with col1:
        for index, row in df[:a + 1].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])

    with col2:
        for index, row in df[a + 1:a * 2 + 1].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])

    with col3:
        for index, row in df[a * 2 + 1:a * 3 + 1].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])
elif b == 2:
    with col1:
        for index, row in df[:a + 1].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])

    with col2:
        for index, row in df[a + 1:a * 2 + 2].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])

    with col3:
        for index, row in df[a * 2 + 2:a * 3 + 2].iterrows():
            st.header(row["first name"].title() + " " + row["last name"].title())
            st.write(row["role"])
            st.image("company_photos/" + row["image"])
