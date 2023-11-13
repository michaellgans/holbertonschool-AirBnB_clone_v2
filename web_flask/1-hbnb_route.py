#!/usr/bin/python3
""" Task 0 """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Displays string when connection is created """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index2():
    """ Displays string when connection is created """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)