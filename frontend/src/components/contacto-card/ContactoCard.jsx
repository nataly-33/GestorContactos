import React from "react";
import "./contacto-card.css";

const ContactCard = ({ contacto, onEditar, onEliminar }) => {
  return (
    <div className="cartilla" >
      <img
      src={contacto.imagen}
      alt={contacto.nombre}/>
      <div className="lado-izq">
        <h3>{contacto.nombre}</h3>
        <p><strong>Teléfono:  </strong> {contacto.telefono}</p>
        <p><strong>Email:  </strong>{contacto.correo}</p>
        <button className="eliminar-cartilla"onClick={() => onEliminar(contacto.nombre)}>Eliminar</button>
      </div>
    </div>
  );
};

export default ContactCard;
