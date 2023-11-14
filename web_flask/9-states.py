#!/usr/bin/python3
""" Task 10 """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states", strict_slashes = False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    from models.state import State

    storage.reload()
    all_states = storage.all(State)

    if id == None:
        states_list = []
        for state in all_states:
            states_list.append(all_states[state])
        return render_template("7-states_list", states=states_list)
    else:
        for state in all_states:
            if all_states[state].id == id:
                obj = all_states[state]
                return render_template("9-states.html", id=id, state=obj)
            else:
                return render_template("9-states.html", not_found=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
