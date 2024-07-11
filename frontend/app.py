import streamlit as st
import requests

st.title("Roleplay Chatbot")

user_input = st.text_area("Enter your message here...")

if st.button("Send"):
    if user_input:
        response = requests.post(
            "http://localhost:8000/chat",
            json={"user_input": user_input}
        )
        if response.status_code == 200:
            st.write("**Response:**")
            st.write(response.json()["response"])
        else:
            st.write("Error:", response.status_code)
    else:
        st.write("Please enter a message.")
