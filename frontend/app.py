import streamlit as st
import requests

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stTextInput textarea {
        background-color: #2e2e2e;
        color: #e5e5e5;
        font-family: 'Courier New', Courier, monospace;
        border: 1px solid #007BFF;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .sidebar {
        background-color: #2e2e2e;
        padding: 20px;
        margin-right: 10px;
        border-radius: 10px;
    }
    .sidebar-header {
        font-size: 24px;
        font-weight: bold;
        color: #007BFF;
        margin-bottom: 10px;
    }
    .sidebar-content {
        font-size: 16px;
        line-height: 1.6;
        color: #e5e5e5;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        max-height: 70vh;
        overflow-y: auto;
        padding: 10px;
        border-radius: 10px;
        background-color: #2e2e2e;
        margin-top: 10px;
    }
    .chat-message, .chat-response {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 70%;
        font-size: 16px;
    }
    .chat-message {
        background-color: #007BFF;
        color: white;
        align-self: flex-start;
    }
    .chat-response {
        background-color: #333;
        color: white;
        align-self: flex-end;
    }
    footer {
        visibility: visible;
        text-align: center;
        padding: 20px;
        background-color: #2e2e2e;
        color: #e5e5e5;
        border-top: 1px solid #007BFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

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

user_input = st.text_area("Enter your message here...", height=100)

# Character ID selection (optional based on your implementation)
character_id = "default_character_id"  # Replace with actual logic to get character ID

if st.button("Send"):
    if user_input:
        with st.spinner("Generating response..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"user_input": user_input, "character_id": character_id}
                )
                if response.status_code == 200:
                    response_text = response.json()["response"]
                    st.session_state['chat_history'].append(("You", user_input))
                    st.session_state['chat_history'].append(("Bot", response_text))
                else:
                    st.error("Error: " + str(response.status_code))
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message.")

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, message_text in st.session_state['chat_history']:
    if sender == "You":
        st.markdown(f'<div class="chat-message">{message_text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-response">{message_text}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <footer>
    <p>Developed by Yeabsira Dereje. Powered by Streamlit and FastAPI.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)





