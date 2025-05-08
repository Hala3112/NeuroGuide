import streamlit as st
import os
import json
import hashlib

USER_DATA_PATH = "user_data.json"

# Helper to hash passwords using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load user data
def load_user_data():
    if os.path.exists(USER_DATA_PATH):
        with open(USER_DATA_PATH, "r") as file:
            return json.load(file)
    return {}

# Save user data
def save_user_data(user_data):
    with open(USER_DATA_PATH, "w") as file:
        json.dump(user_data, file)

# Load existing data
user_data = load_user_data()

# Session state setup
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

st.title("🔐 Login / Sign Up")
option = st.radio("Choose an option", ["Sign Up", "Log In"])

if option == "Sign Up":
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):
        if not username or not password:
            st.error("Username and password cannot be empty.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif username in user_data:
            st.warning("Username already exists. Please choose a different one.")
        else:
            hashed_pw = hash_password(password)
            user_data[username] = hashed_pw
            save_user_data(user_data)
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Account created and logged in!")
            st.rerun()

elif option == "Log In":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        hashed_pw = hash_password(password)
        if username in user_data and user_data[username] == hashed_pw:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success(f"✅ Welcome back, {username}!")
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")
