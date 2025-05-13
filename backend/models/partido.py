# Partido.py
class Partido:
    def __init__(self, equipo1, equipo2, fecha=None, hora=None):
        self.equipo1 = equipo1  # Nombre del primer equipo
        self.equipo2 = equipo2  # Nombre del segundo equipo
        self.ganador = None     # Nombre del equipo ganador
        self.fecha = fecha      # Fecha del partido
        self.hora = hora        # Hora del partido
        self.goles_equipo1=None
        self.goles_equipo2=None

    def asignar_ganador(self, ganador):
        self.ganador = ganador

    def asignar_resultado(self, goles_equipo1, goles_equipo2):
        self.goles_equipo1 = goles_equipo1
        self.goles_equipo2 = goles_equipo2

    def to_dict(self):
        return {
            "equipo1": self.equipo1,
            "equipo2": self.equipo2,
            "ganador": self.ganador,
            "fecha": str(self.fecha),
            "hora": self.hora
        }