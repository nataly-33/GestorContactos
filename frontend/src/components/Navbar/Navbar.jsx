import { Link } from "react-router-dom";
import "./navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-logo">TorneoApp</div>
        <ul className="navbar-links">
          <li>
            <Link to="/">Inicio</Link>
          </li>
          <li>
            <Link to="/register-team">Registrar Equipo</Link>
          </li>
          <li>
            <Link to="/stats">Estadísticas</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
