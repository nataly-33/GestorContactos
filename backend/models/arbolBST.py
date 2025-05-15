class Nodo:
    """Nodo de un árbol binario de búsqueda que contiene un contacto."""

    def __init__(self, contacto):
        """
        Inicializa un nodo con un contacto.

        Args:
            contacto: Objeto que representa el contacto.
        """
        self.contacto = contacto
        self.izquierda = None
        self.derecha = None


class ArbolBST:
    """Árbol binario de búsqueda para almacenar contactos ordenados por nombre."""

    def __init__(self):
        """Inicializa el árbol con la raíz vacía."""
        self.raiz = None

    def insertar(self, contacto):
        """
        Inserta un nuevo contacto en el árbol.

        Args:
            contacto: Objeto contacto a insertar.
        """
        if not self.raiz:
            self.raiz = Nodo(contacto)
        else:
            self._insertar(self.raiz, contacto)

    def _insertar(self, nodo_actual, contacto):
        """
        Inserta recursivamente el contacto en el lugar correcto.

        Args:
            nodo_actual: Nodo donde se está insertando.
            contacto: Contacto a insertar.
        """
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
        """
        Busca un contacto por nombre.

        Args:
            nombre: Nombre del contacto a buscar.

        Returns:
            El contacto encontrado o None si no existe.
        """
        return self._buscar(self.raiz, nombre.lower())

    def _buscar(self, nodo_actual, nombre):
        """
        Busca recursivamente un contacto en el árbol.

        Args:
            nodo_actual: Nodo actual del árbol.
            nombre: Nombre a buscar.

        Returns:
            Contacto encontrado o None.
        """
        if nodo_actual is None:
            return None
        if nombre == nodo_actual.contacto.nombre.lower():
            return nodo_actual.contacto
        elif nombre < nodo_actual.contacto.nombre.lower():
            return self._buscar(nodo_actual.izquierda, nombre)
        else:
            return self._buscar(nodo_actual.derecha, nombre)

    def eliminar(self, nombre):
        """
        Elimina un contacto por nombre del árbol.

        Args:
            nombre: Nombre del contacto a eliminar.
        """
        self.raiz = self._eliminar(self.raiz, nombre.lower())

    def _eliminar(self, nodo_actual, nombre):
        """
        Elimina recursivamente el nodo con el nombre dado.

        Args:
            nodo_actual: Nodo actual del árbol.
            nombre: Nombre a eliminar.

        Returns:
            Nodo actualizado después de la eliminación.
        """
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
        """
        Encuentra el nodo con el valor mínimo en el subárbol dado.

        Args:
            nodo: Nodo raíz del subárbol.

        Returns:
            Nodo con el valor mínimo.
        """
        current = nodo
        while current.izquierda:
            current = current.izquierda
        return current

    def listar(self):
        """
        Devuelve una lista con todos los contactos en orden alfabético.

        Returns:
            Lista de contactos en orden.
        """
        contactos = []
        self._inorden(self.raiz, contactos)
        return contactos

    def _inorden(self, nodo_actual, lista):
        """
        Recorrido inorden para llenar la lista de contactos.

        Args:
            nodo_actual: Nodo actual del árbol.
            lista: Lista donde se almacenan los contactos.
        """
        if nodo_actual:
            self._inorden(nodo_actual.izquierda, lista)
            lista.append(nodo_actual.contacto.to_dict())
            self._inorden(nodo_actual.derecha, lista)
