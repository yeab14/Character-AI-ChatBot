import requests
from datetime import datetime

API_URL = "http://185.124.109.231:9000" 
current_year = str(datetime.now().year)

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
