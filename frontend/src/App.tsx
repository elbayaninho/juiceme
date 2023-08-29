import {Routes, Route} from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import AuthPage from './pages/AuthPage'
import ResetPage from './pages/ResetPage'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<LandingPage/>}/>
        <Route path='/signin' element={<AuthPage/>}/>
        <Route path='/signup' element={<AuthPage/>}/>
        <Route path='/reset' element={<ResetPage/>}/>

      </Routes>
    </>
  )
}

export default App
