import {Routes, Route} from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import AuthPage from './pages/AuthPage'
import ResetPage from './pages/ResetPage'
import Home from './pages/Home'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<LandingPage/>}/>
        <Route path='/signin' element={<AuthPage/>}/>
        <Route path='/signup' element={<AuthPage/>}/>
        <Route path='/reset' element={<ResetPage/>}/>
        <Route path='/home' element={<Home/>}/>


      </Routes>
    </>
  )
}

export default App
