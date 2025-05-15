class Contacto:
    """Clase que representa un contacto con sus datos básicos."""

    def __init__(self, nombre, telefono, correo, imagen):
        """
        Inicializa un contacto con nombre, teléfono, correo e imagen.

        Args:
            nombre (str): Nombre completo del contacto.
            telefono (str): Número de teléfono del contacto.
            correo (str): Correo electrónico del contacto.
            imagen (str): URL o ruta de la imagen del contacto.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.imagen = imagen

    def to_dict(self):
        """
        Convierte el objeto Contacto en un diccionario.

        Returns:
            dict: Diccionario con los atributos del contacto.
        """
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "imagen": self.imagen,
        }
