from collections import deque
from nodo import Nodo


class ArbolBinarioBusqueda:
    """
    Clase que representa un árbol binario de búsqueda (ABB).
    """

    def __init__(self):
        """Inicializa un árbol vacío."""
        self._raiz = None

    def vacio(self):
        """Devuelve True si el árbol está vacío."""
        return self._raiz is None

    def insertar(self, dato):
        """Inserta un dato en el árbol."""
        self._raiz = self._insertar_recursivo(self._raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.hijo_izq = self._insertar_recursivo(nodo.hijo_izq, dato)
        elif dato > nodo.dato:
            nodo.hijo_der = self._insertar_recursivo(nodo.hijo_der, dato)
        return nodo

    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar_recursivo(self._raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.dato:
            return True
        if valor < nodo.dato:
            return self._buscar_recursivo(nodo.hijo_izq, valor)
        return self._buscar_recursivo(nodo.hijo_der, valor)

    def in_orden(self):
        """Devuelve una lista con el recorrido en in-orden."""
        return self._in_orden_recursivo(self._raiz)

    def _in_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        return (self._in_orden_recursivo(nodo.hijo_izq) +
                [nodo.dato] +
                self._in_orden_recursivo(nodo.hijo_der))

    def pre_orden(self):
        """Devuelve una lista con el recorrido en pre-orden."""
        return self._pre_orden_recursivo(self._raiz)

    def _pre_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        return ([nodo.dato] +
                self._pre_orden_recursivo(nodo.hijo_izq) +
                self._pre_orden_recursivo(nodo.hijo_der))

    def post_orden(self):
        """Devuelve una lista con el recorrido en post-orden."""
        return self._post_orden_recursivo(self._raiz)

    def _post_orden_recursivo(self, nodo):
        if nodo is None:
            return []
        return (self._post_orden_recursivo(nodo.hijo_izq) +
                self._post_orden_recursivo(nodo.hijo_der) +
                [nodo.dato])

    def recorrido_por_nivel(self):
        """Devuelve una lista con el recorrido por niveles."""
        if self.vacio():
            return []
        resultado = []
        cola = deque([self._raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.dato)
            if actual.hijo_izq:
                cola.append(actual.hijo_izq)
            if actual.hijo_der:
                cola.append(actual.hijo_der)
        return resultado

    def contar_nodos(self):
        """Cuenta la cantidad de nodos en el árbol."""
        return self._contar_nodos_recursivo(self._raiz)

    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return (1 +
                self._contar_nodos_recursivo(nodo.hijo_izq) +
                self._contar_nodos_recursivo(nodo.hijo_der))

    def altura(self):
        """Calcula la altura del árbol."""
        return self._altura_recursivo(self._raiz)

    def _altura_recursivo(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura_recursivo(nodo.hijo_izq),
                       self._altura_recursivo(nodo.hijo_der))

    def minimo(self):
        """Devuelve el valor mínimo del árbol."""
        if self.vacio():
            return None
        actual = self._raiz
        while actual.hijo_izq:
            actual = actual.hijo_izq
        return actual.dato

    def maximo(self):
        """Devuelve el valor máximo del árbol."""
        if self.vacio():
            return None
        actual = self._raiz
        while actual.hijo_der:
            actual = actual.hijo_der
        return actual.dato

    def eliminar(self, dato):
        """Elimina un nodo con el valor especificado."""
        self._raiz = self._eliminar_recursivo(self._raiz, dato)

    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.hijo_izq = self._eliminar_recursivo(nodo.hijo_izq, dato)
        elif dato > nodo.dato:
            nodo.hijo_der = self._eliminar_recursivo(nodo.hijo_der, dato)
        else:
            if nodo.hijo_izq is None:
                return nodo.hijo_der
            if nodo.hijo_der is None:
                return nodo.hijo_izq
            sucesor = self._minimo_nodo(nodo.hijo_der)
            nodo.dato = sucesor.dato
            nodo.hijo_der = self._eliminar_recursivo(nodo.hijo_der, sucesor.dato)
        return nodo

    def _minimo_nodo(self, nodo):
        actual = nodo
        while actual.hijo_izq is not None:
            actual = actual.hijo_izq
        return actual
