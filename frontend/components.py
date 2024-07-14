import streamlit as st

def profile_info():
    profile_image_base64 = ""  # Replace with your base64 profile image
    st.markdown('<div class="profile-info">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: -90px;">
            <img src="data:image/png;base64,{profile_image_base64}" class="profile-picture" style="width: 130px; height: 130px; border-radius: 50%; margin-bottom: 5px; border: 5px solid var(--text-color); box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);">
            <div class="profile-name">
                Hey&#x1F44B; , I'm Zulekya
            </div>
            <div class="profile-description">
                Your personal AI companion here to support you with warmth, wisdom, and a touch of magic.<br>
                Feel free to ask me anything – from advice to deep conversations or just to brighten your day 😊
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

def chat_history_display():
    st.markdown('<div class="chat-container" style="margin-top: 50px;">', unsafe_allow_html=True)
    for sender, message_text in st.session_state['chat_history']:
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

def sidebar_content():
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

def create_button():
    if st.sidebar.button("✏️ Create", key="create_button"):
        st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

def discover_button():
    if st.sidebar.button("🔍 Discover", key="discover_button"):
        st.sidebar.write("Discover new features coming soon!")
