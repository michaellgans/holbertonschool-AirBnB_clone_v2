#!/usr/bin/python3
"""
Flask document for task 4
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Displays a greeting.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index1():
    """
    Displays HBNB.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index2(text):
    """
    Displays C and then specific text from the user.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def index3(text="is cool"):
    """
    Displays Python and then is cool as default
    This is a test
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def index3(n):
    """
    Using a route parameter with a converter
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
