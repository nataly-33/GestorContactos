class Contacto:
    def __init__(self, nombre, telefono, correo,imagen):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.imagen =imagen

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "imagen": self.imagen
        }
