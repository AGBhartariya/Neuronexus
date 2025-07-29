from transformers import pipeline
from collections import Counter

# Load the pipeline once using PyTorch explicitly to avoid TensorFlow/Keras issues
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1,
    framework="pt"  # Explicitly use PyTorch
)

# Store emotions for analytics
emotion_log = []

def analyze_emotion(text):
    results = emotion_pipeline(text)

    # results is a list of list due to top_k=1 → [[{label, score}]]
    top_emotion = results[0][0]  # first list, first item

    label = top_emotion['label']
    confidence = round(top_emotion['score'], 2)

    # Save to log
    emotion_log.append(label)

    return {"emotion": label, "confidence": confidence}

def get_emotion_stats():
    return dict(Counter(emotion_log))

