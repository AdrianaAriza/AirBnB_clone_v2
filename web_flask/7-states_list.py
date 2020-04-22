#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """"""
    states = [value for key, value in storage.all(State).items()]
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
