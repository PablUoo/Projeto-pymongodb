from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson import ObjectId
from routes.pessoas import init_pessoas_routes

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pymongo"
app.secret_key = "secret"
mongo = PyMongo(app)

def to_objectid(id):
    try:
        return ObjectId(id)
    except Exception:
        return None

# Rota principal
@app.route("/", endpoint='home')
def index():
    return render_template("index.html")

init_pessoas_routes(app, mongo, to_objectid)

if __name__ == "__main__":
    app.run(debug=True)
