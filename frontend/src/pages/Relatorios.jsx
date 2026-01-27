import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Relatorios() {
  const [relatorios, setRelatorios] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    carregarRelatorios();
  }, []);

  async function carregarRelatorios() {
    try {
      setLoading(true);
      const response = await api.get("/relatorios");
      setRelatorios(response.data || []);
    } catch (error) {
      console.error("Erro ao carregar relatórios:", error);
      alert("Erro ao carregar relatórios");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Layout>
      <h2>Relatórios</h2>

      {loading && <p>Carregando...</p>}

      {!loading && (
        <ul>
          {relatorios.map((relatorio, index) => (
            <li key={relatorio._id || relatorio.id || index}>
              {relatorio.nome || "Relatório"}
            </li>
          ))}
        </ul>
      )}
    </Layout>
  );
}

export default Relatorios;
