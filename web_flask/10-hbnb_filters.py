#!/usr/bin/python3
""" Task 11 """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.debug = False


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    from models.state import State
    from models.amenity import Amenity

    storage.reload()
    all_states = storage.all(States)
    all_amenities = storage.all(Amenity)
    states_list = list(all_states.value())
    amenities_list = list(all_amenities.value())

    return render_template("10-hbnb_filters.html",
                           states=states_list,
                           amenities=amenities_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
