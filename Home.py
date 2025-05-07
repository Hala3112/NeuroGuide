import streamlit as st

st.set_page_config(page_title="NeuroWheels", layout="wide")
st.title("🧠 NeuroWheels")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    st.sidebar.success("You are logged in. Use the sidebar to navigate.")
else:
    st.sidebar.warning("Please log in to access full features.")
    st.switch_page("pages/1_Authentication.py")
