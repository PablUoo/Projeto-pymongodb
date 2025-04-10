from flask import render_template, request, redirect, url_for, flash
from bson import ObjectId

def init_enderecos_routes(app, mongo, to_objectid):
    @app.route("/pessoa/<pessoa_id>/enderecos")
    def listar_enderecos(pessoa_id):
        pessoa_oid = to_objectid(pessoa_id)
        if not pessoa_oid:
            flash("ID de pessoa inválido!", "error")
            return redirect(url_for("pessoas"))

        enderecos = mongo.db.enderecos.find({"pessoa_id": pessoa_oid})
        return render_template("enderecos/index.html", enderecos=enderecos, pessoa_id=pessoa_id)

    @app.route("/pessoa/<pessoa_id>/enderecos/criar", methods=["GET", "POST"])
    def criar_endereco(pessoa_id):
        pessoa_oid = to_objectid(pessoa_id)
        if not pessoa_oid:
            flash("ID de pessoa inválido!", "error")
            return redirect(url_for("pessoas"))

        if request.method == "POST":
            rua = request.form["rua"]
            numero = request.form["numero"]
            cidade = request.form["cidade"]

            mongo.db.enderecos.insert_one({
                "pessoa_id": pessoa_oid,
                "rua": rua,
                "numero": numero,
                "cidade": cidade
            })

            flash("Endereço adicionado!", "success")
            return redirect(url_for("listar_enderecos", pessoa_id=pessoa_id))

        return render_template("enderecos/criar.html", pessoa_id=pessoa_id)

    @app.route("/enderecos/editar/<endereco_id>", methods=["GET", "POST"])
    def editar_endereco(endereco_id):
        endereco_oid = to_objectid(endereco_id)
        if not endereco_oid:
            flash("ID do endereço inválido!", "error")
            return redirect(url_for("pessoas"))

        endereco = mongo.db.enderecos.find_one({"_id": endereco_oid})
        if not endereco:
            flash("Endereço não encontrado!", "error")
            return redirect(url_for("pessoas"))

        if request.method == "POST":
            rua = request.form["rua"]
            numero = request.form["numero"]
            cidade = request.form["cidade"]

            mongo.db.enderecos.update_one(
                {"_id": endereco_oid},
                {"$set": {
                    "rua": rua,
                    "numero": numero,
                    "cidade": cidade
                }}
            )

            flash("Endereço atualizado!", "success")
            return redirect(url_for("listar_enderecos", pessoa_id=str(endereco["pessoa_id"])))

        return render_template("enderecos/editar.html", endereco=endereco)
    @app.route("/enderecos/deletar/<endereco_id>", methods=["POST"])
    def deletar_endereco(endereco_id):
        endereco_oid = to_objectid(endereco_id)
        if not endereco_oid:
            flash("ID do endereço inválido!", "error")
            return redirect(url_for("pessoas"))

        endereco = mongo.db.enderecos.find_one({"_id": endereco_oid})
        if not endereco:
            flash("Endereço não encontrado!", "error")
            return redirect(url_for("pessoas"))

        mongo.db.enderecos.delete_one({"_id": endereco_oid})
        flash("Endereço deletado com sucesso!", "success")
        return redirect(url_for("listar_enderecos", pessoa_id=str(endereco["pessoa_id"])))
