// src/components/ContactForm.js
import React, { useState } from "react";
import "./contacto-form.css";

const ContactForm = ({ onSubmit, initialData = {} }) => {
  const [nombre, setNombre] = useState(initialData.nombre || "");
  const [telefono, setTelefono] = useState(initialData.telefono || "");
  const [correo, setCorreo] = useState(initialData.correo || "");
  const [imagen, setImagen] = useState(initialData.imagen || null);
  const [imagenPreview, setImagenPreview] = useState(initialData.imagen || "");

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setImagen(e.target.result); // Imagen en Base64
        setImagenPreview(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const contacto = { nombre, telefono, correo, imagen };
    onSubmit(contacto);
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: "flex", flexDirection: "column", gap: "1rem" }}
    >
      <input
        type="text"
        placeholder="Nombre completo"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        required
      />
      <input
        type="tel"
        placeholder="Teléfono (8 dígitos)"
        value={telefono}
        onChange={(e) => setTelefono(e.target.value)}
        required
      />
      <input
        type="email"
        placeholder="Correo electrónico"
        value={correo}
        onChange={(e) => setCorreo(e.target.value)}
        required
      />

      <label>
        Imagen:
        <input type="file" accept="image/*" onChange={handleImageChange} />
      </label>

      <img
        src={imagenPreview || "default.jpg"}
        alt="Vista previa"
        style={{ width: "100px", height: "100px", objectFit: "cover" }}
      />

      <button type="submit">Guardar Contacto</button>
    </form>
  );
};

export default ContactForm;
