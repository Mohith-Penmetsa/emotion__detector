"""
Unit tests for emotion detection.
"""

from EmotionDetection import emotion_detector

def test_emotions():
    tests = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected in tests.items():
        result = emotion_detector(text)
        assert result["dominant_emotion"] == expected
