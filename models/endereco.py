from flask_pymongo import PyMongo
from bson import ObjectId

mongo = PyMongo()

class Endereco:
    def __init__(self, pessoa_id, rua, numero, cidade, _id=None):
        self.pessoa_id = pessoa_id
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self._id = _id

    def salvar(self):
        dados = {"pessoa_id": ObjectId(self.pessoa_id), "rua": self.rua, "numero": self.numero, "cidade": self.cidade}
        if self._id:
            mongo.db.enderecos.update_one({"_id": ObjectId(self._id)}, {"$set": dados})
        else:
            mongo.db.enderecos.insert_one(dados)

    @staticmethod
    def obter_todos(pessoa_id):
        return mongo.db.enderecos.find({"pessoa_id": ObjectId(pessoa_id)})

    @staticmethod
    def obter(_id):
        return mongo.db.enderecos.find_one({"_id": ObjectId(_id)})

    @staticmethod
    def deletar(_id):
        mongo.db.enderecos.delete_one({"_id": ObjectId(_id)})
