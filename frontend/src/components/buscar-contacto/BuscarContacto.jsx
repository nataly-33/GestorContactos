import React, { useState } from 'react';
import axios from 'axios';
import { FaSearch } from "react-icons/fa";
import './buscar-contacto.css';

const BuscadorContacto = ({ onBuscar }) => {
  const [nombre, setNombre] = useState('');

  const handleBuscar = async (e) => {
    e.preventDefault();

    const valor = nombre.trim();

    if (valor === '') {
      try {
        const res = await axios.get('http://localhost:5000/listar');
        onBuscar(res.data); 
      } catch (error) {
        console.error('Error al cargar contactos:', error);
      }
      return;
    }

    try {
      const res = await axios.get(`http://localhost:5000/buscar/${valor}`);
      if (res.data.mensaje === 'Contacto no encontrado') {
        alert('No se encontró ningún contacto con ese nombre');
        onBuscar([]); 
      } else {
        onBuscar([res.data]); 
      }
    } catch (error) {
      console.error('Error al buscar contacto:', error);
    }
  };

  return (
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
  );
};

export default BuscadorContacto;
