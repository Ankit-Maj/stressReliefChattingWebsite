import streamlit as st
import streamlit_app  # Import the AI Therapist module
import guided_exercises  # Import the Guided Exercises module
import journal  # Import the journal module
import affirmations  # Import the affirmations module
from urllib.parse import parse_qs
import streamlit.components.v1 as components

# Set up page configuration
st.set_page_config(page_title="Serenity - Mental Wellness", page_icon="🌿", layout="wide")

# Check query parameters to determine which page to show
page = st.query_params.get("page", "home")

# Display the selected page
if page == "therapist":
    # Run the AI Therapist module
    streamlit_app.main()
elif page == "exercises":
    # Run the Guided Exercises module
    guided_exercises.main()
elif page == "journal":
    # Run the Journal module
    journal.main()
elif page == "game":
    # Relaxing game page
    st.markdown("""
        <style>
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
    
    # Navigation
    st.markdown("""
        <a href="?page=home" target="_self" class="nav-button">← Back to Home</a>
    """, unsafe_allow_html=True)
    
    # Game header
    st.markdown("<div class='big-title'>Count Masters</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A fun stickman game to help take your mind off stress</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Embedded game - modify to a more sensible size
    stickman_games_html = """
    <div style="width: 100%; height: 600px; overflow: hidden; position: relative;">
        <iframe src="https://www.crazygames.com/embed/count-masters-stickman-games" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                allow="gamepad *;" scrolling="no">
        </iframe>
    </div>
    """
    components.html(stickman_games_html, height=600)
    
    # Footer
    st.markdown("""
        <hr style='border: 0.5px solid #ccc; margin-top: 30px;'>
        <div style='text-align: center; color: gray;'>
            🌿 Games can be a wonderful way to relax and reset your mind 🌿
        </div>
    """, unsafe_allow_html=True)
    
else:
    # Home page content
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
    
    # ------------------- DAILY AFFIRMATION -------------------
    daily_affirmation = affirmations.get_affirmation("random")
    st.markdown(f"""
        <div style='background-color: rgba(255, 255, 255, 0.7); border-radius: 15px; padding: 20px; 
                margin: 20px auto 30px auto; max-width: 800px; text-align: center; 
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-left: 5px solid #8A6FD1;'>
            <div style='font-size: 1.1em; color: #A89CD4; margin-bottom: 10px;'>Today's Affirmation</div>
            <div style='font-size: 1.4em; color: #6a5acd; font-style: italic; line-height: 1.5;'>
                "{daily_affirmation}"
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ------------------- MAIN CONTENT -------------------
    st.markdown("## How Serenity Helps You")

    feature_col1, feature_col2 = st.columns(2)

    with feature_col1:
        # AI Therapist card with link to streamlit_app.py
        st.markdown("""
            <div class='feature-card'>
                <div class='feature-title'>🤖 AI Therapist</div>
                <div class='feature-text'>
                    Connect with our empathetic AI companion designed to provide supportive conversations tailored to your mood.
                    Share your thoughts in a judgment-free space and receive personalized guidance.
                </div>
                <div style='text-align: center; margin-top: 15px;'>
                    <a href="?page=therapist" target="_self">
                        <button class='cta-button' style='font-size: 1em; padding: 8px 20px;'>Try AI Therapist</button>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Guided Exercises card with link to guided_exercises.py
        st.markdown("""
            <div class='feature-card'>
                <div class='feature-title'>🧘 Guided Exercises</div>
                <div class='feature-text'>
                    Access scientifically-backed breathing techniques and mindfulness exercises that help reduce anxiety and stress.
                    Just a few minutes can transform your mental state.
                </div>
                <div style='text-align: center; margin-top: 15px;'>
                    <a href="?page=exercises" target="_self">
                        <button class='cta-button' style='font-size: 1em; padding: 8px 20px;'>Try Guided Exercises</button>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with feature_col2:
        # Replace Daily Affirmations card with Game card
        st.markdown("""
            <div class='feature-card'>
                <div class='feature-title'>🎮 Relaxing Game</div>
                <div class='feature-text'>
                    Take a break and enjoy a moment of peace with our soothing interactive experience.
                    A few minutes of play can help clear your mind and restore your focus.
                </div>
                <div style='text-align: center; margin-top: 15px;'>
                    <a href="?page=game" target="_self">
                        <button class='cta-button' style='font-size: 1em; padding: 8px 20px;'>Play Now</button>
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Replace Relaxing Sounds card with Journal card
        st.markdown("""
            <div class='feature-card'>
                <div class='feature-title'>📔 Personal Journal</div>
                <div class='feature-text'>
                    Document your thoughts, feelings, and experiences in a private digital journal.
                    Track your emotional journey and reflect on your growth over time.
                </div>
                <div style='text-align: center; margin-top: 15px;'>
                    <a href="?page=journal" target="_self">
                        <button class='cta-button' style='font-size: 1em; padding: 8px 20px;'>Open Journal</button>
                    </a>
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