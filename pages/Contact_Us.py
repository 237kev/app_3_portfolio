import streamlit as st
from click import option
import pandas as pd

from send_email import send_email
st.header('Contact Me')

df = pd.read_csv(filepath_or_buffer= 'topics.csv')
with st.form(key='email_forms'):
    user_email = st.text_input('your email address')
    subject = st.selectbox(label='select a topic', options=df, placeholder="Choose an option")
    raw_message = st.text_area('your message')
    message = f"""\
Subject: New email from {user_email}

Topic: {subject}
send From: {user_email}
{raw_message}"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info('your email was send succesfully')
