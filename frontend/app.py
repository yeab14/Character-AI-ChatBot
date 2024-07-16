import streamlit as st
import datetime
from components import get_base64_image, display_profile, display_sidebar, display_chat_history, display_footer
from api_requests import list_characters, get_character, chat_with_character
from styling import apply_custom_css

def main_app():
    # Apply custom CSS for styling
    apply_custom_css()

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

    # Get base64 string for the profile image
    profile_image_base64 = get_base64_image("profile.png")

    # Profile display centered at the top
    profile_name = "Zulekya"
    profile_description = "Your personal AI companion here to support you with warmth, wisdom, and a touch of magic.<br>Feel free to ask me anything – from advice to deep conversations or just to brighten your day 😊"
    display_profile(profile_image_base64, profile_name, profile_description)

    # Streamlit sidebar content
    display_sidebar()

    # Chat history display with margin
    display_chat_history(st.session_state['chat_history'], profile_image_base64)

    # Input area for user messages
    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        st.session_state['chat_history'].append(("You", user_input))
        response = chat_with_character(user_input)
        st.session_state['chat_history'].append(("Bot", f'<div class="animation-text">{response}</div>'))
        st.experimental_rerun()

    # Footer display
    current_year = datetime.datetime.now().year
    display_footer(current_year)

# To allow importing the function in auth_flow.py
if __name__ == "__main__":
    main_app()














