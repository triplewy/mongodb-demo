from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/query1")
def query1():
    return "healthy"


@app.route("/query2")
def query2():
    return jsonify(data={})


@app.route("/query3")
def query3():
    return jsonify(data={})


@app.route("/query4")
def query4():
    return jsonify(data={})


@app.route("/query5", methods=["POST"])
def query5():
    return jsonify(data={})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
