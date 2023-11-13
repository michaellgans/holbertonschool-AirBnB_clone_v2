#!/usr/bin/python3
""" Task 3 """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Displays string when connection is created """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index1():
    """ Displays string when connection is created """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index2(text):
    """ Displays string when connection is created """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def index3(text="is cool"):
    """ Displays string when connection is created """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
