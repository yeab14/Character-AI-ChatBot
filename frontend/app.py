import streamlit as st
import time
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Get base64 string for the profile image
profile_image_base64 = get_base64_image("profile.png")

# Custom CSS for styling
st.markdown(
    f"""
    <style>
    body {{
        background-color: #000;
        color: #fff;
    }}
    .stTextInput textarea {{
        background-color: #1e1e1e;
        color: #fff;
        font-family: 'Courier New', Courier, monospace;
        border: 1px solid #fff;
    }}
    .stButton button {{
    background-color: #000;
    color: #fff;
    border-radius: 25px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s ease; /* Apply transition to all properties */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add subtle shadow */
    }}
    .stButton button:hover {{
    background-color: #fff;
    color: #000;
    border: 1px solid #000;
    transform: scale(1); /* Scale up on hover for a slight zoom effect */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Increase shadow intensity */
    }}
    .sidebar {{
        background-color: #1e1e1e;
        padding: 20px;
        margin-right: 10px;
        border-radius: 10px;
    }}
    .sidebar-header {{
        font-size: 24px;
        font-weight: bold;
        color: #fff;
        margin-bottom: 5px;
    }}
    .sidebar-content {{
        font-size: 16px;
        line-height: 1.6;
        color: #fff;
    }}
    .chat-message, .chat-response {{
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 70%;
        font-size: 16px;
        display: flex;
        align-items: center;
    }}
    .chat-message {{
        background-color: #007BFF;
        color: white;
        align-self: flex-start;
    }}
    .chat-response {{
        background-color: #333;
        color: white;
        align-self: flex-end;
    }}
    .profile-picture {{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px;
    }}
    .profile-info {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }}
    .profile-name {{
        font-size: 20px;
        font-weight: bold;
        color: #fff;
        margin-top: 10px;
    }}
    .profile-description {{
        font-size: 16px;
        color: #fff;
        text-align: center;
    }}
    footer {{
        visibility: visible;
        text-align: center;
        padding: 20px;
        background-color: #1e1e1e;
        color: #fff;
        margin-top: 150px;
        border-top: 1px solid #fff;
    }}
    @keyframes typing {{
        from {{ width: 0 }}
        to {{ width: 100% }}
    }}
    .animation-text {{
        overflow: hidden; /* Ensures the text is not visible until animation starts */
        white-space: nowrap; /* Prevents text wrapping */
        animation: typing 2s steps(20, end);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

# Sidebar content
st.sidebar.markdown(
    """
    <div class="sidebar">
        <div class="sidebar-header">Zulekya</div>
        <div class="sidebar-content">
            Chat with an AI-powered character.<br><br>
            Enter your messages in the field below.<br>
            The AI will respond to your inputs.<br><br>
            Powered by Streamlit and FastAPI.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Profile display centered at the top
st.markdown('<div class="profile-info">', unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="text-align: center; margin-top: -90px;">
        <img src="data:image/png;base64,{profile_image_base64}" class="profile-picture" style="width: 130px; height: 130px; border-radius: 50%; margin-bottom: 5px; border: 5px solid #fff; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);">
       <div class="profile-name" style="font-size: 24px; font-weight: bold; color: #333; margin-top: 20px; margin-bottom: 10px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; letter-spacing: 1px; text-transform: uppercase;">
            Hey&#x1F44B; , I'm Zulekya
        </div>
         <div class="profile-description" style="font-size: 16px; color: #555; text-align: center; font-family: 'var(--font-alpina)', ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif; line-height: 1.6;">
            Your personal AI companion here to support you with warmth, wisdom, and a touch of magic.<br>
            Feel free to ask me anything – from advice to deep conversations or just to brighten your day 😊
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)





st.markdown('</div>', unsafe_allow_html=True)

# Chat history display with margin
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
        time.sleep(2)  # Simulate time delay for bot response
st.markdown('</div>', unsafe_allow_html=True)

# User input area
user_input = st.text_area("Enter your message here...", height=100)

# Send button functionality
if st.button("Send"):
    if user_input:
        with st.spinner("Generating response..."):
            try:
                # Simulate response from API
                response_text = f"Bot responds to: '{user_input}'"
                
                # Update chat history
                st.session_state['chat_history'].append(("You", user_input))
                st.session_state['chat_history'].append(("Bot", response_text))
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message.")

# Footer
st.markdown(
    """
    <footer>
    <p>Developed by Yeabsira Dereje. Powered by Streamlit and FastAPI.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)












