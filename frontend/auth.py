import sqlite3
import hashlib

# Initialize SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table for users if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()


def register(username, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        return False  # Username already exists

    # Insert new user into the database
    c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    return True  # Registration successful


def login(username, password):
    # Hash the provided password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Retrieve the stored hashed password for the username
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    stored_password = c.fetchone()

    if stored_password and stored_password[0] == hashed_password:
        return True  # Login successful
    else:
        return False  # Login failed


# Close the database connection when done
def close_db():
    conn.close()

# Usage example:
# Register a new user
# print(register("user1", "password123"))

# Login with registered user
# print(login("user1", "password123"))

# Close the database connection
# close_db()
