import React, { useEffect, useState } from 'react';
import ContactoTabla from '../components/contacto-tabla/ContactoTabla';
import BuscadorContacto from '../components/buscar-contacto/BuscarContacto';
import axios from 'axios';
import "./lista-page.css"

const ListaPage = () => {
  const [contactos, setContactos] = useState([]);

  const cargarContactos = async () => {
    try {
      const res = await axios.get('http://localhost:5000/lista');
      setContactos(res.data);
    } catch (error) {
      console.error('Error al cargar contactos:', error);
    }
  };

  useEffect(() => {
    cargarContactos();
  }, []);

  const handleEliminar = async (nombre) => {
    try {
      await axios.delete(`http://localhost:5000/eliminar/${nombre}`);
      cargarContactos(); 
    } catch (error) {
      console.error('Error al eliminar:', error);
    }
  };

  const handleBuscar = (resultado) => {
    if (resultado && resultado.length > 0) {
      setContactos(resultado); 
    } else {
      cargarContactos(); 
    }
  };

  return (
    <div className="lista-page">
      <BuscadorContacto onBuscar={handleBuscar} />
      <ContactoTabla contactos={contactos} onEliminar={handleEliminar} />
    </div>
  );
};

export default ListaPage;
