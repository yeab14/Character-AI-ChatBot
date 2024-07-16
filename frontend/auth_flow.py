import streamlit as st
import auth
from app import main_app

def login_flow():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if auth.login(username, password):
            st.success("Logged in successfully!")
            st.session_state.user_logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")

def registration_flow():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password == confirm_password:
            if auth.register(username, password):
                st.success("Registered successfully!")
                st.session_state.user_logged_in = True
                st.experimental_rerun()
            else:
                st.error("Registration failed. Username may be taken.")
        else:
            st.error("Passwords do not match.")

# Redirect to main app if user is logged in
if 'user_logged_in' not in st.session_state:
    st.session_state.user_logged_in = False

if not st.session_state.user_logged_in:
    option = st.radio("Choose an option:", ("Login", "Register"))
    if option == "Login":
        login_flow()
    elif option == "Register":
        registration_flow()
else:
    main_app()
