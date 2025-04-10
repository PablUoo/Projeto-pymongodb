# 📘 Projeto Flask com MongoDB

Este projeto utiliza Flask (microframework em Python) e MongoDB como banco de dados. Abaixo está a documentação para configurar, rodar e desenvolver no ambiente.

---

## ✅ Pré-requisitos

Certifique-se de ter instalado:

- Python 3
- MongoDB
- `pip` (gerenciador de pacotes do Python)

---

## 🛠️ 1. Criar Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv venv
```

---

## 🚀 2. Ativar o Ambiente Virtual

### Linux/macOS:

```bash
source venv/bin/activate
```

### Windows:

```bash
venv\Scripts\activate
```

---

## 📦 3. Instalar Dependências

Instale os pacotes necessários:

```bash
pip install flask flask-pymongo
```

Para salvar as dependências:

```bash
pip freeze > requirements.txt
```

Para instalar posteriormente:

```bash
pip install -r requirements.txt
```

---

## 🍃 4. Iniciar o MongoDB

No Linux (com `systemd`):

```bash
sudo systemctl start mongod
```

Verifique o status:

```bash
sudo systemctl status mongod
```

---

## ▶️ 5. Rodar a Aplicação Flask

Execute o projeto:

```bash
flask run
```

Caso necessário, defina a variável de ambiente `FLASK_APP`:

### Linux/macOS:

```bash
export FLASK_APP=app.py
```

### Windows:

```bash
set FLASK_APP=app.py
```

---

## 📁 Estrutura Sugerida do Projeto

```bash
.
├── app.py
├── venv/
├── templates/
│   └── index.html
├── static/
├── requirements.txt
└── README.md
```

---

## 🧪 Testar Conexão com MongoDB

Exemplo simples de conexão no `app.py`:

```python
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/seu_banco"

mongo = PyMongo(app)

@app.route('/')
def index():
    return 'MongoDB conectado com sucesso!'
```

---

## 🧹 Dicas Finais

- Use `deactivate` para sair do ambiente virtual.
- Mantenha o `requirements.txt` atualizado.
- Utilize `flash`, `render_template` e `request` do Flask para criar rotas com formulários e interações com o banco.

---