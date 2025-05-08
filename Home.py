import streamlit as st

# Page setup
st.set_page_config(page_title="NeuroWheels", layout="wide")

# Title and Header
st.markdown("<h1 style='text-align: center;'>🧠 NeuroWheels</h1>", unsafe_allow_html=True)
st.markdown("## Empowering Mobility, Restoring Independence", unsafe_allow_html=True)

# Project Description
with st.container():
    st.markdown("""
    <div style='padding: 1.5rem; background-color: #f0f2f6; border-radius: 10px;'>
        <p style='font-size: 18px;'>
        <strong>NeuroWheels</strong> is an AI-powered mobility innovation designed to restore freedom and self-reliance 
        for individuals with physical disabilities—whether due to paralysis, limb loss, or neuromuscular disorders. 
        By combining advanced machine learning with user-centric design, our system provides real-time feedback, 
        motivation, and caregiver support.<br><br>
        <strong>Implementation Date:</strong> May 2025
        </p>
    </div>
    """, unsafe_allow_html=True)

# Team Info
with st.expander("👥 Meet the Team"):
    st.markdown("""
    - **Hala Farfoura**  
    - **Mariam Kandari**  
    - **Rawan Saleem**  
    - **Shahad Alabwah**  
    - **Fajer Almanaye**  

    A dedicated team of innovators from diverse backgrounds, working together to build smarter, more compassionate technology.
    """)

# Login Check
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if st.session_state.authenticated:
    st.sidebar.success("✅ You are logged in. Use the sidebar to navigate.")
else:
    st.sidebar.warning("⚠️ Please log in to access full features.")
    st.switch_page("pages/1_Authentication.py")
