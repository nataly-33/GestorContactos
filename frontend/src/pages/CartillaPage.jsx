// src/pages/CartillaPage.js
import React, { useEffect, useState } from "react";
import ContactCard from "../components/contacto-card/ContactoCard";
import "./cartilla-page.css";

const CartillaPage = () => {
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
    // Aquí puedes abrir un modal o navegar a edición
    console.log("Editar", contacto);
  };

  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        gap: "1rem",
        padding: "1rem",
      }}
    >
      <h2>Contactos - Modo Tarjetas</h2>
      {contactos.map((contacto, index) => (
        <ContactCard
          key={index}
          contacto={contacto}
          onEditar={handleEditar}
          onEliminar={handleEliminar}
        />
      ))}
    </div>
  );
};

export default CartillaPage;
