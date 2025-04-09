
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()


class Pessoa:
    def __init__(self, nome, email, idade, _id=None):
        self.nome = nome
        self.email = email
        self.idade = idade
        self._id = _id  # Armazena o ID caso ele exista

    def salvar(self):
        """Salva ou atualiza a pessoa no MongoDB."""
        pessoa_db = mongo.db.pessoas
        if self._id:  # Se _id existe, é uma atualização
            pessoa_db.update_one(
                {"_id": ObjectId(self._id)},
                {"$set": {"nome": self.nome, "email": self.email, "idade": self.idade}}, 
                upsert=True
            )
        else:  # Caso contrário, é uma nova inserção
            pessoa_db.insert_one({"nome": self.nome, "email": self.email, "idade": self.idade})

    def deletar(self):
        """Deleta a pessoa do MongoDB pelo _id."""
        pessoa_db = mongo.db.pessoas
        pessoa_db.delete_one({"_id": ObjectId(self._id)})

    @staticmethod
    def obter(id):
        """Obtém a pessoa pelo _id."""
        pessoa_db = mongo.db.pessoas
        pessoa = pessoa_db.find_one({"_id": ObjectId(id)})
        if pessoa:
            return Pessoa(pessoa["nome"], pessoa["email"], pessoa["idade"], str(pessoa["_id"]))
        return None

    @staticmethod
    def obter_todas():
        """Obtém todas as pessoas."""
        pessoa_db = mongo.db.pessoas
        pessoas = []
        for p in pessoa_db.find():
            pessoas.append(Pessoa(p["nome"], p["email"], p["idade"], str(p["_id"])))
        return pessoas
