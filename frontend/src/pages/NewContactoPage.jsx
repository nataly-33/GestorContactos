import React from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import ContactoForm from "../components/contacto-form/ContactoForm";

const NuevoContactoPage = () => {
  const navigate = useNavigate();

  const handleSubmit = async (contacto) => {
    try {
      await axios.post("http://localhost:5000/crear", contacto);
      navigate("/"); 
      
    } catch (error) {
      console.error("Error al crear contacto:", error);
      alert("Hubo un error al crear el contacto.");
    }
  };

  return (
      <ContactoForm onSubmit={handleSubmit} />
  );
};

export default NuevoContactoPage;

