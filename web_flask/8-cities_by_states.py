#!/usr/bin/python3
import os

from flask import Flask, render_template
from models import storage, City
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda x: x.name)
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def close(error):
    """"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
