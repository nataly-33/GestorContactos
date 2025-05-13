import React, { useState } from "react";
import TournamentBracket from "../../src/components/TournamentBracket/TournamentBracket";
import MatchCard from "../../src/components/MatchCard/MatchCard";
import defaultLogo from "./default-logo.png"; // Importamos la imagen local
import "./home-page.css";

const HomePage = () => {
  const [matches, setMatches] = useState([]);
  const [results, setResults] = useState([]);

  const handleAddResult = (matchId, scoreA, scoreB) => {
    const updatedMatches = matches.map((match) =>
      match.id === matchId ? { ...match, scoreA, scoreB } : match
    );
    setMatches(updatedMatches);
    setResults([...results, { matchId, scoreA, scoreB }]);
  };

  // Simulación: cuando tengamos equipos registrados, crearemos los partidos
  const generateInitialMatches = (teams) => {
    if (teams.length < 2) return;
    const newMatches = [];
    for (let i = 0; i < teams.length; i += 2) {
      if (teams[i + 1]) {
        newMatches.push({
          id: i / 2 + 1,
          teamA: teams[i],
          teamB: teams[i + 1],
          scoreA: 0,
          scoreB: 0,
        });
      }
    }
    setMatches(newMatches);
  };

  // ⚡ Simulación de equipos registrados
  const sampleTeams = [
    { name: "Equipo A", logo: defaultLogo },
    { name: "Equipo B", logo: defaultLogo },
    { name: "Equipo C", logo: defaultLogo },
    { name: "Equipo D", logo: defaultLogo },
  ];

  // ⚡ Solo para esta demo: generar partidos automáticos
  React.useEffect(() => {
    generateInitialMatches(sampleTeams);
  }, []);

  return (
    <div className="home-page">
      <h1 className="title">Torneo de Fútbol</h1>
      <TournamentBracket matches={matches} />
      <h2 className="subtitle">Registrar Resultado</h2>
      <div className="matches-container">
        {matches.map((match) => (
          <MatchCard
            key={match.id}
            match={match}
            onAddResult={handleAddResult}
          />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
