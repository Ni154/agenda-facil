import React from 'react'
import { Outlet } from 'react-router-dom'

export default function Layout() {
  return (
    <div>
      {/* aqui pode ficar seu menu / header / sidebar */}
      
      <main>
        <Outlet />
      </main>
    </div>
  )
}
