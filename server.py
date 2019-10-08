from flask import Flask, request, jsonify
from flask_cors import CORS
import query

app = Flask(__name__)
CORS(app)


@app.route("/query1")
def query1():
    result = query.query1()
    return jsonify(result)


@app.route("/query2")
def query2():
    result = query.query2()
    return jsonify(result)


@app.route("/query3")
def query3():
    result = query.query3()
    return jsonify(result)


@app.route("/query4")
def query4():
    result = query.query3()
    return jsonify(result)


@app.route("/query5", methods=["POST"])
def query5():
    result = query.query3()
    return jsonify(result)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
