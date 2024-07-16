import streamlit as st
import auth
from app import main_app

# Function to add background image from URL
def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Poppins', sans-serif; /* Stylish font */
            color: #fff; /* White text */
        }}
        @keyframes fadein {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .content {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            max-width: 600px; /* Adjust as needed */
            padding: 20px;
            animation: fadein 1s ease-in-out;
        }}
        .title {{
            margin-top: 100px;
            margin-left: -300px; /* Adjust as needed */
            font-size: 50px; /* Larger title */
            font-weight: bold;
            margin-bottom: 20px;
            text-align: left;
        }}
        .description {{
            text-align: justify; /* Justified text alignment */
            margin-left: -300px; /* Adjust as needed */
            margin-bottom: 20px;
            font-size: 25px; /* Larger text */
            font-family: 'Playfair Display', serif; /* Elegant serif font */
            color: #fff; /* White text */
            letter-spacing: 0.5px; /* Slight letter spacing */
            line-height: 1.5; /* Increased line height for readability */
            text-shadow: 1px 1px 2px rgba(0,0,0,1); /* Text shadow for depth */
            animation: fade-in 1s ease-out; /* Fade-in animation */
        }}
        .form-container {{
            width: 100%;
            margin-left: -300px;
        }}
        .input {{
            margin-bottom: 15px;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #333;
            color: #fff;
            width: calc(100% - 20px);
            font-size: 16px; /* Larger input text */
        }}
        .button {{
            margin-left: -100px;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #444;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
            text-align: center;
            font-size: 18px; /* Larger button text */
        }}
        .login-button, .register-button {{
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        background-color: #444;
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s ease;
        width: 100%;
        text-align: center;
        font-size: 18px; /* Larger button text */
    }}
    .login-button:hover, .register-button:hover {{
        background-color: #555;
    }}
        .button:hover {{
            background-color: #555;
        }}
        .message.success, .message.error {{
            margin-top: 10px;
            text-align: left;
            animation: slidein 0.5s; /* Slide in animation for messages */
        }}
        @keyframes slidein {{
            from {{ margin-top: -50px; opacity: 0; transform: translateX(-20px); }}
            to {{ margin-top: 10px; opacity: 1; transform: translateX(0); }}
        }}
        .footer {{
            text-align: left;
            color: #ccc;
            font-size: 14px;
            margin-top: 20px;
        }}
        a {{
            color: #4CAF50;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
        }}
        a:hover {{
            color: #3e8e41;
        }}
        .stRadio > div {{
            flex-direction: row;
             margin-left: -650px;
            justify-content: center;
            margin-top: -50px;
            font-size: 25px; /* Larger text */
            font-family: 'Playfair Display', serif; /* Elegant serif font */
            color: #fff; /* White text */
            letter-spacing: 0.5px; /* Slight letter spacing */
            line-height: 1.5; /* Increased line height for readability */
            text-shadow: 1px 1px 2px rgba(0,0,0,1); /* Text shadow for depth */
            animation: fade-in 1s ease-out; /* Fade-in animation */
        }}
        .stRadio > div > label {{
            display: flex;
            align-items: center;
            margin-right: 20px;
            font-size: 25px; /* Larger text */
            font-family: 'Playfair Display', serif; /* Elegant serif font */
            color: #fff; /* White text */
            letter-spacing: 0.5px; /* Slight letter spacing */
            line-height: 1.5; /* Increased line height for readability */
            text-shadow: 1px 1px 2px rgba(0,0,0,1); /* Text shadow for depth */
            animation: fade-in 1s ease-out; /* Fade-in animation */
        }}
        .stRadio > div > label:hover {{
            color: #ccc;
        }}
        .stRadio > div > label > input {{
            margin-right: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL of the background image
background_image_url = "https://img.freepik.com/premium-photo/woman-with-freckled-eye-freckled-freckles-her-face_1082211-5263.jpg?w=826"

# Inject the background image CSS into Streamlit
add_bg_from_url(background_image_url)

# Function definitions for login and registration flows
def login_flow():
    st.markdown('<div class="content" id="login_section">', unsafe_allow_html=True)
    st.markdown('<div class="title">Zulekya AI Chatbot Login</div>', unsafe_allow_html=True)
    st.markdown("""
        <p class="description">
            Welcome back to Zulekya AI Chatbot! Your personal AI companion awaits to support you with warmth, wisdom, and a touch of magic. 
            Whether you need advice, want to engage in deep conversations, or simply wish to brighten your day, Zulekya is here for you 😊.
            Sign in now to reconnect and continue your journey with Zulekya.
        </p>
    """, unsafe_allow_html=True)
    username = st.text_input("Username", key="login_username", max_chars=20, placeholder="Enter your username")
    password = st.text_input("Password", type="password", key="login_password", max_chars=20, placeholder="Enter your password")
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
    st.markdown('<div class="content" id="registration_section">', unsafe_allow_html=True)
    st.markdown('<div class="title">Register for Zulekya AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown("""
        <p class="description">
            Join Zulekya AI Chatbot today! Your personal AI companion is ready to support you with warmth, wisdom, and a touch of magic.
            Whether you need advice, want to engage in deep conversations, or simply wish to brighten your day, Zulekya is here for you 😊.
            Sign up now to start your journey with Zulekya.
        </p>
    """, unsafe_allow_html=True)
    username = st.text_input("Username", key="register_username", max_chars=20)
    password = st.text_input("Password", type="password", key="register_password", max_chars=20)
    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password", max_chars=20)
    st.markdown('<div style="text-align: center; margin-bottom: 10px;">', unsafe_allow_html=True)
    if st.button("Register", class_="register-button"):
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
    st.markdown('<div class="content">', unsafe_allow_html=True)
    st.markdown('<div class="title">Welcome to Zulekya AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown("""
        <p class="description">
            Welcome to Zulekya AI Chatbot, where every conversation sparks a new adventure! Whether you're seeking advice, engaging in deep conversations, or simply looking to brighten your day, Zulekya is your trusted companion.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
    option = st.radio("", ("Login", "Register"))
    st.markdown('</div>', unsafe_allow_html=True)
    if option == "Login":
        login_flow()
    elif option == "Register":
        st.markdown('<div id="register_section"></div>', unsafe_allow_html=True)  # Anchor for registration section
        registration_flow()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    main_app()

























