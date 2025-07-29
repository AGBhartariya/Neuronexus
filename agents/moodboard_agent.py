import random

# Map emotions to visual categories
emotion_to_category = {
    "joy": "Energetic",
    "happy": "Inspiration",
    "anger": "Release",
    "sadness": "Comfort",
    "fear": "Grounding",
    "surprise": "Discovery",
    "love": "Warmth",
    "neutral": "Clarity"
}

# Keywords for each category
category_keywords = {
    "Energetic": ["sunrise", "cityscape", "mountains", "fireworks"],
    "Inspiration": ["sky", "stars", "light", "journey"],
    "Release": ["storm", "fire", "wind", "rain"],
    "Comfort": ["cozy", "blanket", "tea", "books"],
    "Grounding": ["forest", "earth", "stone", "roots"],
    "Discovery": ["galaxy", "map", "space", "explore"],
    "Warmth": ["family", "sunlight", "hug", "heart"],
    "Clarity": ["lake", "mountain", "minimal", "clear"]
}

def generate_moodboard_urls(emotion):
    category = emotion_to_category.get(emotion.lower(), "Clarity")
    keywords = category_keywords.get(category, ["nature"])
    random.shuffle(keywords)

    urls = [f"https://source.unsplash.com/400x300/?{kw}" for kw in keywords[:4]]

    return {
        "category": category,
        "urls": urls
    }
