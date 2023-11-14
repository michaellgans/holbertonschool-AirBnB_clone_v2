#!/usr/bin/python3
""" Task 8 """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    from models.state import State

    storage.reload()
    all_states = storage.all(State)

    states_list = []

    for state in all_states:
        states_list.append(all_states[state])
    return render_template("7-states_list.html", states=states_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
