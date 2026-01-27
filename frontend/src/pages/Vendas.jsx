import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Vendas() {
  const [vendas, setVendas] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    carregarVendas();
  }, []);

  async function carregarVendas() {
    try {
      setLoading(true);
      const response = await api.get("/vendas");
      setVendas(response.data || []);
    } catch (error) {
      console.error("Erro ao carregar vendas:", error);
      alert("Erro ao carregar vendas");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Layout>
      <h2>Vendas</h2>

      {loading && <p>Carregando...</p>}

      {!loading && (
        <ul>
          {vendas.map((venda) => (
            <li key={venda._id || venda.id}>
              {venda.descricao || "Venda"}
            </li>
          ))}
        </ul>
      )}
    </Layout>
  );
}

export default Vendas;
