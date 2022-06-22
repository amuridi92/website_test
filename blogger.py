from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

comments = []


@app.route("/", methods=["GET"])
def welcome_page():
    return render_template("blogger.html")


@app.route("/add",methods=["POST"])
def add_blog():
    data = request.get_json()
    comments.append(data)
    return jsonify("comment added!")

@app.route("/get-all", methods=["GET"])
def get_all():
    return jsonify(comments)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)