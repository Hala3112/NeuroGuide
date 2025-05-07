import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("📊 Real-Time BioSignal Dashboard")

if not st.session_state.get("authenticated"):
    st.warning("Login to view signals.")
    st.stop()

placeholder = st.empty()
for _ in range(100):
    t = np.linspace(0, 2, 256)
    eeg = np.sin(2 * np.pi * (10 + np.random.rand()) * t) + 0.3 * np.random.randn(len(t))
    heart_rate = np.random.randint(65, 100)
    breathing = np.random.randint(12, 20)
    stress = np.random.rand()
    status = "Good" if stress < 0.6 else "Moderate" if stress < 0.8 else "Stressed"

    with placeholder.container():
        st.subheader("🧠 Brainwave Signal")
        st.line_chart(pd.DataFrame({"Time": t, "EEG": eeg}).set_index("Time"))
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("❤️ Heart Rate", f"{heart_rate} bpm")
        c2.metric("💨 Breathing", f"{breathing} rpm")
        c3.metric("😬 Stress", f"{stress:.2f}")
        c4.metric("🧑‍⚕️ Health", status)
        st.info("⏳ Streaming simulated data...")

    time.sleep(0.1)
