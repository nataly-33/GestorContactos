// src/pages/ListaPage.js
import React, { useEffect, useState } from "react";
import ContactList from "../components/contacto-lista/ContactoLista";
import "./lista-page.css";

const ListaPage = () => {
  const [contactos, setContactos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/listar")
      .then((res) => res.json())
      .then((data) => setContactos(data));
  }, []);

  const handleEliminar = (nombre) => {
    fetch(`http://localhost:5000/eliminar/${nombre}`, {
      method: "DELETE",
    }).then(() => setContactos(contactos.filter((c) => c.nombre !== nombre)));
  };

  const handleEditar = (contacto) => {
    // Aquí puedes abrir un modal o navegar a la página de edición
    console.log("Editar", contacto);
  };

  return (
    <div>
      <h2>Contactos - Modo Lista</h2>
      <ContactList
        contactos={contactos}
        onEditar={handleEditar}
        onEliminar={handleEliminar}
      />
    </div>
  );
};

export default ListaPage;
