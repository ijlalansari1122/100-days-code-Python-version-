import bcrypt
from utils.file_operations import load_data, save_data

USERS_FILE = 'data/users.json'

def signup():
    users = load_data(USERS_FILE)
    while True:
        username = input("Enter username: ").strip()
        if username in users:
            print("Username already exists. Please try a different one.")
            continue

        password = input("Enter password: ").strip()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        role = input("Enter role (admin/user): ").strip().lower()
        if role not in ['admin', 'user']:
            print("Invalid role. Please enter 'admin' or 'user'.")
            continue

        users[username] = {'password': hashed_password.decode(), 'role': role}
        save_data(USERS_FILE, users)
        print("Signup successful!")
        break

def login():
    users = load_data(USERS_FILE)
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and bcrypt.checkpw(password.encode(), users[username]['password'].encode()):
        print(f"Login successful! Welcome, {username}.")
        return users[username]['role']
    else:
        print("Invalid username or password.")
        return None
