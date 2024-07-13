import streamlit as st
import time
import base64
import requests

API_URL = "http://185.124.109.231:9000" 

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def list_characters():
    response = requests.get(f"{API_URL}/characters/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to load characters.")
        return []

def get_character(char_id):
    response = requests.get(f"{API_URL}/characters/{char_id}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Character not found.")
        return None

def chat_with_character(user_input, character_id):
    response = requests.post(f"{API_URL}/chat", json={"user_input": user_input, "character_id": character_id})
    if response.status_code == 200:
        return response.json()['response']
    else:
        st.error("Failed to get response from the character.")
        return ""

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
        resize: none;
        min-height: 30px; /* Decreased initial height */
        padding: 10px;
        width: calc(100% - 60px); /* Adjust width to accommodate send button */
        transition: width 0.3s ease-in-out, min-height 0.3s ease;
    }}
    .stTextInput textarea:focus {{
        border-color: #007BFF;
        width: calc(100% - 60px); /* Maintain adjusted width on focus */
        min-height: 50px; /* Increase height on focus */
    }}
    .stTextInput .stTextareaWrapper {{
        position: relative;
    }}

    
    .stButton button {{
        background-color: var(--btn-bg);
        color: var(--btn-text);
        border-radius: 5px;
        border: none;
        padding: 12px 24px;
        font-size: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 100%;
        max-width: 300px; /* Limit maximum width */
        margin: 10px auto; /* Center align horizontally */
        display: block; /* Ensure button is block level for full width */
        text-align: center; /* Center align text */
    }}
    .stButton button:hover {{
        background-color: var(--btn-hover-bg);
        color: var(--btn-hover-text);
        border: 1px solid var(--btn-hover-border);
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }}

    .send-button {{
        position: absolute;
        top: -95px;
        right: 10px;
        transform: translateY(-50%);
        background-color: #000;
        color: #fff;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        border: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }}
    .send-button:hover {{
        background-color: #333;
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
        color: var(--text-color);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }}
    .sidebar .sidebar-content {{
        font-size: 18px;
        color: var(--text-color);
        text-align: center;
        margin-bottom: 10px;
        font-family: 'var(--font-alpina)', ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif;
        line-height: 1.6;
    }}
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
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

st.markdown('</div>', unsafe_allow_html=True)

# Text input with dynamic sizing and send button as arrow-up icon
st.markdown('<div class="stTextareaWrapper">', unsafe_allow_html=True)
user_input = st.text_area("Type your message here...", key="user_input", height=None, max_chars=None)

send_button_html = """
<button class="send-button" onclick="sendMessage()">
    <i class="fas fa-arrow-up"></i>
</button>
"""

st.markdown(send_button_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# JavaScript to handle send button click
send_button_js = """
<script>
function sendMessage() {
    const userInput = document.querySelector('textarea[aria-label="Type your message here..."]');
    if (userInput.value.trim() !== "") {
        userInput.form.submit();
    }
}
</script>
"""

st.markdown(send_button_js, unsafe_allow_html=True)

# Footer
st.markdown(
    """
  <footer>
    <p>&copy; 2024 Zulekya Chatbot. All rights reserved. Developed by Yeabsira Dereje.</p>
</footer>

    """,
    unsafe_allow_html=True,
)












