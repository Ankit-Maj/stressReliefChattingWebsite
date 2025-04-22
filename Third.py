# This version of the app removes unnecessary imports to avoid errors like:
# ModuleNotFoundError: No module named 'micropip'
# `micropip` is not used in this app, so the error was likely due to an unrelated or environmental issue.

import streamlit as st
import requests
import random

# ------------------- CONFIG -------------------
st.set_page_config(page_title="Serenity", page_icon="💌", layout="centered")

# --------------- API SETTINGS ------------------
API_URL = st.secrets["API_URL"]
API_KEY = st.secrets["API_KEY"]  # Replace this with your actual OpenRouter API key
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
    /* Affirmation card styling */
    .affirmation-card {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #8A6FD1;
    }
    .affirmation-text {
        font-size: 1.2em;
        color: #6a5acd;
        font-style: italic;
        line-height: 1.5;
    }
    /* Breathing circle animation */
    .breathing-circle {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: radial-gradient(circle, #8a6fd1, #a89cd4);
        margin: 20px auto;
        animation: breathe 19s infinite ease-in-out;
        box-shadow: 0 0 20px rgba(138, 111, 209, 0.5);
    }
    @keyframes breathe {
        0%, 100% { transform: scale(0.8); }
        25% { transform: scale(1); } /* Inhale for 4s */
        40% { transform: scale(1); } /* Hold for 7s */
        70% { transform: scale(0.8); } /* Exhale for 8s */
    }
    .breathing-text {
        text-align: center;
        margin-top: 15px;
        font-size: 1.2em;
        color: #6a5acd;
    }
    .breathing-instruction {
        text-align: center;
        margin: 5px 0;
        font-size: 1.1em;
        font-weight: bold;
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

# ------------------ FUNCTIONS ---------------------
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

def get_affirmation(mood):
    """Generate a mood-specific affirmation"""
    affirmations = {
        "Anxious": [
            "This moment of anxiety is temporary, but your strength is permanent.",
            "With each breath, I release tension and invite calm.",
            "I am safe, I am grounded, I am present.",
            "My anxiety does not define me; my courage does."
        ],
        "Stressed": [
            "I release the pressure I place on myself and choose peace instead.",
            "Stress is a response, not a requirement. I choose a different path.",
            "I am stronger than the challenges before me.",
            "My worth is not measured by productivity but by presence."
        ],
        "Overwhelmed": [
            "I tackle one thing at a time, and that is enough.",
            "I give myself permission to slow down and breathe.",
            "Progress comes one step at a time; I don't need to climb the mountain today.",
            "I am exactly where I need to be on my journey."
        ],
        "Sad": [
            "My feelings are valid, and this sadness will gently pass.",
            "I honor my emotions without being defined by them.",
            "Even in sadness, I am worthy of love and compassion.",
            "This feeling is a visitor, not a permanent resident in my heart."
        ],
        "Tired": [
            "Rest is not a luxury, but essential nourishment for my soul.",
            "I listen to my body and honor its need for restoration.",
            "In stillness, I find my strength renewed.",
            "My value isn't diminished when I pause to replenish my energy."
        ],
        "Calm": [
            "I nurture this peaceful feeling and carry it through my day.",
            "Tranquility lives within me, ready to be accessed at any moment.",
            "I am the architect of my internal weather; I choose sunshine.",
            "This calmness is my natural state; I return to it easily."
        ],
        "Happy": [
            "I am deserving of this joy and allow it to fill every part of me.",
            "Happiness is not a destination, but the way I travel through life.",
            "I cultivate and share my joy, knowing there is plenty to go around.",
            "My happiness creates ripples that touch everyone around me."
        ]
    }
    
    return random.choice(affirmations.get(mood, ["I am worthy of peace and healing."]))

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

# -------------- DAILY AFFIRMATION ---------------
affirmation = get_affirmation(mood)
st.markdown(f"""
    <div class='affirmation-card'>
        <div class='affirmation-text'>"{affirmation}"</div>
    </div>
""", unsafe_allow_html=True)

# -------------- BREATHING EXERCISE --------------
with st.expander("🫁 Breathing Exercise - 4-7-8 Technique"):
    st.markdown("""
        <div class='breathing-circle'></div>
        <div class='breathing-text'>Follow the circle's rhythm:</div>
        <div class='breathing-instruction'>Inhale through your nose for 4 seconds</div>
        <div class='breathing-instruction'>Hold your breath for 7 seconds</div>
        <div class='breathing-instruction'>Exhale completely through your mouth for 8 seconds</div>
        <div class='breathing-text'>Practice this cycle 4 times for optimal calming effect</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; margin-top: 20px; color: #666;'>
        The 4-7-8 breathing technique activates your parasympathetic nervous system, 
        helping reduce anxiety and promote better sleep.
        </p>
    """, unsafe_allow_html=True)

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
