#!/usr/bin/python3
""" Flask document for task 5 """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Displays a greeting """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index1():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index2(text):
    """ Displays C and then specific text from the user """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def index3(text="is cool"):
    """ Displays Python and then is cool as default """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def index4(n):
    """ Using a route parameter with a converter """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def index5(n):
    """ Displays an html file and dynamically inserts values """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def index6(n):
    """ Displays an html file and dynamically inserts values """
    if n % 2 == 0:
        type = "even"
    else:
        type = "odd"
    return render_template("6-number_odd_or_even.html", n=n, type=type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
