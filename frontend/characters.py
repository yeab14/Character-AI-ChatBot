import streamlit as st

# Function to display characters
def display_characters():
    # Hardcoded characters
    characters = [
        {
            'id': 'zulekya',
            'name': 'Zulekya',
            'description': 'Your AI companion Zulekya, here to support you with warmth, wisdom, and a touch of magic.',
            'image': 'profile.png'  # Local path to the Zulekya image
        },
        {
            'id': 'add_new',
            'name': 'Add New Character',
            'description': 'Create your own unique AI character to interact with.',
            'image': 'add_icon.png'  # Local path to the + icon image
        }
    ]
    
    if characters:
        for character in characters:
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(character['image'], width=80)
                with col2:
                    st.markdown(f"### {character['name']}")
                    st.markdown(f"_{character['description']}_")
                    if st.button("Select", key=character['id']):
                        if character['id'] != 'add_new':
                            st.session_state['selected_character'] = character['id']
                            st.experimental_rerun()
                        else:
                            st.write("Add new character functionality not implemented yet.")

# Main function
def main():
    st.title("Select Your Character")
    
    # Display characters in a stylish way
    display_characters()
    
    # Check if a character is selected
    if 'selected_character' in st.session_state:
        st.session_state['chat_character'] = st.session_state['selected_character']
        st.write(f"Character {st.session_state['chat_character']} selected! Redirecting...")
        st.experimental_rerun()

if __name__ == "__main__":
    main()

