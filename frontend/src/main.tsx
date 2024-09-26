import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import {BrowserRouter} from 'react-router-dom'
import { MsalProvider } from "@azure/msal-react";
import { PublicClientApplication } from "@azure/msal-browser";
import { msalConfiguration } from './components/Shared/authConfig.ts'

const msalInstance = new PublicClientApplication(msalConfiguration);
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
    <MsalProvider instance={msalInstance}>
    <App />
    </MsalProvider>
    </BrowserRouter>
  </React.StrictMode>,
)
