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
        background-color: var(--body-bg);
        color: var(--text-color);
    }}
    .stTextInput textarea {{
        background-color: var(--input-bg);
        color: var(--text-color);
        font-family: 'Courier New', Courier, monospace;
        border: 1px solid var(--text-color);
    }}
    .stButton button {{
        background-color: var(--btn-bg);
        color: var(--btn-text);
        border-radius: 25px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}
    .stButton button:hover {{
        background-color: var(--btn-hover-bg);
        color: var(--btn-hover-text);
        border: 1px solid var(--btn-hover-border);
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
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
        font-size: 25px;
        font-weight: bold;
        color: var(--text-color);
        margin-top: 20px;
        margin-bottom: 10px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    .profile-description {{
        font-size: 16px;
        color: var(--text-color);
        text-align: center;
        font-family: 'var(--font-alpina)', ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif;
        line-height: 1.6;
    }}
    footer {{
        visibility: visible;
        text-align: center;
        padding: 20px;
        background-color: var(--footer-bg);
        color: var(--text-color);
        margin-top: 150px;
        border-top: 1px solid var(--text-color);
    }}
    @keyframes typing {{
        from {{ width: 0 }}
        to {{ width: 100% }}
    }}
    .animation-text {{
        overflow: hidden;
        white-space: nowrap;
        animation: typing 2s steps(20, end);
    }}
    .sidebar .sidebar-header {{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #fff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }}

     .sidebar .sidebar-content {{
        font-size: 18px;
        color: #fff;
        text-align: center;
        font-family: 'var(--font-alpina)', ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif;
        line-height: 1.6;
    }}

    .stSidebar .sidebar-content .stButton {{
        margin-top: 20px;
    }}

     .sidebar .stButton button {{
    display: flex;
    align-items: center;
     text-align: center;
    justify-content: center;
    background-color: transparent;
    color: #fff;
    font-size: 18px;
    border: none;
    margin: 10px 0;
    transition: background-color 0.3s ease, color 0.3s ease;
    }}

    .sidebar .stButton button:hover {{
    background-color: #555;
    color: #fff;
    border: 2px solid #fff;
    cursor: pointer;
    }}
    .sidebar .stButton button i {{
        margin-right: 10px;
    }}
    </style>
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """,
    unsafe_allow_html=True,
)

# Set theme variables
st.markdown(
    """
    <style>
    :root {
        --body-bg: #000;
        --text-color: #fff;
        --input-bg: #1e1e1e;
        --btn-bg: #000;
        --btn-text: #fff;
        --btn-hover-bg: #fff;
        --btn-hover-text: #000;
        --btn-hover-border: #000;
        --footer-bg: #1e1e1e;
    }
    @media (prefers-color-scheme: light) {
        :root {
            --body-bg: #fff;
            --text-color: #000;
            --input-bg: #f1f1f1;
            --btn-bg: #000;
            --btn-text: #fff;
            --btn-hover-bg: #fff;
            --btn-hover-text: #000;
            --btn-hover-border: #000;
            --footer-bg: #f1f1f1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

# Profile display centered at the top
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

# Streamlit sidebar content
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

# Create and Discover buttons with icons
if st.sidebar.button("✏️ Create", key="create_button"):
    st.session_state['chat_history'] = [("Bot", '<div class="animation-text">Hello! How can I assist you today?</div>')]

if st.sidebar.button("🔍 Discover", key="discover_button"):
    st.sidebar.write("Discover new features coming soon!")

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












