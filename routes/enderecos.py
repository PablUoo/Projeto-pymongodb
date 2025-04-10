from flask import render_template, request, redirect, url_for, flash

def init_enderecos_routes(app, mongo, to_objectid):
    @app.route("/pessoa/<pessoa_id>/enderecos")
    def listar_enderecos(pessoa_id):
        enderecos = Endereco.obter_todos(pessoa_id)
        return render_template("enderecos/index.html", enderecos=enderecos, pessoa_id=pessoa_id)

    @app.route("/pessoa/<pessoa_id>/enderecos/criar", methods=["GET", "POST"])
    def criar_endereco(pessoa_id):
        if request.method == "POST":
            rua = request.form["rua"]
            numero = request.form["numero"]
            cidade = request.form["cidade"]
            endereco = Endereco(pessoa_id, rua, numero, cidade)
            endereco.salvar()
            flash("Endereço adicionado!", "success")
            return redirect(url_for("listar_enderecos", pessoa_id=pessoa_id))
        return render_template("enderecos/criar.html", pessoa_id=pessoa_id)

    @app.route("/enderecos/editar/<endereco_id>", methods=["GET", "POST"])
    def editar_endereco(endereco_id):
        endereco = Endereco.obter(endereco_id)
        if not endereco:
            flash("Endereço não encontrado!", "error")
            return redirect(url_for("pessoas"))

        if request.method == "POST":
            rua = request.form["rua"]
            numero = request.form["numero"]
            cidade = request.form["cidade"]
            Endereco(endereco["pessoa_id"], rua, numero, cidade, endereco_id).salvar()
            flash("Endereço atualizado!", "success")
            return redirect(url_for("listar_enderecos", pessoa_id=endereco["pessoa_id"]))
        return render_template("enderecos/editar.html", endereco=endereco)
