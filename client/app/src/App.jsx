import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Inicio do projeto</h1>
      <div>
        <form action="#" method="post">
          <label htmlFor="nome">Nome completo</label>
          <input type="text" name="nome" id='nome' placeholder='Digite seu nome...' min='3' />
          <br />
          <label htmlFor="fone">Telefone de contato</label>
          <input type="text" name='fone' id='fone' placeholder='numero de telefone...' />
          <br />
          <button>Enviar</button>
        </form>
      </div>
    </>
  )
}

export default App
