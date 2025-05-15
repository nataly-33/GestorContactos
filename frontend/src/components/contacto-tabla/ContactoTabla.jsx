import React from 'react';
import "./contacto-tabla.css"

const ContactoTabla = ({ contactos, onEliminar }) => {
  return (
    <table className="tabla-contactos">
      <colgroup>
        <col style={{ width: "15%" }} />
        <col style={{ width: "25%" }}/>
        <col style={{ width: "20%" }} />
        <col style={{ width: "25%" }}/>
        <col style={{ width: "15%" }}/>
      </colgroup>
      <thead>
        <tr>
          <th>Perfil</th>
          <th>Nombre</th>
          <th>Teléfono</th>
          <th>Correo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        {contactos.map((contacto, index) => (
          <tr key={index}>
            <td className="perfil">
              <img
                src={contacto.imagen}
                alt={contacto.nombre}
                style={{
                  width: '40px',
                  height: '40px',
                  borderRadius: '50%',
                  objectFit: 'cover'
                }}
              />
            </td>
            <td>{contacto.nombre}</td>
            <td className="centrado">{contacto.telefono}</td>
            <td>{contacto.correo}</td>
            <td className="centrado">
              <button className="btn-eliminar" onClick={() => onEliminar(contacto.nombre)}>
                Eliminar
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default ContactoTabla;