#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbtn():
    """"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool', strict_slashes=False):
    """"""
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """"""
    return render_template('5-number.html', n=n)


app.run()
