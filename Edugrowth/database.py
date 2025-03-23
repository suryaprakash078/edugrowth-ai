import sqlite3
import bcrypt  
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to create a database and a users table
def create_database():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Function to add a new user
def add_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        logging.info("User  added successfully.")
    except sqlite3.IntegrityError:
        logging.error("Username already exists.")
    finally:
        conn.close()

# Function to verify user credentials
def verify_user(username, password):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            logging.info("Login successful!")
            return True
        else:
            logging.warning("Invalid password.")
            return False
    else:
        logging.warning("User  not found.")
        return False
    conn.close()

# Example usage
if __name__ == "__main__":
    create_database()
    add_user('testuser', 'securepassword123')
    verify_user('testuser', 'securepassword123')