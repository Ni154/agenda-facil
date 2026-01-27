import { useEffect, useState } from 'react'

export default function Clientes() {
  const [clientes, setClientes] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/clientes/')
      .then(res => res.json())
      .then(data => setClientes(data))
      .catch(err => console.error(err))
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h1>Clientes</h1>

      {clientes.length === 0 && <p>Nenhum cliente encontrado</p>}

      <ul>
        {clientes.map(c => (
          <li key={c.id}>{c.nome}</li>
        ))}
      </ul>
    </div>
  )
}
