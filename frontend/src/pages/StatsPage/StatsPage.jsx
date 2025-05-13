import React, { useEffect, useState } from "react";
import StatCard from "../../components/StatCard/StatCard";
import "./stats-page.css";

const StatsPage = () => {
  const [topScorers, setTopScorers] = useState([]);
  const [topAssistants, setTopAssistants] = useState([]);
  const [topYellowCards, setTopYellowCards] = useState([]);
  const [topRedCards, setTopRedCards] = useState([]);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/stats");
      const data = await response.json();

      setTopScorers(data.topScorers);
      setTopAssistants(data.topAssistants);
      setTopYellowCards(data.topYellowCards);
      setTopRedCards(data.topRedCards);
    } catch (error) {
      console.error("Error al cargar estadísticas:", error);
    }
  };

  return (
    <div className="stats-page">
      <h1>Estadísticas del Torneo</h1>
      <div className="stats-section">
        <h2>Máximos Goleadores</h2>
        <div className="stat-cards">
          {topScorers.map((player, index) => (
            <StatCard
              key={index}
              title={player.nombre}
              value={`${player.goles} goles`}
            />
          ))}
        </div>
      </div>

      <div className="stats-section">
        <h2>Máximos Asistentes</h2>
        <div className="stat-cards">
          {topAssistants.map((player, index) => (
            <StatCard
              key={index}
              title={player.nombre}
              value={`${player.asistencias} asistencias`}
            />
          ))}
        </div>
      </div>

      <div className="stats-section">
        <h2>Más Tarjetas Amarillas</h2>
        <div className="stat-cards">
          {topYellowCards.map((player, index) => (
            <StatCard
              key={index}
              title={player.nombre}
              value={`${player.amarillas} amarillas`}
            />
          ))}
        </div>
      </div>

      <div className="stats-section">
        <h2>Más Tarjetas Rojas</h2>
        <div className="stat-cards">
          {topRedCards.map((player, index) => (
            <StatCard
              key={index}
              title={player.nombre}
              value={`${player.rojas} rojas`}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default StatsPage;
