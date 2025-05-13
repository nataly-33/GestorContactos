import "./match-card.css";

const MatchCard = ({ teamA, teamB, scoreA, scoreB, onResultSubmit }) => {
  return (
    <div className="match-card">
      <div className="team">
        <img src={teamA.logo} alt={teamA.name} className="team-logo" />
        <span className="team-name">{teamA.name}</span>
      </div>

      <div className="match-score">
        <input
          type="number"
          min="0"
          value={scoreA}
          onChange={(e) => onResultSubmit("A", parseInt(e.target.value) || 0)}
          className="score-input"
        />
        <span className="score-separator">-</span>
        <input
          type="number"
          min="0"
          value={scoreB}
          onChange={(e) => onResultSubmit("B", parseInt(e.target.value) || 0)}
          className="score-input"
        />
      </div>

      <div className="team">
        <img src={teamB.logo} alt={teamB.name} className="team-logo" />
        <span className="team-name">{teamB.name}</span>
      </div>
    </div>
  );
};

export default MatchCard;
