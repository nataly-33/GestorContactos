import { useState } from "react";
import "./team-form-modal.css";

const TeamFormModal = ({ onClose, onSubmit }) => {
  const [teamName, setTeamName] = useState("");
  const [coachName, setCoachName] = useState("");
  const [participantCount, setParticipantCount] = useState(1);
  const [participants, setParticipants] = useState([""]);
  const [teamImage, setTeamImage] = useState(null);

  const handleParticipantChange = (index, value) => {
    const updatedParticipants = [...participants];
    updatedParticipants[index] = value;
    setParticipants(updatedParticipants);
  };

  const handleParticipantCountChange = (count) => {
    const newCount = parseInt(count, 10);
    setParticipantCount(newCount);

    if (newCount > participants.length) {
      setParticipants([
        ...participants,
        ...Array(newCount - participants.length).fill(""),
      ]);
    } else {
      setParticipants(participants.slice(0, newCount));
    }
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setTeamImage(file);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const teamData = {
      teamName,
      coachName,
      participants,
      teamImage,
    };
    onSubmit(teamData);
    onClose();
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Registrar Nuevo Equipo</h2>
        <form onSubmit={handleSubmit} className="team-form">
          <input
            type="text"
            placeholder="Nombre del equipo"
            value={teamName}
            onChange={(e) => setTeamName(e.target.value)}
            required
          />

          <input
            type="text"
            placeholder="Nombre del director técnico"
            value={coachName}
            onChange={(e) => setCoachName(e.target.value)}
            required
          />

          <input
            type="number"
            min="1"
            placeholder="Cantidad de participantes"
            value={participantCount}
            onChange={(e) => handleParticipantCountChange(e.target.value)}
            required
          />

          {participants.map((participant, index) => (
            <input
              key={index}
              type="text"
              placeholder={`Participante ${index + 1}`}
              value={participant}
              onChange={(e) => handleParticipantChange(index, e.target.value)}
              required
            />
          ))}

          <div className="upload-section">
            <label htmlFor="team-image">Foto del equipo (opcional)</label>
            <input
              id="team-image"
              type="file"
              accept="image/*"
              onChange={handleImageChange}
            />
          </div>

          <div className="modal-buttons">
            <button type="submit" className="btn-submit">
              Registrar
            </button>
            <button type="button" onClick={onClose} className="btn-cancel">
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TeamFormModal;
