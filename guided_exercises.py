import streamlit as st

def main():
    # ------------------- STYLES -------------------
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
        /* Exercise card styling */
        .exercise-card {
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 15px;
            padding: 25px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #8A6FD1;
        }
        .exercise-title {
            font-size: 1.8em;
            color: #6a5acd;
            margin-bottom: 15px;
        }
        .exercise-text {
            font-size: 1.1em;
            color: #444;
            margin-bottom: 15px;
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
    st.markdown("<div class='big-title'>Guided Exercises</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Mindful techniques to help you find your center</div>", unsafe_allow_html=True)
    st.markdown("---")

    # -------------- BREATHING EXERCISE --------------
    st.markdown("""
        <div class='exercise-card'>
            <div class='exercise-title'>🫁 4-7-8 Breathing Technique</div>
            <div class='exercise-text'>
                This powerful breathing exercise acts as a natural tranquilizer for your nervous system. 
                Regular practice can help reduce anxiety, manage stress, and improve sleep quality.
            </div>
            <div class='breathing-circle'></div>
            <div class='breathing-text'>Follow the circle's rhythm:</div>
            <div class='breathing-instruction'>Inhale through your nose for 4 seconds</div>
            <div class='breathing-instruction'>Hold your breath for 7 seconds</div>
            <div class='breathing-instruction'>Exhale completely through your mouth for 8 seconds</div>
            <div class='breathing-text'>Practice this cycle 4 times for optimal calming effect</div>
            <p style='text-align: center; margin-top: 20px; color: #666;'>
                The 4-7-8 breathing technique activates your parasympathetic nervous system, 
                helping reduce anxiety and promote better sleep.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # -------------- BODY SCAN EXERCISE --------------
    st.markdown("""
        <div class='exercise-card'>
            <div class='exercise-title'>🧘 Progressive Body Scan</div>
            <div class='exercise-text'>
                A body scan meditation brings awareness to each part of your body, helping release tension 
                and reconnect with physical sensations.
            </div>
            <ol style='font-size: 1.1em; color: #444; margin-left: 20px;'>
                <li>Find a comfortable position, sitting or lying down</li>
                <li>Close your eyes and bring awareness to your breath</li>
                <li>Slowly direct your attention to your feet, noticing any sensations</li>
                <li>Gradually move upward (ankles, calves, knees, etc.), spending 10-15 seconds on each area</li>
                <li>When you notice tension, breathe into that area and visualize it releasing</li>
                <li>Continue until you've scanned your entire body</li>
                <li>Take a moment to notice how your whole body feels</li>
                <li>Slowly open your eyes when you're ready</li>
            </ol>
            <p style='text-align: center; margin-top: 15px; color: #666;'>
                Try this exercise for 5-10 minutes daily for reduced stress and improved bodily awareness.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # -------------- 5-4-3-2-1 GROUNDING TECHNIQUE --------------
    st.markdown("""
        <div class='exercise-card'>
            <div class='exercise-title'>👁️ 5-4-3-2-1 Grounding Technique</div>
            <div class='exercise-text'>
                This powerful grounding exercise uses your five senses to anchor you to the present moment,
                helping with anxiety, stress, and intrusive thoughts.
            </div>
            <div style='background-color: rgba(138, 111, 209, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0;'>
                <ol style='font-size: 1.1em; color: #444; margin-left: 20px;'>
                    <li><strong>5 things you can SEE</strong> - Look around and name five things you can see in detail</li>
                    <li><strong>4 things you can TOUCH/FEEL</strong> - Notice four things you can physically feel</li>
                    <li><strong>3 things you can HEAR</strong> - Listen for three sounds around you</li>
                    <li><strong>2 things you can SMELL</strong> - Notice two scents (or recall two favorite smells)</li>
                    <li><strong>1 thing you can TASTE</strong> - Identify one taste (or imagine a favorite flavor)</li>
                </ol>
            </div>
            <p style='text-align: center; margin-top: 15px; color: #666;'>
                Practice this exercise whenever you feel overwhelmed or disconnected from your surroundings.
                Focusing on your senses helps bring you back to the present moment.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # -------------- PEACEFUL PLACE VISUALIZATION --------------
    st.markdown("""
        <div class='exercise-card'>
            <div class='exercise-title'>🌅 Peaceful Place Visualization</div>
            <div class='exercise-text'>
                Guided imagery helps create a mental sanctuary you can visit anytime to reduce stress and anxiety.
            </div>
            <div style='background-color: rgba(138, 111, 209, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0;'>
                <p style='font-size: 1.1em; color: #444; margin-bottom: 15px;'>Follow these steps:</p>
                <ol style='font-size: 1.1em; color: #444; margin-left: 20px;'>
                    <li>Find a comfortable position and close your eyes</li>
                    <li>Take several deep breaths to relax your body</li>
                    <li>Imagine a place where you feel completely peaceful and safe</li>
                    <li>Notice all the visual details of this place - colors, light, textures</li>
                    <li>What sounds can you hear in this peaceful place?</li>
                    <li>Notice any pleasant scents or fragrances</li>
                    <li>Feel the temperature, breeze or textures on your skin</li>
                    <li>Let yourself fully experience being in this place for 5-10 minutes</li>
                    <li>When ready, slowly return your awareness to the present</li>
                </ol>
            </div>
            <p style='text-align: center; margin-top: 15px; color: #666;'>
                Your peaceful place is always available to you. With practice, you'll be able to access it quickly 
                whenever you need a moment of calm.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # -------------- PROGRESSIVE MUSCLE RELAXATION --------------
    st.markdown("""
        <div class='exercise-card'>
            <div class='exercise-title'>💪 Progressive Muscle Relaxation</div>
            <div class='exercise-text'>
                This exercise involves tensing and then releasing different muscle groups to reduce physical tension 
                and promote relaxation throughout your body.
            </div>
            <div style='background-color: rgba(138, 111, 209, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0;'>
                <p style='font-size: 1.1em; color: #444; margin-bottom: 15px;'>For each muscle group:</p>
                <ol style='font-size: 1.1em; color: #444; margin-left: 20px;'>
                    <li>Tense the muscles firmly (but not painfully) for 5 seconds</li>
                    <li>Focus on the sensation of tension</li>
                    <li>Release the tension all at once</li>
                    <li>Notice how the muscles feel as they relax (15-20 seconds)</li>
                </ol>
                <p style='font-size: 1.1em; color: #444; margin: 15px 0;'>Muscle group sequence:</p>
                <ul style='font-size: 1.1em; color: #444; margin-left: 20px;'>
                    <li>Hands and forearms (make fists)</li>
                    <li>Upper arms (bend arms and "make muscles")</li>
                    <li>Shoulders (raise toward ears)</li>
                    <li>Face (scrunch up facial muscles)</li>
                    <li>Neck (gently press head back)</li>
                    <li>Chest and abdomen (tighten by inhaling deeply)</li>
                    <li>Legs (lift slightly off surface and point toes)</li>
                    <li>Feet (curl toes downward)</li>
                </ul>
            </div>
            <p style='text-align: center; margin-top: 15px; color: #666;'>
                Many people hold tension in their bodies without realizing it. This exercise helps you recognize 
                the difference between tension and relaxation, allowing you to release stress more effectively.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ------------------- FOOTER ----------------------
    st.markdown("""
        <hr style='border: 0.5px solid #ccc;'>
        <div style='text-align: center; color: gray;'>
            🌿 Practice makes progress. Be patient with yourself. 🌿
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Serenity - Guided Exercises", page_icon="🧘", layout="centered")
    main()
