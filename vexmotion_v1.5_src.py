import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import textblob
import random

nltk.download('vader_lexicon')  # Download the VADER lexicon

# Initialize the Sentiment Intensity Analyzer
sid = SentimentIntensityAnalyzer()

def generate_sentence(sentiment):
    positive_sentences = [
        "I feel joyful and optimistic about the future.",
        "Today is a great day to be alive!",
        "I am grateful for the kindness of others."
    ]
    
    negative_sentences = [
        "I am feeling down and discouraged.",
        "The situation seems hopeless at the moment.",
        "I am frustrated with the lack of progress."
    ]
    
    if sentiment == 'positive':
        return random.choice(positive_sentences)
    elif sentiment == 'negative':
        return random.choice(negative_sentences)

print("VexmotionAI v1.5")

while True:
    text = input("Enter a sentence (type 'quit' to exit): ")
    
    if text.lower() == 'quit':
        print("Exiting the sentiment analysis program...")
        break

    if text.lower() == 'what is the type of sentence needed':
        sentiment_needed = input("Enter the sentiment needed (positive or negative): ")
        generated_sentence = generate_sentence(sentiment_needed)
        print("Generated sentence:", generated_sentence)
        continue

    # Get the sentiment score
    sentiment_score = sid.polarity_scores(text)

    # Determine the sentiment based on the score
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    sentence_type = 'Unknown'
    if text.endswith('?'):
        sentence_type = 'Interrogative'
    elif text.endswith('!'):
        sentence_type = 'Exclamatory'
    elif text.endswith('.'):
        sentence_type = 'Declarative'
    elif text.endswith('...'):
        sentence_type = 'Ellipsis'

    print('-----VexmotionAI-----')
    print('Text:', text)
    print('Sentiment:', sentiment)
    print('Sentiment Score:', sentiment_score)
    print('Sentence type:', sentence_type)
    print('---------------------')
