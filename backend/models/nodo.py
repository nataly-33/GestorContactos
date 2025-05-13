class Nodo:
    """
    Clase que representa un nodo de un árbol binario.

    Atributos:
        dato: Dato almacenado en el nodo.
        hijo_izq: Referencia al hijo izquierdo.
        hijo_der: Referencia al hijo derecho.
    """

    def __init__(self, dato):
        """Inicializa un nodo con el dato proporcionado y sin hijos."""
        self._dato = dato
        self._hijo_izq = None
        self._hijo_der = None

    @property
    def dato(self):
        """Devuelve el dato del nodo."""
        return self._dato

    @dato.setter
    def dato(self, valor):
        """Establece el dato del nodo."""
        self._dato = valor

    @property
    def hijo_izq(self):
        """Devuelve el hijo izquierdo."""
        return self._hijo_izq

    @hijo_izq.setter
    def hijo_izq(self, nodo):
        """Establece el hijo izquierdo."""
        self._hijo_izq = nodo

    @property
    def hijo_der(self):
        """Devuelve el hijo derecho."""
        return self._hijo_der

    @hijo_der.setter
    def hijo_der(self, nodo):
        """Establece el hijo derecho."""
        self._hijo_der = nodo
