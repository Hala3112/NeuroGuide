import openai
import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="NeuroGuide Assistant")
st.title("🧠 NeuroGuide - AI Doctor for Mobility Support")

# Load OpenAI API key securely
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Doctor system prompt
doctor_prompt = """
You are a compassionate and professional doctor helping individuals with mobility impairments.
Your responses should always be calming, supportive, and kind, with a focus on patient care.
When answering, imagine you are speaking to someone who is going through a challenging time and 
needs encouragement and practical advice.
"""

# Initialize the model (default)
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Inject the system prompt once at the start
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({"role": "system", "content": doctor_prompt})

# Show chat history
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# User input
user_input = st.chat_input("How can I help you today?")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Prepare assistant response
    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        full_reply = ""

        try:
            for chunk in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=st.session_state.messages,
                stream=True,
            ):
                full_reply += chunk.choices[0].delta.get("content", "")
                msg_placeholder.markdown(full_reply + "▌")
        except Exception as e:
            msg_placeholder.markdown("⚠️ Error from OpenAI API.")
            st.error(f"{e}")
            full_reply = "Sorry, something went wrong."

        msg_placeholder.markdown(full_reply)
        st.session_state.messages.append({"role": "assistant", "content": full_reply})
