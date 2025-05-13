import React, { useState } from "react";
import "./team-formal-modal.css";

const TeamFormModal = ({ addTeam, closeModal }) => {
  const [teamName, setTeamName] = useState("");
  const [coach, setCoach] = useState("");
  const [players, setPlayers] = useState([]);
  const [playerInput, setPlayerInput] = useState("");
  const [logo, setLogo] = useState(null);

  const handleAddPlayer = () => {
    if (playerInput.trim() && players.length < 20) {
      setPlayers([...players, playerInput]);
      setPlayerInput("");
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (teamName && coach && players.length > 0) {
      const newTeam = {
        name: teamName,
        coach: coach,
        players: players,
        logo: logo ? URL.createObjectURL(logo) : "/default-logo.png",
      };
      addTeam(newTeam);
      closeModal();
    } else {
      alert("Por favor complete todos los campos.");
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal">
        <h2>Registrar Nuevo Equipo</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Nombre del equipo</label>
            <input
              type="text"
              value={teamName}
              onChange={(e) => setTeamName(e.target.value)}
              placeholder="Nombre del equipo"
              required
            />
          </div>

          <div className="form-group">
            <label>Director Técnico</label>
            <input
              type="text"
              value={coach}
              onChange={(e) => setCoach(e.target.value)}
              placeholder="Nombre del Director Técnico"
              required
            />
          </div>

          <div className="form-group">
            <label>Jugadores</label>
            <div className="player-input">
              <input
                type="text"
                value={playerInput}
                onChange={(e) => setPlayerInput(e.target.value)}
                placeholder="Agregar jugador"
              />
              <button type="button" onClick={handleAddPlayer}>
                Añadir Jugador
              </button>
            </div>
            <ul className="player-list">
              {players.map((player, index) => (
                <li key={index}>{player}</li>
              ))}
            </ul>
          </div>

          <div className="form-group">
            <label>Logo del equipo</label>
            <input
              type="file"
              onChange={(e) => setLogo(e.target.files[0])}
              accept="image/*"
            />
          </div>

          <div className="modal-footer">
            <button type="button" onClick={closeModal} className="cancel-btn">
              Cancelar
            </button>
            <button type="submit" className="submit-btn">
              Registrar Equipo
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TeamFormModal;
