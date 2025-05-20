import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { IoClose } from "react-icons/io5";
import "./contacto-form.css";

const ContactoForm = ({ onSubmit, initialData = {} }) => {
  const navigate = useNavigate();

  const [nombre, setNombre] = useState(initialData.nombre || "");
  const [telefono, setTelefono] = useState(initialData.telefono || "");
  const [correo, setCorreo] = useState(initialData.correo || "");
  const [imagen, setImagen] = useState(initialData.imagen || null);
  const [imagenPreview, setImagenPreview] = useState(initialData.imagen || "/perfil-default.png");

  const [telefonoError, setTelefonoError] = useState(""); 

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setImagen(e.target.result); 
        setImagenPreview(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const validarTelefono = (numero) => {
    const regex = /^[67]\d{7}$/; 
    return regex.test(numero);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!validarTelefono(telefono)) {
      setTelefonoError("El número debe tener 8 dígitos y comenzar con 6 o 7");
      return; 
    } else {
      setTelefonoError(""); 
    }

    let imagenFinal = imagen;
    if (!imagenFinal) {
      imagenFinal = "/perfil-default.png";
      setImagenPreview(imagenFinal);
    }

    const contacto = { nombre, telefono, correo, imagen: imagenFinal };
    onSubmit(contacto);
  };

  const handleCancel = () => {
    navigate("/");
  };

  return (
    <form onSubmit={handleSubmit} className="contacto-form">
      <div className="close-button" onClick={handleCancel}>
        <IoClose size={35} />
      </div>
      <div className="contacto-row">
        <label className="label-input">Nombre completo</label>
        <input
          type="text"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          required
        />
      </div>

      <div className="contacto-row">
        <label className="label-input">Celular</label>
        <input
          type="text" 
          value={telefono}
          onChange={(e) => setTelefono(e.target.value)}
          className={telefonoError ? "input-error" : ""}
          required
        />
        {telefonoError && <p className="error-text">{telefonoError}</p>}
      </div>

      <div className="contacto-row">
        <label className="label-input">Correo electrónico</label>
        <input
          type="email"
          value={correo}
          onChange={(e) => setCorreo(e.target.value)}
          required
        />
      </div>

      <div className="contacto-row">
        <label className="label-input">Imagen</label>
        <label>
          <input type="file" accept="image/*" onChange={handleImageChange} />
        </label>
      </div>

      <img
        src={imagenPreview || "default.jpg"}
        alt="Vista previa"
        style={{ width: "100px", height: "100px", objectFit: "cover" }}
      />

      <button type="submit" className="button-guardar">Guardar Contacto</button>
    </form>
  );
};

export default ContactoForm;
