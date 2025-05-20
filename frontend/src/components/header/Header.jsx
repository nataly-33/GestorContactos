import React from "react";
import { Link } from "react-router-dom";
import { RiContactsBook3Line } from "react-icons/ri";
import "./header.css/";

const Header = () => {
  return (
    <header className="header-principal"  >
        <div className="logo-titulo">
          <RiContactsBook3Line  size={45} />
          <h1>CONTACTOS</h1>
        </div>
        <nav className="nav-links">
          <Link to="/">Lista</Link>
          <Link to="/cartilla">Cartilla</Link>
        </nav>
        <Link to="/nuevo">
          <button className="button-registrar">Registrar</button>
        </Link>
      </header>
  );
};

export default Header;
