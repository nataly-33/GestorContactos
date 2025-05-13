# Equipo.py
from jugador import Jugador

class Equipo:
    def __init__(self, nombre, director_tecnico,imagen):
        self.nombre = nombre
        self.director_tecnico = director_tecnico
        self.imagen = imagen  
        self.jugadores = []   

    def agregar_jugador(self, nombre_jugador):
        nuevo = Jugador(nombre_jugador)
        self.jugadores.append(nuevo)

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "director_tecnico": self.director_tecnico,
            "imagen": self.imagen
        }
