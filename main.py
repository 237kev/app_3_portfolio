import streamlit as st
import pandas

st.set_page_config(layout= 'wide')
col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])  # Adjust column width ratio.

with col1:
    st.image("images/photo.jpg", width=700)  # Set a reasonable width for web display

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

col3, col4 = st.columns(2)
df = pandas.read_csv('data.csv', sep=';')

with col3:
#    for value in df[df.columns[0]]:
#        st.header(value)
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write (f"[Source Code]({row['url']})",unsafe_allow_html=True)


with col4:

    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write (f"[Source Code]({row['url']})",unsafe_allow_html=True)


#st.write(df)
#with col4:
 #   for index, row in df.iterrows():
 #       print(row)