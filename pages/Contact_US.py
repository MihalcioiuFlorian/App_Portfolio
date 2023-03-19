''' Sending email via python streamlit'''
import streamlit as st
from send_email import send_email

st.header("Contact us")

with st.form(key="email_forms"):    #form needs a key
    user_email = st.text_input("Your email adress...", placeholder="your_email@email.com")
    raw_message = st.text_area("Your message", placeholder="message...")  #allows multi-line text
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")  #special button design to submit the form it belongs to

    if button:
        send_email(message)
        st.info("Your email was sent succesfully!")