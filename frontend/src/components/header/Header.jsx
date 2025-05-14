import React from "react";
import { Link } from "react-router-dom";
import "./header.css/";

const Header = () => {
  return (
    <header
      style={{ padding: "1rem", backgroundColor: "#282c34", color: "white" }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
          {/* Aquí puedes poner un logo */}
          <h1>Gestor de Contactos</h1>
          <nav>
            <Link to="/lista">Lista</Link> |<Link to="/cartilla">Cartilla</Link>
          </nav>
        </div>
        <Link to="/nuevo">
          <button style={{ padding: "0.5rem 1rem" }}>Registrar Nuevo</button>
        </Link>
      </div>
    </header>
  );
};

export default Header;
