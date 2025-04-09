from flask import Blueprint, render_template, request, redirect, url_for
from models.pessoa import Pessoa
from bson import ObjectId

pessoa_controller = Blueprint('pessoa_controller', __name__)

@pessoa_controller.route('/')
def index():
    """Rota principal que exibe todas as pessoas."""
    pessoas = Pessoa.obter_todas()
    return render_template('index.html', pessoas=pessoas)

@pessoa_controller.route('/adicionar', methods=['POST'])
def adicionar():
    """Rota para adicionar uma nova pessoa."""
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade', type=int)
    
    if nome and email and idade:
        pessoa = Pessoa(nome, email, idade)
        pessoa.salvar()
    return redirect(url_for('pessoa_controller.index'))

@pessoa_controller.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    pessoa = mongo.db.pessoas.find_one({"_id": ObjectId(pessoa_id)})
    """Rota para editar os dados de uma pessoa."""
    pessoa = Pessoa.obter(id)
    if request.method == 'POST':
        pessoa.nome = request.form.get('nome')
        pessoa.idade = request.form.get('idade', type=int)
        pessoa.salvar()
        return redirect(url_for('pessoa_controller.index'))
    return render_template('editar.html', pessoa=pessoa)

@pessoa_controller.route('/deletar/<pessoa_id>', methods=['GET'])
def deletar(pessoa_id):
    """Rota para deletar uma pessoa pelo _id."""
    pessoa = Pessoa.obter(pessoa_id)
    if pessoa:
        pessoa.deletar()
    return redirect(url_for('pessoa_controller.index'))
