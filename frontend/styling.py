import streamlit as st

def apply_custom_css():
    st.markdown(
        """
        <style>
            /* General styling */
            body {
                background-color: #121212;
                color: #ffffff;
                font-family: 'Arial', sans-serif;
            }
            .css-1lcbmhc {
                background-color: #121212;
            }

            /* Sidebar styling */
            .sidebar .sidebar-header {
                font-size: 1.5rem;
                color: #d7a022;
                text-align: center;
                margin-bottom: 10px;
            }
            .sidebar .sidebar-content {
                font-size: 1rem;
                color: #ffffff;
                text-align: center;
            }

            /* Profile styling */
            .profile-info {
                text-align: center;
                margin-bottom: 30px;
            }
            .profile-picture {
                width: 130px;
                height: 130px;
                border-radius: 50%;
                margin-bottom: 5px;
                border: 5px solid #ffffff;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
            .profile-name {
                font-size: 1.5rem;
                color: #d7a022;
                margin-bottom: 5px;
            }
            .profile-description {
                font-size: 1rem;
                color: #ffffff;
                margin-bottom: 5px;
            }
            .chat-message, .chat-response {
                display: flex;
                align-items: center;
                margin-bottom: 10px;
            }
            .chat-message .profile-picture, .chat-response .profile-picture {
                width: 40px;
                height: 40px;
                border-radius: 50%;
                margin-right: 10px;
            }
            .chat-message .chat-text, .chat-response .chat-text {
                background-color: #282828;
                padding: 10px;
                border-radius: 10px;
                font-size: 1rem;
                color: #ffffff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }

            /* Sidebar button styling */
            .css-1n76uvr, .css-1n76uvr:focus, .css-1n76uvr:hover, .css-1n76uvr:active {
                color: #ffffff;
                background-color: #d7a022;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-size: 1rem;
                margin-bottom: 10px;
                cursor: pointer;
                transition: background-color 0.3s ease, transform 0.2s;
                text-align: center;
                display: inline-block;
                width: 100%;
            }
            .css-1n76uvr:hover {
                background-color: #c69a1e;
                transform: translateY(-2px);
            }
            .css-1n76uvr:active {
                background-color: #b5891b;
                transform: translateY(0);
            }

            /* Footer styling */
            footer {
                text-align: center;
                margin-top: 20px;
                font-size: 0.9rem;
                color: #ffffff;
            }

            /* Animation for text */
            .animation-text {
                animation: fadeIn 2s ease-in-out;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


