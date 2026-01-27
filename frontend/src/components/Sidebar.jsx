import React from "react";
import { NavLink } from "react-router-dom";

const sidebarStyle = {
  width: "220px",
  background: "#1f2937",
  color: "#fff",
  padding: "16px"
};

const linkStyle = {
  display: "block",
  padding: "10px 0",
  color: "#fff",
  textDecoration: "none"
};

function Sidebar() {
  return (
    <aside style={sidebarStyle}>
      <h2>Agenda Fácil</h2>

      <nav>
        <NavLink to="/dashboard" style={linkStyle}>
          Dashboard
        </NavLink>
        <NavLink to="/clientes" style={linkStyle}>
          Clientes
        </NavLink>
        <NavLink to="/produtos" style={linkStyle}>
          Produtos
        </NavLink>
        <NavLink to="/servicos" style={linkStyle}>
          Serviços
        </NavLink>
        <NavLink to="/agendamentos" style={linkStyle}>
          Agendamentos
        </NavLink>
        <NavLink to="/vendas" style={linkStyle}>
          Vendas
        </NavLink>
        <NavLink to="/despesas" style={linkStyle}>
          Despesas
        </NavLink>
        <NavLink to="/relatorios" style={linkStyle}>
          Relatórios
        </NavLink>
      </nav>
    </aside>
  );
}

export default Sidebar;
