custom_css = """
<style>
/* Your custom CSS styles */
body {
    background-color: #1E1E24;
    color: #FFFFFF;
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
}

.sidebar {
    background-color: #25252D;
    padding: 20px;
    border-right: 1px solid #2E2E38;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.sidebar-header {
    font-size: 24px;
    font-weight: bold;
    color: #FFFFFF;
    margin-bottom: 20px;
}

.sidebar-content {
    font-size: 18px;
    color: #C0C0C0;
}

.profile-info {
    text-align: center;
    padding: 20px;
    margin-bottom: 20px;
}

.profile-name {
    font-size: 24px;
    font-weight: bold;
    margin-top: 10px;
}

.profile-description {
    margin-top: 10px;
    font-size: 16px;
    color: #C0C0C0;
}

.chat-container {
    padding: 20px;
    max-width: 70%;
    overflow-y: auto;
    height: calc(100vh - 180px); /* Adjust height based on sidebar and footer */
}

.chat-message {
    background-color: #007BFF;
    color: #FFFFFF;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
    max-width: 70%;
    font-size: 16px;
    display: flex;
    align-items: center;
}

.chat-response {
    background-color: #6C757D;
    color: #FFFFFF;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
    max-width: 70%;
    font-size: 16px;
    display: flex;
    align-items: center;
}

.profile-picture {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 10px;
}

.animation-text {
    animation: fadeIn 0.5s ease forwards;
}

@keyframes fadeIn {
    0% {
        opacity: 0;
        transform: translateY(10px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Send button */
.send-button {
    position: absolute;
    top: 280px;
    right: 30px;
    transform: translateY(-50%);
    background-color: #007BFF;
    color: #FFFFFF;
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
}

.send-button:hover {
    background-color: #0056b3;
}

/* Input text area */
.stTextInput textarea {
    height: 40px; /* Initial height */
    min-height: 40px;
    max-height: 120px; /* Maximum height */
    width: calc(100% - 80px); /* Adjust width */
    background-color: #2E2E38; /* Darker gray background */
    color: #FFFFFF; /* White text color */
    font-size: 16px;
    font-family: 'Arial', sans-serif;
    border: none;
    border-radius: 8px; /* Rounded corners */
    padding: 12px; /* Padding inside */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Light shadow */
    resize: none; /* Prevent resizing */
    transition: height 0.3s ease-in-out; /* Smooth height transition */
}

.stTextInput textarea::placeholder {
    color: #808080; /* Light gray placeholder text */
    font-style: italic; /* Italic placeholder */
}

/* Hover effect on textarea */
.stTextInput textarea:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Slight shadow on hover */
}

/* Focus state on textarea */
.stTextInput textarea:focus {
    outline: none; /* Remove default focus outline */
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.3); /* Blue focus border */
}
</style>
"""

# HTML and JavaScript for Send Button
send_button_html = """
<div id="send-button" class="send-button" onclick="sendMessage()">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="22" y1="2" x2="11" y2="13"></line>
        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
    </svg>
</div>
"""

send_button_js = """
<script>
function sendMessage() {
    const message = document.querySelector('.stTextInput textarea').value.trim();
    if (message !== '') {
        // Add user message to chat history
        const chatHistory = document.querySelector('.chat-container');
        const userMessage = `<div class="chat-message"><img src="https://via.placeholder.com/40" class="profile-picture" /><div class="chat-text">${message}</div></div>`;
        chatHistory.innerHTML += userMessage;

        // Scroll to bottom of chat
        chatHistory.scrollTop = chatHistory.scrollHeight;

        // Clear text area
        document.querySelector('.stTextInput textarea').value = '';

        // Simulate bot response (replace with actual API call)
        setTimeout(() => {
            const botMessage = `<div class="chat-response"><img src="data:image/png;base64,{profile_image_base64}" class="profile-picture" /><div class="chat-text">I received: ${message}</div></div>`;
            chatHistory.innerHTML += botMessage;
            chatHistory.scrollTop = chatHistory.scrollHeight;
        }, 1000);
    }
}
</script>
"""
