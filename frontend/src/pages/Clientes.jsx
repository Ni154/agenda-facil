import { useEffect, useState } from "react";
import api from "../services/api";

export default function Clientes() {
  const [clientes, setClientes] = useState([]);
  const [nome, setNome] = useState("");

  useEffect(() => {
    carregarClientes();
  }, []);

  function carregarClientes() {
    api.get("/clientes").then((res) => {
      setClientes(res.data);
    });
  }

  function handleSubmit(e) {
    e.preventDefault();

    api.post("/clientes", { nome }).then(() => {
      setNome("");
      carregarClientes();
    });
  }

  return (
    <div>
      <h1>Clientes</h1>

      <form onSubmit={handleSubmit}>
        <input
          placeholder="Nome do cliente"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          required
        />
        <button type="submit">Cadastrar</button>
      </form>

      <ul>
        {clientes.map((c) => (
          <li key={c.id}>{c.nome}</li>
        ))}
      </ul>
    </div>
  );
}
