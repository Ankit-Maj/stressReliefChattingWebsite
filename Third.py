# This version of the app removes unnecessary imports to avoid errors like:
# ModuleNotFoundError: No module named 'micropip'
# `micropip` is not used in this app, so the error was likely due to an unrelated or environmental issue.

import streamlit as st
import requests

# ------------------- CONFIG -------------------
st.set_page_config(page_title="Serenity", page_icon="💌", layout="centered")

# --------------- API SETTINGS ------------------
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"  # Replace this with your actual OpenRouter API key
MODEL = "google/gemini-2.0-flash-exp:free"


# ------------------- STYLES -------------------
st.markdown("""
    <style>
    /* ✅ EDITED: Updated background styling to apply globally */
    body {
        background: linear-gradient(to bottom right, #e4d9f7, #d6e9f9) !important;
    }
    .big-title {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        color: #8A6FD1;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #A89CD4;
    }
    .stChatMessage .stMarkdown {
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ UI HEADER ------------------
st.markdown("<div class='big-title'>Serenity</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>You're not alone. Let this AI companion guide you to calmness.</div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------- SESSION SETUP ------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ FUNCTION ---------------------
def get_bot_response(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": messages
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# --------------- MOOD SELECTOR ------------------
st.sidebar.header("Your Mood")
mood = st.sidebar.selectbox("How are you feeling today?", [
    "Anxious", "Stressed", "Overwhelmed", "Sad", "Tired", "Calm", "Happy"
])

# --------------- KEYWORD SELECTOR ---------------
st.sidebar.header("Keywords")
keywords = st.sidebar.multiselect("Pick keywords to guide the chatbot:", [
    "Breathing", "Meditation", "Nature", "Support", "Encouragement", "Mindfulness", "Letting Go"
])

# ------------- CHAT INPUT + HISTORY -------------
user_input = st.chat_input("Type here to share your thoughts or feelings...")

if user_input:
    # Build contextual intro for the bot based on mood and keywords
    intro_message = f"The user is feeling {mood.lower()}. Please respond in a calming, encouraging tone. Mention these keywords if possible: {', '.join(keywords)}."

    # Insert system instruction once at the beginning
    if not any(msg["role"] == "system" for msg in st.session_state.chat_history):
        st.session_state.chat_history.insert(0, {"role": "system", "content": intro_message})

    st.session_state.chat_history.append({"role": "user", "content": user_input})
    reply = get_bot_response(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# ----------------- CHAT DISPLAY ------------------
for message in st.session_state.chat_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# ------------------- FOOTER ----------------------
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <div style='text-align: center; color: gray;'>
        🌿 Breathe in. Hold. Breathe out. You're doing great. 🌿
    </div>
""", unsafe_allow_html=True)
