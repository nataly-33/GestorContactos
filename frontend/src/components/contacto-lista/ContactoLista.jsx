// src/components/ContactList.js
import React from "react";
import "./contacto-lista.css";

const ContactList = ({ contactos, onEditar, onEliminar }) => {
  return (
    <ul style={{ listStyle: "none", paddingLeft: 0 }}>
      {contactos.map((contacto, index) => (
        <li
          key={index}
          style={{
            borderBottom: "1px solid #ccc",
            padding: "1rem",
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <div>
            <strong>{contacto.nombre}</strong>
            <br />
            <small>Tel: {contacto.telefono}</small>
            <br />
            <small>Email: {contacto.correo}</small>
          </div>
          <div>
            <button onClick={() => onEditar(contacto)}>Editar</button>
            <button onClick={() => onEliminar(contacto.nombre)}>
              Eliminar
            </button>
          </div>
        </li>
      ))}
    </ul>
  );
};

export default ContactList;
