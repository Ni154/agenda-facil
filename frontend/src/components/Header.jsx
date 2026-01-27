import React from "react";

const headerStyle = {
  background: "#f9fafb",
  padding: "12px 16px",
  borderBottom: "1px solid #e5e7eb",
  marginBottom: "16px"
};

function Header() {
  return (
    <header style={headerStyle}>
      <h1>Sistema Agenda Fácil</h1>
    </header>
  );
}

export default Header;
