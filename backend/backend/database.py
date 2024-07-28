# database.py

import sqlite3
import hashlib
import os

# Initialize SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table for users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL,
        salt TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
