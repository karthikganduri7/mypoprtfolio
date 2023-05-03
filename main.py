import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.jpeg", width=300)

with col2:
    st.title("Karthik Ganduri")
    content = """ Hi, This is karthik Ganduri, Site Reliabilty Engineer by profession
    Working in Optum Technolgies
    Lives in Hyderabad, TG, India
    """
    st.info(content)