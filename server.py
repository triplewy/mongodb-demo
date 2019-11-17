"""
(This is a file-level docstring.)
This file contains code for Flask server that handles API requests
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import query

app = Flask(__name__)
CORS(app)


@app.route("/query1")
def query1():
    minFare = int(request.args.get('minFare'))
    maxFare = int(request.args.get('maxFare'))

    result = query.query1(minFare, maxFare)
    return jsonify(result)


@app.route("/query2")
def query2():
    search = request.args.get('search')
    minReviews = int(request.args.get('minReviews'))

    result = query.query2(search, minReviews)
    return jsonify(result)


@app.route("/query3")
def query3():
    result = query.query3()
    return jsonify(result)


@app.route("/query4")
def query4():
    result = query.query4()
    return jsonify(result)


@app.route("/query5")
def query5():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    result = query.query5(latitude, longitude)
    return jsonify(result)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
