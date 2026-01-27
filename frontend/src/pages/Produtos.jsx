import React, { useEffect, useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Produtos() {
  const [produtos, setProdutos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    carregarProdutos();
  }, []);

  async function carregarProdutos() {
    try {
      setLoading(true);
      const response = await api.get("/produtos");
      setProdutos(response.data || []);
    } catch (error) {
      console.error("Erro ao carregar produtos:", error);
      alert("Erro ao carregar produtos");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Layout>
      <h2>Produtos</h2>

      {loading && <p>Carregando...</p>}

      {!loading && (
        <ul>
          {produtos.map((produto) => (
            <li key={produto._id || produto.id}>
              {produto.nome}
            </li>
          ))}
        </ul>
      )}
    </Layout>
  );
}

export default Produtos;
