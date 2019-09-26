#!/usr/bin/env python
from flask import Flask, render_template, request
from util import lookup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')


@app.route('/weather', methods=["GET", "POST"])
@app.route('/weather/<query>', methods=["GET", "POST"])
def weather(query=None):
    if request.method == "POST":
        query = request.form['query']
    elif query == None and request.args.get('query'):
        query = request.args.get('query')

    location, weather = lookup(query)

    return render_template('weather.html.j2', location=location, weather=weather)


if __name__ == '__main__':
    app.run(debug=True, port=5555)
