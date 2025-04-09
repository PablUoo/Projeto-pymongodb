from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pymongo"
app.secret_key = "secret"  # Necessário para usar flash
mongo = PyMongo(app)

# Função auxiliar para converter _id para ObjectId
def to_objectid(id):
    try:
        return ObjectId(id)
    except:
        return None

# Rota principal
@app.route("/", endpoint='home')
def index():
    return render_template("index.html")

@app.route("/pessoas")
def pessoas():
    pessoas = mongo.db.pessoas.find()
    return render_template("pessoas/index.html", pessoas=pessoas)

@app.route("/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        idade = request.form.get("idade", type=int)
        
        if nome and email and idade:
            mongo.db.pessoas.insert_one({"nome": nome, "email": email, "idade": idade})
            flash("Pessoa criada com sucesso!", "success")
            return redirect(url_for("pessoas"))
        else:
            flash("Todos os campos são obrigatórios!", "error")
    
    return render_template("pessoas/criar.html")

@app.route("/editar/<pessoa_id>", methods=["GET", "POST"])
def editar(pessoa_id):
    pessoa_id = to_objectid(pessoa_id)
    if not pessoa_id:
        flash("ID inválido", "error")
        return redirect(url_for("pessoas"))

    pessoa = mongo.db.pessoas.find_one({"_id": pessoa_id})
    
    if not pessoa:
        flash("Pessoa não encontrada", "error")
        return redirect(url_for("pessoas"))

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        idade = request.form.get("idade", type=int)
        
        if nome and email and idade:
            mongo.db.pessoas.update_one(
                {"_id": pessoa_id},
                {"$set": {"nome": nome, "email": email, "idade": idade}}
            )
            flash("Pessoa editada com sucesso!", "success")
            return redirect(url_for("pessoas"))
        else:
            flash("Todos os campos são obrigatórios!", "error")
    
    return render_template("pessoas/editar.html", pessoa=pessoa)

@app.route("/deletar/<pessoa_id>")
def deletar(pessoa_id):
    pessoa_id = to_objectid(pessoa_id)
    if not pessoa_id:
        flash("ID inválido", "error")
        return redirect(url_for("pessoas"))
    
    pessoa = mongo.db.pessoas.find_one({"_id": pessoa_id})
    if pessoa:
        mongo.db.pessoas.delete_one({"_id": pessoa_id})
        flash("Pessoa deletada com sucesso!", "success")
    else:
        flash("Pessoa não encontrada", "error")
    
    return redirect(url_for("pessoas"))

if __name__ == "__main__":
    app.run(debug=True)
