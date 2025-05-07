import streamlit as st
import os
import json

USER_DATA_PATH = "user_data.json"

def load_user_data():
    if os.path.exists(USER_DATA_PATH):
        with open(USER_DATA_PATH, "r") as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    with open(USER_DATA_PATH, "w") as file:
        json.dump(user_data, file)

st.title("🔐 Login / Sign Up")

user_data = load_user_data()
option = st.radio("Choose an option", ["Sign Up", "Log In"])

if option == "Sign Up":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Create Account"):
        if username and password and password == confirm_password:
            if username not in user_data:
                user_data[username] = password
                save_user_data(user_data)
                st.session_state.authenticated = True
                st.success("Account created successfully!")
                st.rerun()
            else:
                st.warning("Username already exists.")
        else:
            st.error("Check your inputs.")

elif option == "Log In":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        if user_data.get(username) == password:
            st.session_state.authenticated = True
            st.success(f"Welcome back, {username}!")
            st.rerun()
        else:
            st.error("Invalid credentials.")
