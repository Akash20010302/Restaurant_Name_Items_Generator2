import streamlit as st
import langchain_helper

st.title("Restauraunt Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic","American"))



if cuisine:
    response = langchain_helper.generate_restraunt_name_and_items(cuisine)
    st.header(response['restraunt_name'].strip())
    menu_items = response['menu_items'].strip().split(",") # This will return me as a list
    st.write("**Menu Items**")
    for i in menu_items:
        st.write("-", i)