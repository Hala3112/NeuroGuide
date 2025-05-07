import streamlit as st

st.title("💳 Upgrade to Premium & Add-ons")

if not st.session_state.get("authenticated"):
    st.warning("Login to manage upgrades.")
    st.stop()

upgrade = st.checkbox("Upgrade to Premium (5 KD)")
buy_arm = st.checkbox("Add Robotic Arm (45 KD)")
buy_tablet = st.checkbox("Add Built-in Tablet (30 KD)")

total = sum([
    5 if upgrade else 0,
    45 if buy_arm else 0,
    30 if buy_tablet else 0
])

st.divider()
st.subheader("🧾 Order Summary")
if total == 0:
    st.info("No upgrades selected.")
else:
    st.success(f"Total: {total} KD")
    if st.button("Proceed to Payment"):
        st.balloons()
        st.success("Payment processed successfully!")
