from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson import ObjectId

# Importa as rotas
from routes.pessoas import init_pessoas_routes
from routes.enderecos import init_enderecos_routes
from routes.filhos import init_filhos_routes

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pymongo"
app.secret_key = "secret"
mongo = PyMongo(app)

# Função auxiliar para converter ID
def to_objectid(id):
    try:
        return ObjectId(id)
    except Exception:
        return None

# Rota principal
@app.route("/", endpoint='home')
def index():
    return render_template("index.html")

# Inicializa as rotas
init_pessoas_routes(app, mongo, to_objectid)
init_enderecos_routes(app, mongo, to_objectid)
init_filhos_routes(app, mongo, to_objectid)

if __name__ == "__main__":
    app.run(debug=True)
