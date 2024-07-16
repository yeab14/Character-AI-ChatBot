import streamlit as st
import auth
from app import main_app

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        # .container {
        #     width: 400px;
        #     padding: 20px;
        #     border-radius: 10px;
        #     box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        #     background-color: #222;
        #     margin-bottom: 20px;
        # }
        .title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
            color: #fff;
        }
        .input {
            margin-bottom: 15px;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #333;
            color: #fff;
            width: calc(100% - 20px);
        }
        .button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #444;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
            text-align: center;
        }
        .button:hover {
            background-color: #555;
        }
        .message.success {
            color: #4CAF50;
            margin-top: 10px;
            text-align: center;
        }
        .message.error {
            color: #FF5733;
            margin-top: 10px;
            text-align: center;
        }
        .footer {
            text-align: center;
            color: #ccc;
            font-size: 14px;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

def login_flow():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<div class="title">Welcome to Zulekya AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: center; margin-bottom: 30px;">
            Your personal AI companion here to support you with warmth, wisdom, and a touch of magic. Feel free to ask me anything – from advice to deep conversations or just to brighten your day 😊
        </p>
    """, unsafe_allow_html=True)
    username = st.text_input("Username", key="login_username", max_chars=20)
    password = st.text_input("Password", type="password", key="login_password", max_chars=20)
    st.markdown('<div style="text-align: center; margin-bottom: 10px;">', unsafe_allow_html=True)
    if st.button("Login", key="login_button"):
        if auth.login(username, password):
            st.markdown('<div class="message success">Logged in successfully!</div>', unsafe_allow_html=True)
            st.session_state.user_logged_in = True
            st.experimental_rerun()
        else:
            st.markdown('<div class="message error">Invalid username or password.</div>', unsafe_allow_html=True)
            st.markdown("""
                <p class="footer">
                    Haven't registered yet? <a href="#register_section">Click here to register</a>.
                </p>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def registration_flow():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<div class="title">Welcome to Zulekya AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: center; margin-bottom: 30px;">
            Your personal AI companion here to support you with warmth, wisdom, and a touch of magic. Feel free to ask me anything – from advice to deep conversations or just to brighten your day 😊
        </p>
    """, unsafe_allow_html=True)
    username = st.text_input("Username", key="register_username", max_chars=20)
    password = st.text_input("Password", type="password", key="register_password", max_chars=20)
    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password", max_chars=20)
    st.markdown('<div style="text-align: center; margin-bottom: 10px;">', unsafe_allow_html=True)
    if st.button("Register"):
        if password == confirm_password:
            if auth.register(username, password):
                st.markdown('<div class="message success">Registered successfully!</div>', unsafe_allow_html=True)
                st.session_state.user_logged_in = True
                st.experimental_rerun()
            else:
                st.markdown('<div class="message error">Registration failed. Username may be taken.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="message error">Passwords do not match.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Redirect to main app if user is logged in
if 'user_logged_in' not in st.session_state:
    st.session_state.user_logged_in = False

if not st.session_state.user_logged_in:
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<div class="title">Welcome to Zulekya AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
    option = st.radio("", ("Login", "Register"))
    st.markdown('</div>', unsafe_allow_html=True)
    if option == "Login":
        login_flow()
    elif option == "Register":
        st.markdown('<div id="register_section"></div>', unsafe_allow_html=True)  # Anchor for registration section
        registration_flow()
else:
    main_app()


