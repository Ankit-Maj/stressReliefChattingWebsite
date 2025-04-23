import random

def get_affirmation(mood="random"):
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
    
    # If mood is random, choose a random mood
    if mood == "random":
        mood = random.choice(list(affirmations.keys()))
        
    return random.choice(affirmations.get(mood, ["I am worthy of peace and healing."]))
