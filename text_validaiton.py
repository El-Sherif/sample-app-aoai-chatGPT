import re
#from textblob import TextBlob


def harmful_filter(text):
    banned_words = ["sex", "kill someone"]  # Replace with actual words
    pattern = re.compile(r'\b(' + '|'.join(banned_words) + r')\b', re.IGNORECASE)
    if pattern.search(text):
        return True
    return False

def mental_health_filter(text):
    banned_words = ["suicide", "kill myself"]  # Replace with actual words
    pattern = re.compile(r'\b(' + '|'.join(banned_words) + r')\b', re.IGNORECASE)
    if pattern.search(text):
        return True
    return False

#def analyze_sentiment(text):
#    blob = TextBlob(text)
#    sentiment = blob.sentiment.polarity  # -1 to 1 where -1 is negative and 1 is positive
#    return "Negative" if sentiment < -0.5 else "Positive" if sentiment > 0.5 else "Neutral"

#def sentiment_check(text):
#    return analyze_sentiment(text) == 'Neutral'

#filtered_response = profanity_filter(response)
#sentiment = sentiment_check(response)