from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from models.contacto import Contacto
from models.arbolBST import ArbolBST

app = Flask(__name__)
CORS(app)

# Configuración de MongoDB
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost/proyectobst")
mongo = PyMongo(app)
db = mongo.db.contactos

# Inicializar árbol BST
arbol_contactos = ArbolBST()

def cargar_contactos_en_arbol():
    contactos = db.find()
    for c in contactos:
        contacto = Contacto(
            c.get("nombre", ""),
            c.get("telefono", ""),
            c.get("correo", ""),
            c.get("imagen", "")
        )
        arbol_contactos.insertar(contacto)

cargar_contactos_en_arbol()


# Rutas

@app.route('/crear', methods=['POST'])
def crear_contacto():
    data = request.get_json()
    
    # Validaciones básicas
    if not data or 'nombre' not in data:
        return jsonify({"error": "Falta el nombre del contacto"}), 400
    
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    correo = data.get('correo')
    imagen = data.get('imagen')

    # Verificar si ya existe el contacto por nombre
    if arbol_contactos.buscar(nombre):
        return jsonify({"error": "Ya existe un contacto con ese nombre"}), 400

    # Crear y guardar en MongoDB
    nuevo_contacto = Contacto(nombre, telefono, correo, imagen)
    resultado = db.insert_one(nuevo_contacto.to_dict())

    # Insertar en el árbol
    arbol_contactos.insertar(nuevo_contacto)

    return jsonify({
        "mensaje": "Contacto agregado correctamente",
        "_id": str(resultado.inserted_id)
    })


@app.route('/buscar/<nombre>', methods=['GET'])
def buscar_contacto(nombre):
    contacto = arbol_contactos.buscar(nombre)

    if contacto:
        return jsonify(contacto.to_dict())
    else:
        return jsonify({"mensaje": "Contacto no encontrado"}), 404


@app.route('/listar', methods=['GET'])
def listar_contactos():
    contactos = arbol_contactos.listar()
    return jsonify(contactos)


@app.route('/eliminar/<nombre>', methods=['DELETE'])
def eliminar_contacto(nombre):
    contacto = arbol_contactos.buscar(nombre)
    if contacto:
        db.delete_one({"nombre": nombre})
        arbol_contactos.eliminar(nombre)
        return jsonify({"mensaje": f"Contacto '{nombre}' eliminado"})
    else:
        return jsonify({"error": "Contacto no encontrado"}), 404

@app.route('/editar/<nombre>', methods=['PUT'])
def editar_contacto(nombre):
    contacto = arbol_contactos.buscar(nombre)

    if not contacto:
        return jsonify({"error": "Contacto no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    # Recibir todos los campos del contacto
    nuevo_nombre = data.get("nombre", contacto.nombre)
    telefono = data.get("telefono", contacto.telefono)
    correo = data.get("correo", contacto.correo)
    imagen = data.get("imagen", contacto.imagen)

    # Validaciones básicas
    if not telefono or len(telefono) != 8 or not telefono.isdigit():
        return jsonify({"error": "Teléfono debe tener 8 dígitos"}), 400
    if not correo or "@" not in correo:
        return jsonify({"error": "Correo inválido"}), 400

    # Si cambia el nombre, hay que borrar y reinsertar en el árbol
    if nuevo_nombre != contacto.nombre:
        db.update_one(
            {"nombre": nombre},
            {"$set": {
                "nombre": nuevo_nombre,
                "telefono": telefono,
                "correo": correo,
                "imagen": imagen
            }}
        )
        arbol_contactos.eliminar(nombre)
        nuevo_contacto = Contacto(nuevo_nombre, telefono, correo, imagen)
        arbol_contactos.insertar(nuevo_contacto)
    else:
        db.update_one(
            {"nombre": nombre},
            {"$set": {
                "telefono": telefono,
                "correo": correo,
                "imagen": imagen
            }}
        )
        # Actualizar directamente en el árbol (opcional)
        contacto.telefono = telefono
        contacto.correo = correo
        contacto.imagen = imagen

    return jsonify({
        "mensaje": "Contacto actualizado correctamente",
        "contacto": {
            "nombre": nuevo_nombre,
            "telefono": telefono,
            "correo": correo,
            "imagen": imagen
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)