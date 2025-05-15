from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from flask_pymongo import PyMongo

from models.contacto import Contacto
from models.arbolBST import ArbolBST

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost/proyectobst")
mongo = PyMongo(app)
db = mongo.db.contactos


def recargar_arbol():
    """
    Recarga el árbol BST con los contactos almacenados en la base de datos MongoDB.

    Extrae todos los documentos de la colección y los inserta en el árbol.
    """
    global arbol_contactos
    arbol_contactos = ArbolBST()
    contactos = list(db.find())
    for c in contactos:
        contacto = Contacto(
            c.get("nombre", ""),
            c.get("telefono", ""),
            c.get("correo", ""),
            c.get("imagen", "")
        )
        arbol_contactos.insertar(contacto)


recargar_arbol()


@app.route('/crear', methods=['POST'])
def crear_contacto():
    """
    Crea un nuevo contacto a partir de los datos JSON recibidos.

    Valida que el nombre esté presente y que no exista un contacto con el mismo nombre.
    Inserta el contacto en MongoDB y en el árbol BST.

    Returns:
        JSON con mensaje de éxito y el ID insertado,
        o JSON con error y código HTTP 400 o 500 en caso de fallo.
    """
    try:
        data = request.get_json()
        if not data or 'nombre' not in data:
            return jsonify({"error": "Falta el nombre del contacto"}), 400

        nombre = data.get('nombre')
        telefono = data.get('telefono')
        correo = data.get('correo')
        imagen = data.get('imagen') or "/perfil-default.png"

        if arbol_contactos.buscar(nombre):
            return jsonify({"error": "Ya existe un contacto con ese nombre"}), 400

        nuevo_contacto = Contacto(nombre, telefono, correo, imagen)
        resultado = db.insert_one(nuevo_contacto.to_dict())
        arbol_contactos.insertar(nuevo_contacto)

        return jsonify({
            "mensaje": "Contacto agregado correctamente",
            "_id": str(resultado.inserted_id)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/buscar/<nombre>', methods=['GET'])
def buscar_contacto(nombre):
    """
    Busca un contacto en el árbol BST por su nombre.

    Args:
        nombre (str): Nombre del contacto a buscar.

    Returns:
        JSON con los datos del contacto si existe,
        o mensaje de error 404 si no se encuentra.
    """
    try:
        contacto = arbol_contactos.buscar(nombre)
        if contacto:
            return jsonify(contacto.to_dict())
        return jsonify({"mensaje": "Contacto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/listar', methods=['GET'])
def listar_contactos():
    """
    Lista todos los contactos almacenados en el árbol BST.

    Returns:
        JSON con la lista de contactos.
    """
    try:
        contactos = arbol_contactos.listar()
        return jsonify(contactos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/eliminar/<nombre>', methods=['DELETE'])
def eliminar_contacto(nombre):
    """
    Elimina un contacto por nombre de MongoDB y del árbol BST.

    Args:
        nombre (str): Nombre del contacto a eliminar.

    Returns:
        JSON con mensaje de éxito o error 404 si no se encuentra el contacto.
    """
    try:
        contacto = arbol_contactos.buscar(nombre)
        if contacto:
            db.delete_one({"nombre": nombre})
            arbol_contactos.eliminar(nombre)
            return jsonify({"mensaje": f"Contacto '{nombre}' eliminado"})
        return jsonify({"error": "Contacto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
