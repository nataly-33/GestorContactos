import "./tournament-bracket.css";

const TournamentBracket = ({ rounds, onSetResult }) => {
  return (
    <div className="bracket-container">
      {rounds.map((round, roundIndex) => (
        <div key={roundIndex} className="round">
          <h3>Ronda {roundIndex + 1}</h3>
          {round.map((match, matchIndex) => (
            <div key={matchIndex} className="match">
              <div className="team">
                {match.teamA ? match.teamA : "Pendiente"}
              </div>
              <div className="vs">VS</div>
              <div className="team">
                {match.teamB ? match.teamB : "Pendiente"}
              </div>
              {match.teamA && match.teamB && (
                <button
                  className="set-result-button"
                  onClick={() => onSetResult(roundIndex, matchIndex)}
                >
                  Ingresar Resultado
                </button>
              )}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default TournamentBracket;
