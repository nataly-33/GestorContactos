import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ListaPage from "./pages/ListaPage";
import CartillaPage from "./pages/CartillaPage";
import NuevoContactoPage from "./pages/NewContactoPage";
import Header from "./components/header/Header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<ListaPage />} />
        <Route path="/cartilla" element={<CartillaPage />} />
        <Route path="/nuevo" element={<NuevoContactoPage />} />
      </Routes>
    </Router>
  );
}

export default App;
