from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import sys
import argparse

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
CORS(app)


@app.route("/health")
def health():
    return "healthy"


# @app.route("/labels")
# def labels():
#     return jsonify(data=kerasInfer.labels)


# @app.route("/clusters")
# def clusters():
#     results = query("SELECT clusterId, title FROM clusters;", ())
#     return jsonify(data=results)


# @app.route("/titles")
# def titles():
#     results = query(
#         "SELECT titleId, title, clusterId FROM titles WHERE clusterId IS NOT NULL;", ())
#     return jsonify(data=results)


# @app.route("/predict", methods=["POST"])
# def predict():
#     imgId = uuid.uuid1().hex
#     file = request.files['file']
#     if file and allowed_file(file.filename):
#         path = os.path.join(
#             app.config['UPLOAD_FOLDER'], "{}.jpg".format(imgId))
#         file.save(path)
#         results1 = tagInfer.predict(path)
#         results2 = kerasInfer.predict(path)
#         results = results1 + results2
#         results = sorted(results, key=lambda x: x[1], reverse=True)
#         return jsonify(data=results[:5], id=imgId)
#     else:
#         raise TypeError('Error')


# @app.route("/label", methods=["POST"])
# def label():
#     body = request.get_json()
#     img_id = body["imgId"]
#     title_id = body["titleId"]
#     upload(img_id, title_id)
#     return jsonify(message="success")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
