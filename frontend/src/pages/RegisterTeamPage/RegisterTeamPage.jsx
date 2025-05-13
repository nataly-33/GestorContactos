import React, { useState } from "react";
import TeamFormModal from "./TeamFormModal"; // Importa el modal
import "./RegisterTeamPage.css";

const RegisterTeamPage = () => {
  const [teams, setTeams] = useState([]); // Estado para almacenar los equipos
  const [isModalOpen, setIsModalOpen] = useState(false); // Estado para abrir y cerrar el modal

  // Función para abrir el modal
  const openModal = () => setIsModalOpen(true);

  // Función para cerrar el modal
  const closeModal = () => setIsModalOpen(false);

  // Función para agregar un nuevo equipo
  const addTeam = (newTeam) => {
    setTeams([...teams, newTeam]);
  };

  return (
    <div className="register-team-page">
      <h1>Registrar Equipos</h1>

      <button onClick={openModal} className="add-team-btn">
        Agregar Equipo
      </button>

      {/* Mostrar el modal si isModalOpen es true */}
      {isModalOpen && (
        <TeamFormModal addTeam={addTeam} closeModal={closeModal} />
      )}

      {/* Mostrar lista de equipos registrados */}
      <div className="team-list">
        <h2>Equipos Registrados</h2>
        <ul>
          {teams.map((team, index) => (
            <li key={index}>
              <img src={team.logo} alt={`${team.name} Logo`} width="50" />
              <span>{team.name}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default RegisterTeamPage;
