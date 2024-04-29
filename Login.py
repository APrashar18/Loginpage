import streamlit as st

navigation = st.sidebar.selectbox("Search",["Sign Up", "Login"])

if navigation == "Sign Up":
    st.title("Sign Up")
    email = st.text_input("Email")
    username = st.text_input("Username")
    if len(username) <= 4 or len(username) >= 14:
        st.error("Username must have more than 5 characters and less than 14 characters")
    password = st.text_input("Password", type = "password")
    if len(password) < 8:
        st.error("Password must have 8 or more characters")
    st.button("Sign Up")

if navigation == "Login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type = "password")
    st.button("Login")

print("Hello")