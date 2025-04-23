import streamlit as st
import requests
import random
import affirmations  # Import the affirmations module

def main():
    # --------------- API SETTINGS ------------------
    API_URL = st.secrets["API_URL"]
    API_KEY = st.secrets["API_KEY"]
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
             0% { transform: scale(0.8); }
            21.05% { transform: scale(1); } /* Inhale for 4s (4/19 = 21.05%) */
            57.89% { transform: scale(1); } /* Hold for 7s (7/19 = 36.84%) */
            100% { transform: scale(0.8); } /* Exhale for 8s (8/19 = 42.11%) */
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
        /* Navigation button */
        .nav-button {
            display: inline-block;
            padding: 5px 15px;
            background-color: #8A6FD1;
            color: white;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.9em;
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        .nav-button:hover {
            background-color: #7860c1;
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)

    # ------------------ NAVIGATION -----------------
    st.markdown("""
        <a href="?page=home" target="_self" class="nav-button">← Back to Home</a>
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
    affirmation = affirmations.get_affirmation(mood)
    st.markdown(f"""
        <div class='affirmation-card'>
            <div class='affirmation-text'>"{affirmation}"</div>
        </div>
    """, unsafe_allow_html=True)

    # Remove the breathing exercise section and add a link to guided exercises instead
    st.markdown("""
        <div style='text-align: center; margin: 20px 0;'>
            <p style='color: #6a5acd; margin-bottom: 10px;'>Need help relaxing?</p>
            <a href="?page=exercises" target="_self" class="nav-button">
                Try our Guided Exercises →
            </a>
        </div>
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

# This allows the file to be run independently or imported as a module
if __name__ == "__main__":
    st.set_page_config(page_title="Serenity - AI Therapist", page_icon="💌", layout="centered")
    main()
