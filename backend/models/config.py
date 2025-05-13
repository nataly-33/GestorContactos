class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.goles = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0

    def registrar_estadisticas(self, goles=0, asistencias=0, amarillas=0, rojas=0):
        self.goles += goles
        self.asistencias += asistencias
        self.tarjetas_amarillas += amarillas
        self.tarjetas_rojas += rojas

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "goles": self.goles,
            "asistencias": self.asistencias,
            "amarillas": self.tarjetas_amarillas,
            "rojas": self.tarjetas_rojas
        }
