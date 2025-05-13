import json
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from models.equipo import Equipo  
from models.jugador import Jugador
from models.partido import Partido
from models.arbolTorneo import ArbolTorneo

app = Flask(__name__)

# Conexión a la base de datos MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["torneo_eliminacion_directa"]
equipos= db["equipo"]            
jugadores= db["jugador"]
partidos= db["partido"]

# Ruta para cargar los datos de equipos desde un archivo JSON
@app.route('/cargar_equipos', methods=['POST'])
def cargar_equipos():
    data = request.get_json()  # Traemos los datos del JSON
    equipos_lista=[]

    for equipo_data in data:
        # Crear instancia de Equipo
        equipo = Equipo(
            nombre=equipo_data["nombre"],
            director_tecnico=equipo_data["director_tecnico"],
            imagen=equipo_data["imagen"]
        )

        # Insertar el equipo en Mongo usando to_dict (sin plantel)
        equipo_id = equipos.insert_one(equipo.to_dict()).inserted_id

        # Agregar jugadores (si hay)
        for jugador_data in equipo_data.get("jugadores", []):
            jugador = Jugador(
                nombre=jugador_data["nombre"],
            )

            # Insertar jugador en Mongo usando su to_dict()
            jugador_dict = jugador.to_dict()
            jugador_dict["equipo_id"] = str(equipo_id)  # Relación jugador-equipo
            jugadores.insert_one(jugador_dict)

            # Agregar el jugador al objeto en memoria (opcional)
            equipo.agregar_jugador(jugador_data["nombre"])

        # Guardar el equipo en la lista en memoria
        equipos_lista.append(equipo)

    return jsonify({"mensaje": "Equipos y jugadores cargados exitosamente"}), 201

"""
# Ruta para crear un nuevo equipo
@app.route('/crear_equipo', methods=['POST'])
def crear_equipo():
    try:
        data = request.get_json()
        nuevo_equipo = Equipo(data["nombre"], data["director_tecnico"], data.get("imagen"))
        
        for jugador_data in data.get("jugadores", []):
            jugador = Jugador(jugador_data["nombre"])
            nuevo_equipo.agregar_jugador(jugador.nombre)
        
        equipos_collection.insert_one(nuevo_equipo.to_dict())  # Guardar el equipo en MongoDB
        return jsonify({"message": "Equipo creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para actualizar un equipo
@app.route('/actualizar_equipo/<equipo_id>', methods=['PUT'])
def actualizar_equipo(equipo_id):
    try:
        data = request.get_json()
        equipo = equipos_collection.find_one({"_id": equipo_id})

        if not equipo:
            return jsonify({"error": "Equipo no encontrado"}), 404

        equipos_collection.update_one({"_id": equipo_id}, {"$set": data})  # Actualizar el equipo
        return jsonify({"message": "Equipo actualizado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para eliminar un equipo
@app.route('/eliminar_equipo/<equipo_id>', methods=['DELETE'])
def eliminar_equipo(equipo_id):
    try:
        equipos_collection.delete_one({"_id": equipo_id})  # Eliminar el equipo
        return jsonify({"message": "Equipo eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para crear o actualizar un partido
@app.route('/crear_o_actualizar_partido', methods=['POST'])
def crear_o_actualizar_partido():
    try:
        data = request.get_json()
        partido_data = data["partido"]
        
        # Verificar si el partido ya existe en la base de datos
        partido = partidos_collection.find_one({"_id": partido_data["id"]})
        
        if partido:
            # Si el partido ya existe, actualizarlo
            partidos_collection.update_one(
                {"_id": partido_data["id"]}, 
                {"$set": partido_data}  # Actualizar con los nuevos datos
            )
            return jsonify({"message": "Partido actualizado exitosamente"}), 200
        else:
            # Si el partido no existe, crear uno nuevo
            partidos_collection.insert_one(partido_data)
            return jsonify({"message": "Partido creado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para registrar los resultados del partido
@app.route('/registrar_resultado', methods=['POST'])
def registrar_resultado():
    try:
        data = request.get_json()
        partido_data = data["partido"]
        goles_equipo1 = partido_data["goles_equipo1"]
        goles_equipo2 = partido_data["goles_equipo2"]
        
        # Buscar el partido correspondiente en la base de datos
        partido = partidos_collection.find_one({"_id": partido_data["id"]})
        if not partido:
            return jsonify({"error": "Partido no encontrado"}), 404

        # Actualizar los goles y determinar el ganador
        partido["goles_equipo1"] = goles_equipo1
        partido["goles_equipo2"] = goles_equipo2
        partido["ganador"] = partido["equipo1"] if goles_equipo1 > goles_equipo2 else partido["equipo2"]
        
        # Actualizar el partido en la base de datos
        partidos_collection.update_one({"_id": partido_data["id"]}, {"$set": partido})

        # Actualizar el árbol del torneo con los nuevos resultados
        arbol = ArbolTorneo()  # Este debe ser cargado previamente desde el archivo JSON o base de datos
        arbol.actualizar_torneo(partido)

        return jsonify({"message": "Resultado registrado y torneo actualizado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Ruta para obtener el árbol de partidos del torneo
@app.route('/obtener_torneo', methods=['GET'])
def obtener_torneo():
    try:
        arbol = ArbolTorneo()  # Este debe ser cargado previamente desde el archivo JSON o base de datos
        resultado_torneo = arbol.obtener_partidos_por_nivel()
        return jsonify({"torneo": resultado_torneo}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400 
"""
if __name__ == '__main__':
    app.run(debug=True)
