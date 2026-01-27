import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Servicos() {
  const [servicos, setServicos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    carregarServicos();
  }, []);

  async function carregarServicos() {
    try {
      setLoading(true);
      const response = await api.get("/servicos");
      setServicos(response.data || []);
    } catch (error) {
      console.error("Erro ao carregar serviços:", error);
      alert("Erro ao carregar serviços");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Layout>
      <h2>Serviços</h2>

      {loading && <p>Carregando...</p>}

      {!loading && (
        <ul>
          {servicos.map((servico) => (
            <li key={servico._id || servico.id}>
              {servico.nome}
            </li>
          ))}
        </ul>
      )}
    </Layout>
  );
}

export default Servicos;
