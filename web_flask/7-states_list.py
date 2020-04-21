#!/usr/bin/python3
from flask import app, Flask, render_template

from models import storage, State

app = Flask(__name__)


@app.route('/states_list')
def state_list():
    """list of all State objects present in DBStorage"""
    states = [value for key, value in storage.all(State).items()]
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close():
    """"""
    storage.close()


if __name__ == "__main__":
    app.run
