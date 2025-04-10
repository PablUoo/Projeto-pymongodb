from flask_pymongo import PyMongo
from bson import ObjectId

mongo = PyMongo()

class Filho:
    def __init__(self, pessoa_id, nome, idade, _id=None):
        self.pessoa_id = pessoa_id
        self.nome = nome
        self.idade = idade
        self._id = _id

    def salvar(self):
        dados = {"pessoa_id": ObjectId(self.pessoa_id), "nome": self.nome, "idade": self.idade}
        if self._id:
            mongo.db.filhos.update_one({"_id": ObjectId(self._id)}, {"$set": dados})
        else:
            mongo.db.filhos.insert_one(dados)

    @staticmethod
    def obter_todos(pessoa_id):
        return mongo.db.filhos.find({"pessoa_id": ObjectId(pessoa_id)})

    @staticmethod
    def obter(_id):
        return mongo.db.filhos.find_one({"_id": ObjectId(_id)})

    @staticmethod
    def deletar(_id):
        mongo.db.filhos.delete_one({"_id": ObjectId(_id)})