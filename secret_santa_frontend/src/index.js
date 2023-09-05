import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter} from "react-router-dom";
import {Toaster} from "react-hot-toast";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <BrowserRouter>
        <React.StrictMode>
            <Toaster reverseOrder={true}/>
            <App />
        </React.StrictMode>
    </BrowserRouter>
);

reportWebVitals();
