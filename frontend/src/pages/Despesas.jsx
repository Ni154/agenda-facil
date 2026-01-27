import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Despesas() {
  const [despesas, setDespesas] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    carregarDespesas();
  }, []);

  async function carregarDespesas() {
    try {
      setLoading(true);
      const response = await api.get("/despesas");
      setDespesas(response.data || []);
    } catch (error) {
      console.error("Erro ao carregar despesas:", error);
      alert("Erro ao carregar despesas");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Layout>
      <h2>Despesas</h2>

      {loading && <p>Carregando...</p>}

      {!loading && (
        <ul>
          {despesas.map((despesa) => (
            <li key={despesa._id || despesa.id}>
              {despesa.descricao || "Despesa"} —{" "}
              {despesa.valor != null ? `R$ ${despesa.valor}` : ""}
            </li>
          ))}
        </ul>
      )}
    </Layout>
  );
}

export default Despesas;
