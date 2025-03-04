import streamlit as st

st.set_page_config(layout='wide')
col1, col2 = st.columns([1, 6])  # Adjust column width ratio

with col1:
    st.image("images/photo.jpg", width=250)  # Set a reasonable width for web display

with col2:
    st.title("Kevin KAMDEM")
    content = """
    I am Kevin KAMDEM,  
    a Bachelor of Engineering graduate in Automotive Systems Engineering from Heilbronn University (2020).  
    I have worked as an Electronics Developer and Software Engineer,  
    specializing in C++ development, embedded systems,  
    and real-time applications.  

    Now, I focus on entrepreneurial projects in real estate, digital content management,  
    and international recruitment, combining my technical expertise with business innovation.
    """
    st.write(content)

st.write("🚀 You can find the apps I have built below. Feel free to contact me!")