class Nodo:
    def __init__(self, contacto):
        self.contacto = contacto
        self.izquierda = None
        self.derecha = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, contacto):
        if not self.raiz:
            self.raiz = Nodo(contacto)
        else:
            self._insertar(self.raiz, contacto)

    def _insertar(self, nodo_actual, contacto):
        if contacto.nombre.lower() < nodo_actual.contacto.nombre.lower():
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(contacto)
            else:
                self._insertar(nodo_actual.izquierda, contacto)
        elif contacto.nombre.lower() > nodo_actual.contacto.nombre.lower():
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(contacto)
            else:
                self._insertar(nodo_actual.derecha, contacto)

    def buscar(self, nombre):
        return self._buscar(self.raiz, nombre.lower())

    def _buscar(self, nodo_actual, nombre):
        if nodo_actual is None:
            return None
        if nombre == nodo_actual.contacto.nombre.lower():
            return nodo_actual.contacto
        elif nombre < nodo_actual.contacto.nombre.lower():
            return self._buscar(nodo_actual.izquierda, nombre)
        else:
            return self._buscar(nodo_actual.derecha, nombre)

    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre.lower())

    def _eliminar(self, nodo_actual, nombre):
        if nodo_actual is None:
            return nodo_actual

        if nombre < nodo_actual.contacto.nombre.lower():
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, nombre)
        elif nombre > nodo_actual.contacto.nombre.lower():
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, nombre)
        else:
            # Caso 1: sin hijos
            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
                return None
            # Caso 2: solo hijo derecho
            elif nodo_actual.izquierda is None:
                return nodo_actual.derecha
            # Caso 3: solo hijo izquierdo
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            # Caso 4: dos hijos
            else:
                temp = self._min_value_node(nodo_actual.derecha)
                nodo_actual.contacto = temp.contacto
                nodo_actual.derecha = self._eliminar(nodo_actual.derecha, temp.contacto.nombre)
        return nodo_actual

    def _min_value_node(self, nodo):
        current = nodo
        while current.izquierda:
            current = current.izquierda
        return current

    def listar(self):
        contactos = []
        self._inorden(self.raiz, contactos)
        return contactos

    def _inorden(self, nodo_actual, lista):
        if nodo_actual:
            self._inorden(nodo_actual.izquierda, lista)
            lista.append(nodo_actual.contacto.to_dict())
            self._inorden(nodo_actual.derecha, lista)