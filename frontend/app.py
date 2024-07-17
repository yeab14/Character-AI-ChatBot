# app.py

import streamlit as st
import datetime
from components import get_base64_image, display_profile, display_sidebar, display_chat_history, display_footer
from api_requests import chat_with_character
from styling import apply_custom_css

def main_app():
    # Apply custom CSS for styling
    apply_custom_css()

    # Check if a character is selected
    if 'chat_character' not in st.session_state:
        st.session_state['chat_character'] = {
            "id": "default",
            "name": "Zulekya",
            "description": "Your personal AI companion here to support you with warmth, wisdom, and a touch of magic.<br>Feel free to ask me anything – from advice to deep conversations or just to brighten your day 😊",
            "image": "profile.png"
        }

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

    # Get base64 string for the profile image
    profile_image_base64 = get_base64_image(st.session_state['chat_character']["image"])

    # Profile display centered at the top
    profile_name = st.session_state['chat_character']["name"]
    profile_description = st.session_state['chat_character']["description"]
    display_profile(profile_image_base64, profile_name, profile_description)

    # Streamlit sidebar content
    display_sidebar()

    # Chat history display with margin
    display_chat_history(st.session_state['chat_history'], profile_image_base64)

    # Input area for user messages
    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        st.session_state['chat_history'].append(("You", user_input))
        response = chat_with_character(user_input, st.session_state['chat_character']["id"])
        st.session_state['chat_history'].append(("Bot", f'<div class="animation-text">{response}</div>'))
        st.experimental_rerun()

    # Footer display
    current_year = datetime.datetime.now().year
    display_footer(current_year)

if __name__ == "__main__":
    main_app()














