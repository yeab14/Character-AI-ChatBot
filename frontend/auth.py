import sqlite3
import hashlib

DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    return conn

def register(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        conn.close()
        return False  # Username already exists

    # Insert new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    return True  # Registration successful

def login(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    
    # Hash the provided password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Retrieve the stored hashed password for the username
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    stored_password = c.fetchone()
    conn.close()

    if stored_password and stored_password[0] == hashed_password:
        return True  # Login successful
    else:
        return False  # Login failed
