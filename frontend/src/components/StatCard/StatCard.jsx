import "./stat-card.css";

const StatCard = ({ title, players }) => {
  return (
    <div className="stat-card">
      <h2 className="stat-card-title">{title}</h2>
      <ul className="stat-card-list">
        {players.map((player, index) => (
          <li key={index} className="stat-card-item">
            <span className="player-name">{player.name}</span> —{" "}
            <span className="player-stat">{player.value}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StatCard;
