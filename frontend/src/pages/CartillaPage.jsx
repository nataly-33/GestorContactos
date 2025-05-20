import React, { useEffect, useState } from "react";
import ContactCard from "../components/contacto-card/ContactoCard";
import "./cartilla-page.css";

const CartillaPage = () => {
  const [contactos, setContactos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/lista")
      .then((res) => res.json())
      .then((data) => setContactos(data));
  }, []);

  const handleEliminar = (nombre) => {
    fetch(`http://localhost:5000/eliminar/${nombre}`, {
      method: "DELETE",
    }).then(() => setContactos(contactos.filter((c) => c.nombre !== nombre)));
  };

  const handleEditar = (contacto) => {
    console.log("Editar", contacto);
  };

  return (
    <div className="cartilla-contenedor" >
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
