import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_profile(image_base64, profile_name, profile_description):
    st.markdown('<div class="profile-info">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: -90px;">
            <img src="data:image/png;base64,{image_base64}" class="profile-picture" style="width: 130px; height: 130px; border-radius: 50%; margin-bottom: 5px; border: 5px solid var(--text-color); box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);">
            <div class="profile-name">
                Hey&#x1F44B; , I'm {profile_name}
            </div>
            <div class="profile-description">
                {profile_description}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def display_sidebar():
    st.sidebar.markdown(
        """
        <div class="sidebar">
            <div class="sidebar-header">Zulekya</div>
            <div class="sidebar-content">
                Chat with an AI-powered character.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.sidebar.button("✏️ Create", key="create_button"):
        st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

    if st.sidebar.button("🔍 Discover", key="discover_button"):
        st.sidebar.write("Discover new features coming soon!")

def display_chat_history(chat_history, profile_image_base64):
    st.markdown('<div class="chat-container" style="margin-top: 50px;">', unsafe_allow_html=True)
    for sender, message_text in chat_history:
        if sender == "You":
            st.markdown(
                f'''
                <div class="chat-message">
                    <img src="https://via.placeholder.com/40" class="profile-picture" />
                    <div class="chat-text">{message_text}</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'''
                <div class="chat-response">
                    <img src="data:image/png;base64,{profile_image_base64}" class="profile-picture" />
                    <div class="chat-text">{message_text}</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)

def display_footer(current_year):
    st.markdown(
        f"""
        <footer>
            <p>&copy; {current_year} Zulekya Chatbot, Developed by Yeabsira Dereje. All rights reserved.</p>
        </footer>
        """,
        unsafe_allow_html=True,
    )


