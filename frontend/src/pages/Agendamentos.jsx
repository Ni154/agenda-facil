import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Agendamentos() {
  const [agendamentos, setAgendamentos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    carregarAgendamentos();
  }, []);

  async function carregarAgendamentos() {
    try {
      setLoading(true);
      const response = await api.get("/agendamentos");
      setAgendamentos(response.data || []);
    } catch (error) {
      console.error("Erro ao carregar agendamentos:", error);
      alert("Erro ao carregar agendamentos");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Layout>
      <h2>Agendamentos</h2>

      {loading && <p>Carregando...</p>}

      {!loading && (
        <ul>
          {agendamentos.map((agendamento) => (
            <li key={agendamento._id || agendamento.id}>
              {agendamento.descricao || "Agendamento"}
            </li>
          ))}
        </ul>
      )}
    </Layout>
  );
}

export default Agendamentos;
