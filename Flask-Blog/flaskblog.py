""" Example blog using Flask"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    """ Returns respone for home page."""
    return "<h1>Hello, Universe!!</h1>"

@app.route("/about")
def about():
    """ Returns response for about page."""
    return "<h1>About page.<br>Website created by Walid.<br>Copyright (c) 2022.</h1>"


if __name__ == '__main__':
    app.run(debug=True)
