import streamlit as st
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="Countdown Timer", layout="centered")

# Custom CSS for dark background and red text
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: #FF4B4B;
        }
        .countdown {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #FF4B4B;
        }
        h1 {
            color: #FF4B4B;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1>⏳ Countdown to 11 June 2025 - 11:00 PM</h1>", unsafe_allow_html=True)

# Placeholder for countdown
countdown_placeholder = st.empty()

# Target time
target_time = datetime(2025, 6, 11, 23, 0, 0)

# Use a loop with rerun via Streamlit reactivity
while True:
    now = datetime.now()
    if now >= target_time:
        countdown_placeholder.markdown("<div class='countdown'>🎉 Time has arrived! 🎉</div>", unsafe_allow_html=True)
        break

    remaining = target_time - now
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    countdown_text = f"{days}d {hours}h {minutes}m {seconds}s"
    countdown_placeholder.markdown(f"<div class='countdown'>{countdown_text}</div>", unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()
