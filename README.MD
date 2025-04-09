# se não tem o venv
python3 -m venv venv

# acessar o venv
source venv/bin/activate

# instalar Dependencia
pip install flask flask-pymongo

# Start mongo
sudo systemctl start mongod
