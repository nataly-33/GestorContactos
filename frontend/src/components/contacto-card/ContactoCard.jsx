// src/components/ContactCard.js
import React from "react";
import "./contacto-card.css";

const ContactCard = ({ contacto, onEditar, onEliminar }) => {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "8px",
        padding: "1rem",
        textAlign: "center",
        width: "200px",
      }}
    >
      <img
        src={contacto.imagen || "default.jpg"}
        alt={contacto.nombre}
        style={{
          width: "100%",
          height: "150px",
          objectFit: "cover",
          borderRadius: "8px",
        }}
      />
      <h3>{contacto.nombre}</h3>
      <p>Teléfono: {contacto.telefono}</p>
      <p>Email: {contacto.correo}</p>
      <div>
        <button onClick={() => onEditar(contacto)}>Editar</button>
        <button onClick={() => onEliminar(contacto.nombre)}>Eliminar</button>
      </div>
    </div>
  );
};

export default ContactCard;
