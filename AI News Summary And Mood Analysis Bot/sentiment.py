from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def classify_mood(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05: return "Positive", score
    elif score <= -0.05: return "Negative", score
    return "Neutral", score

def mood_icon(mood):
    return {"Positive":"😊","Neutral":"😐","Negative":"😞"}.get(mood,"😐")
