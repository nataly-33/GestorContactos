from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
import os

from controllers import contacto_controller

app = Flask(__name__)
CORS(app)

# Configuración de MongoDB
app.config["MONGO_URI"] = os.environ.get(
    "MONGO_URI", "mongodb://localhost/proyectobst"
)
mongo = PyMongo(app)

# Inicializa el árbol BST y la base de datos
contacto_controller.configurar_db_y_arbol(mongo)


# Rutas
@app.route('/crear', methods=['POST'])
def crear():
    return contact_controller.crear_contacto()


@app.route('/buscar/<nombre>', methods=['GET'])
def buscar(nombre):
    return contact_controller.buscar_contacto(nombre)


@app.route('/listar', methods=['GET'])
def listar():
    return contact_controller.listar_contactos()


@app.route('/eliminar/<nombre>', methods=['DELETE'])
def eliminar(nombre):
    return contact_controller.eliminar_contacto(nombre)


# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
