#!/usr/bin/python3
""" Task 10 """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.debug = False

@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states", strict_slashes = False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    from models.state import State

    storage.reload()
    all_states = storage.all(State)

    if id is None:
        states_list = list(all_states.values())
        return render_template("7-states_list.html", states=states_list)
    else:
        for state in all_states.values():
            if state.id == id:
                return render_template("9-states.html", state=state)

        return render_template("9-states.html", not_found=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
