from flask import render_template, request, redirect, url_for, flash

def init_filhos_routes(app, mongo, to_objectid):
    @app.route("/pessoa/<pessoa_id>/filhos")
    def listar_filhos(pessoa_id):
        pessoa_oid = to_objectid(pessoa_id)
        if not pessoa_oid:
            flash("ID da pessoa inválido", "error")
            return redirect(url_for("pessoas"))

        filhos = mongo.db.filhos.find({"pessoa_id": pessoa_oid})
        return render_template("filhos/index.html", filhos=filhos, pessoa_id=pessoa_id)

    @app.route("/pessoa/<pessoa_id>/filhos/criar", methods=["GET", "POST"])
    def criar_filho(pessoa_id):
        pessoa_oid = to_objectid(pessoa_id)
        if not pessoa_oid:
            flash("ID da pessoa inválido", "error")
            return redirect(url_for("pessoas"))

        if request.method == "POST":
            nome = request.form.get("nome")
            idade = request.form.get("idade", type=int)

            if nome and idade is not None:
                mongo.db.filhos.insert_one({
                    "pessoa_id": pessoa_oid,
                    "nome": nome,
                    "idade": idade
                })
                flash("Filho criado com sucesso!", "success")
                return redirect(url_for("listar_filhos", pessoa_id=pessoa_id))
            else:
                flash("Todos os campos são obrigatórios!", "error")

        return render_template("filhos/criar.html", pessoa_id=pessoa_id)

    @app.route("/filhos/editar/<filho_id>", methods=["GET", "POST"])
    def editar_filho(filho_id):
        filho_oid = to_objectid(filho_id)
        if not filho_oid:
            flash("ID do filho inválido", "error")
            return redirect(url_for("pessoas"))

        filho = mongo.db.filhos.find_one({"_id": filho_oid})
        if not filho:
            flash("Filho não encontrado!", "error")
            return redirect(url_for("pessoas"))

        if request.method == "POST":
            nome = request.form.get("nome")
            idade = request.form.get("idade", type=int)

            if nome and idade is not None:
                mongo.db.filhos.update_one(
                    {"_id": filho_oid},
                    {"$set": {"nome": nome, "idade": idade}}
                )
                flash("Filho atualizado!", "success")
                return redirect(url_for("listar_filhos", pessoa_id=str(filho["pessoa_id"])))
            else:
                flash("Todos os campos são obrigatórios!", "error")

        return render_template("filhos/editar.html", filho=filho)