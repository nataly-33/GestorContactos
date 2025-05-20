import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaSearch } from "react-icons/fa";
import './buscar-contacto.css';

const BuscadorContacto = ({ onBuscar }) => {
  const [nombre, setNombre] = useState('');
  const [mensajeError, setMensajeError] = useState('');

  useEffect(() => {
    const cargarContactos = async () => {
      try {
        const res = await axios.get('http://localhost:5000/lista');
        onBuscar(res.data);
        setMensajeError('');
      } catch (error) {
        console.error('Error al cargar contactos:', error);
        setMensajeError('No se pudo cargar la lista de contactos.');
      }
    };

    cargarContactos();
  }, []); 

  const handleBuscar = async (e) => {
    e.preventDefault();
    const valor = nombre.trim();

    if (valor === '') {
      try {
        const res = await axios.get('http://localhost:5000/lista');
        onBuscar(res.data);
        setMensajeError('');
      } catch (error) {
        console.error('Error al cargar contactos:', error);
        setMensajeError('No se pudo cargar la lista de contactos.');
      }
      return;
    }

    try {
      const res = await axios.get(`http://localhost:5000/buscar/${valor}`);
      if (res.data.mensaje === 'Contacto no encontrado') {
        setMensajeError('El nombre no está en la lista');
        onBuscar([]);
      } else {
        setMensajeError('');
        onBuscar([res.data]);
      }
    } catch (error) {
      console.error('Error al buscar contacto:', error);
      setMensajeError('Error al buscar el contacto.');
    }
  };

  return (
    <div>
      <form className="buscador-form" onSubmit={handleBuscar}>
        <input
          type="text"
          placeholder="nombre..."
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
        />
        <button type="submit" className="btn-buscar" title="Buscar">
          <FaSearch size={30} />
        </button>
      </form>

      {mensajeError && (
        <p className="mensaje-error">{mensajeError}</p>
      )}
    </div>
  );
};

export default BuscadorContacto;
