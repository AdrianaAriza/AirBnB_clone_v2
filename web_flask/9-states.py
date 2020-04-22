#!/usr/bin/python3
import os

from flask import Flask, render_template
from models import storage, City
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_id(id=None):
    """"""
    f = 0
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    if id:
        f = 1
        for state in states:
            if id == state.id:
                print('True')
                cities = storage.all(City).values()
                cities = sorted(cities, key=lambda x: x.name)
                return render_template('9-states.html',
                                       states=state, cities=cities, f=f)
    if f:
        f = 2
        return render_template('9-states.html', f=f)

    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close(error):
    """"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
