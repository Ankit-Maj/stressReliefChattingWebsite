import streamlit as st

# ------------------- CONFIG -------------------
st.set_page_config(page_title="Serenity - Mental Wellness", page_icon="🌿", layout="wide")

# ------------------- STYLES -------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #e4d9f7, #d6e9f9) !important;
    }
    .main-title {
        font-size: 3.5em;
        font-weight: bold;
        text-align: center;
        color: #8A6FD1;
        margin-bottom: 0.2em;
    }
    .tagline {
        text-align: center;
        font-size: 1.5em;
        color: #A89CD4;
        margin-bottom: 2em;
    }
    .feature-card {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #8A6FD1;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .feature-title {
        font-size: 1.8em;
        color: #6a5acd;
        margin-bottom: 10px;
    }
    .feature-text {
        font-size: 1.1em;
        color: #444;
    }
    .cta-button {
        background-color: #8A6FD1;
        color: white;
        padding: 12px 30px;
        font-size: 1.2em;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        display: inline-block;
        margin: 20px 0;
        text-align: center;
        text-decoration: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .cta-button:hover {
        background-color: #7860c1;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- HEADER -------------------
st.markdown("<div class='main-title'>Serenity</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your digital sanctuary for mental wellness</div>", unsafe_allow_html=True)

# ------------------- NAVIGATION -------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div style='text-align: center'>
            <a href='/Third' target='_self'>
                <button class='cta-button'>Try AI Therapist</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

# ------------------- MAIN CONTENT -------------------
st.markdown("## How Serenity Helps You")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.markdown("""
        <div class='feature-card'>
            <div class='feature-title'>🤖 AI Therapist</div>
            <div class='feature-text'>
                Connect with our empathetic AI companion designed to provide supportive conversations tailored to your mood.
                Share your thoughts in a judgment-free space and receive personalized guidance.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='feature-card'>
            <div class='feature-title'>🧘 Guided Exercises</div>
            <div class='feature-text'>
                Access scientifically-backed breathing techniques and mindfulness exercises that help reduce anxiety and stress.
                Just a few minutes can transform your mental state.
            </div>
        </div>
    """, unsafe_allow_html=True)

with feature_col2:
    st.markdown("""
        <div class='feature-card'>
            <div class='feature-title'>💝 Daily Affirmations</div>
            <div class='feature-text'>
                Start each day with positive affirmations tailored to your emotional state.
                These gentle reminders help rewire negative thought patterns and build resilience.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='feature-card'>
            <div class='feature-title'>🌈 Mood Tracking</div>
            <div class='feature-text'>
                Monitor your emotional well-being over time with our simple mood tracking feature.
                Identify patterns and triggers to better understand your mental health journey.
            </div>
        </div>
    """, unsafe_allow_html=True)

# ------------------- TESTIMONIALS -------------------
st.markdown("## What Users Say")
testimonial_cols = st.columns(3)

testimonials = [
    {"quote": "Serenity has been my daily companion through anxiety. The breathing exercises alone have changed my life.", "author": "Jamie, 28"},
    {"quote": "The AI therapist feels surprisingly empathetic. It's there for me at 3 AM when I need someone to talk to.", "author": "Alex, 34"},
    {"quote": "I start each morning with a new affirmation. These small moments of positivity add up over time.", "author": "Sam, 41"}
]

for i, col in enumerate(testimonial_cols):
    with col:
        st.markdown(f"""
            <div style='background-color: rgba(255, 255, 255, 0.7); border-radius: 15px; padding: 20px; text-align: center;'>
                <div style='font-style: italic; font-size: 1.1em; color: #555;'>"{testimonials[i]['quote']}"</div>
                <div style='margin-top: 10px; color: #8A6FD1; font-weight: bold;'>{testimonials[i]['author']}</div>
            </div>
        """, unsafe_allow_html=True)

# ------------------- FOOTER -------------------
st.markdown("""
    <hr style='margin-top: 50px; border: 0.5px solid #ccc;'>
    <div style='text-align: center; color: gray; padding: 20px;'>
        🌿 Serenity - Your companion for mental wellness 🌿<br>
        <span style='font-size: 0.8em;'>© 2023 Serenity. All rights reserved.</span>
    </div>
""", unsafe_allow_html=True)
