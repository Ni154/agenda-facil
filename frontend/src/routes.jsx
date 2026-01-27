import { createBrowserRouter } from 'react-router-dom'
import Layout from './components/Layout'

import Dashboard from './pages/Dashboard'
import Clientes from './pages/Clientes'
import Produtos from './pages/Produtos'
import Servicos from './pages/Servicos'
import Agendamentos from './pages/Agendamentos'
import Vendas from './pages/Vendas'
import Despesas from './pages/Despesas'
import Relatorios from './pages/Relatorios'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: 'clientes', element: <Clientes /> },
      { path: 'produtos', element: <Produtos /> },
      { path: 'servicos', element: <Servicos /> },
      { path: 'agendamentos', element: <Agendamentos /> },
      { path: 'vendas', element: <Vendas /> },
      { path: 'despesas', element: <Despesas /> },
      { path: 'relatorios', element: <Relatorios /> },
    ],
  },
])

export default router
