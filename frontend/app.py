import streamlit as st
import requests

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput textarea {
        background-color: #1e1e1e;
        color: white;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .sidebar {
        background-color: #f0f0f0;
        padding: 20px;
        margin-right: 10px;
        border-radius: 10px;
    }
    .sidebar-header {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sidebar-content {
        font-size: 16px;
        line-height: 1.6;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .chat-message {
        background-color: #007BFF;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        align-self: flex-start;
        max-width: 70%;
    }
    .chat-response {
        background-color: #333;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        align-self: flex-end;
        max-width: 70%;
    }
    footer {
        visibility: visible;
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
        <div class="sidebar-header">ChatGPT</div>
        <div class="sidebar-content">
            Chat with an AI-powered character.<br><br>
            Enter your messages in the field on the left.<br>
            The AI will respond on the right.<br><br>
            Powered by Streamlit and FastAPI.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main content
st.title("Roleplay Chatbot")

user_input = st.text_area("Enter your message here...")

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



