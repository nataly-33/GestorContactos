# NodoPartido.py
from partido import Partido

class NodoPartido:
    def __init__(self, partido):
        self.partido = partido
        self.izquierdo = None  # Hijo izquierdo
        self.derecho = None    # Hijo derecho

# ArbolTorneo.py
import random
from partido import Partido
from datetime import datetime, timedelta

class ArbolTorneo:
    def __init__(self, equipos):
        self.raiz = None
        self.equipos = equipos
        self.partidos_por_nivel = {}
        self.horas_disponibles = ["13:00", "16:00", "19:00"]
        self.fecha_inicio = datetime.now() + timedelta(days=7)

    def crear_torneo(self):
        random.shuffle(self.equipos)
        nodos = [NodoPartido(Partido(equipo, None)) for equipo in self.equipos]

        while len(nodos) % 2 != 0:
            nodos.append(NodoPartido(Partido("BYE", None)))

        fecha_actual = self.fecha_inicio
        nivel = 0

        while len(nodos) > 1:
            nuevos_nodos = []
            random.shuffle(self.horas_disponibles)
            horarios = self.horas_disponibles.copy()

            for i in range(0, len(nodos), 2):
                equipo1 = nodos[i].partido.equipo1 if nodos[i].partido.equipo2 is None else nodos[i].partido.ganador
                equipo2 = nodos[i+1].partido.equipo1 if nodos[i+1].partido.equipo2 is None else nodos[i+1].partido.ganador

                partido = Partido(equipo1, equipo2, fecha_actual.date(), horarios.pop(0))
                nuevo_nodo = NodoPartido(partido)
                nuevo_nodo.izquierdo = nodos[i]
                nuevo_nodo.derecho = nodos[i+1]
                nuevos_nodos.append(nuevo_nodo)

                if nivel not in self.partidos_por_nivel:
                    self.partidos_por_nivel[nivel] = []
                self.partidos_por_nivel[nivel].append(nuevo_nodo)

                if not horarios:
                    horarios = self.horas_disponibles.copy()
                    random.shuffle(horarios)

            nodos = nuevos_nodos
            fecha_actual += timedelta(days=7)
            nivel += 1

        self.raiz = nodos[0]
        self.fecha_final = fecha_actual + timedelta(days=7)
        self.raiz.partido.fecha = self.fecha_final.date()
        self.raiz.partido.hora = random.choice(self.horas_disponibles)

    def obtener_nombre_ronda(self, nivel):
        if nivel == 0:
            return "Octavos"
        elif nivel == 1:
            return "Cuartos"
        elif nivel == 2:
            return "Semifinal"
        elif nivel == 3:
            return "Final"
        else:
            return f"Ronda {nivel}"

    def obtener_partidos_por_nivel(self):
        resultado = []
        niveles = sorted(self.partidos_por_nivel.keys(), reverse=True)

        for nivel in niveles:
            ronda = {
                "nivel": nivel,
                "nombreRonda": self.obtener_nombre_ronda(nivel),
                "partidos": [nodo.partido.to_dict() for nodo in self.partidos_por_nivel[nivel]]
            }
            resultado.append(ronda)

        # Agregar la final aparte
        if self.raiz:
            final = {
                "nivel": len(self.partidos_por_nivel),
                "nombreRonda": "Final",
                "partidos": [self.raiz.partido.to_dict()]
            }
            resultado.append(final)

        return resultado
