from flask import Flask
from textblob import TextBlob
from typing import cast, Protocol

app = Flask(__name__)

class _HasPolarity(Protocol):
    polarity: float

@app.route('/')
def home():
    """Return instructions for using the sentiment analysis service."""
    return app.make_response("Enter a message in the URL suffix to return its sentiment.<br>Example: http://server.port/I am feeling good")

@app.route('/<message>')
def index(message):
    """Return the sentiment of the message."""
    sentiment = 'positive'
    blob = TextBlob(message)
    polarity = cast(_HasPolarity, blob.sentiment).polarity
    if polarity < 0.1:
        sentiment = 'negative'
    return app.make_response(sentiment)

@app.route('/about')
def about():
    """Return information about the application."""
    return app.make_response("This is a simple sentiment analysis web application using Flask and TextBlob.")

@app.route('/health')
def health():
    """Return the health status of the application."""
    return app.make_response("OK")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# To run the application, use the command: python app.py
# Ensure you have Flask and TextBlob installed in your environment.

class Point3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: 'Point3D') -> float:
        """Calculate the Euclidean distance to another Point3D."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
    
    def __repr__(self) -> str:
        """Return a string representation of the Point3D."""
        return f"Point3D({self.x}, {self.y}, {self.z})"

def farewell(name: str) -> str:
    """Return a farewell message."""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    point1 = Point3D(1.0, 2.0, 3.0)
    point2 = Point3D(4.0, 5.0, 6.0)
    print(f"Distance between {point1} and {point2} is {point1.distance_to(point2)}")
    print(farewell("Alice"))


    
    


