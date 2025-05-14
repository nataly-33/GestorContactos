// src/pages/NuevoContactoPage.js
import React, { useState } from "react";
import ContactCard from "../components/contacto-card/ContactoCard";
import ContactForm from "../components/contacto-form/ContactoForm";
import "./new-contacto-page.css";

const NuevoContactoPage = () => {
  const handleSubmit = async (contacto) => {
    await fetch("http://localhost:5000/crear", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(contacto),
    });

    alert("Contacto creado");
    window.history.back(); // Regresa a la página anterior
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Crear Nuevo Contacto</h2>
      <ContactForm onSubmit={handleSubmit} />
    </div>
  );
};

export default NuevoContactoPage;
