import React from 'react'
import Login from './Login'
import Signup from './Signup'
import Home from './Home'
import {BrowserRouter,Routes,Route} from 'react-router-dom'
function App() {
  return (
     <BrowserRouter>
        <Routes>
             <Route path='/home' element={<Home />}></Route>
             <Route path='/signup' element={<Signup />}></Route>
             <Route path='/' element={<Login />}></Route>
        </Routes>
     </BrowserRouter>
  )
}

export default App