import streamlit as st
from datetime import datetime, timedelta
import time

# Set page config
st.set_page_config(page_title="Countdown to 11 June 2025", layout="centered", initial_sidebar_state="collapsed")

# Apply dark background and red text
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #FF4B4B;
        }
        .stApp {
            background-color: #121212;
        }
        .countdown {
            font-size: 48px;
            font-weight: bold;
            color: #FF4B4B;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Target datetime
target_time = datetime(2025, 6, 11, 23, 0, 0)  # 11 June 2025 11:00 PM

st.title("🕒 Countdown to 11 June 2025 - 11:00 PM")

placeholder = st.empty()

while True:
    now = datetime.now()
    if now >= target_time:
        placeholder.markdown('<div class="countdown">🎉 Time has arrived! 🎉</div>', unsafe_allow_html=True)
        break

    remaining = target_time - now
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    countdown_str = f"{days}d {hours}h {minutes}m {seconds}s"
    placeholder.markdown(f'<div class="countdown">{countdown_str}</div>', unsafe_allow_html=True)
    time.sleep(1)
