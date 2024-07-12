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
        transition: background-color 0.3s ease;
    }}
    .stButton button:hover {{
        background-color: #fff;
        color: #000;
         border: 1px solid #000;
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
        margin-bottom: 10px;
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
    .chat-text {{
        flex-grow: 1;
    }}
    footer {{
        visibility: visible;
        text-align: center;
        padding: 20px;
        background-color: #1e1e1e;
        color: #fff;
        margin-top: 200px; 
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
        <div class="sidebar-header">Roleplay Chatbot</div>
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

# Main content
st.title("Roleplay Chatbot")

# Chat history display
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
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









