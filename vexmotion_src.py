import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the VADER lexicon

# Initialize the Sentiment Intensity Analyzer
sid = SentimentIntensityAnalyzer()

while True:
    text = input("VexmotionAI")
    text = input("Enter a sentence (type 'quit' to exit): ")
    
    if text.lower() == 'quit':
        print("Exiting the sentiment analysis program...")
        break

    # Get the sentiment score
    sentiment_score = sid.polarity_scores(text)

    # Determine the sentiment based on the score
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    print('VexmotionAI')
    print(f'Text: {text}')
    print(f'Sentiment: {sentiment}')
    print(f'Sentiment Score: {sentiment_score}')
