from unittest.mock import sentinel
from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return app.make_response("Enter a message in the URL suffix to return its sentiment.<br>Example: http://server.port/I am feeling good")

@app.route('/<message>')
def index(message):
    sentiment = 'positive'
    if TextBlob(message).sentiment.polarity < 0.0:
        sentiment = 'negative'
    return app.make_response(sentiment)

