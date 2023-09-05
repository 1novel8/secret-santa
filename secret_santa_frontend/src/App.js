import {
  Routes,
  Route,
} from 'react-router-dom';
import {useState} from "react";

import NotFoundPage from "./pages/NotFoundPage";
import HomePage from "./pages/HomePage"
import Layout from "./components/Layout";

import storage from "./utils/storage";
import {axiosInstance} from "./utils/axios";
import PartyPage from "./pages/PartyPage";

function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(storage.getToken() !== null);
    const tokenVerify = () => {
        axiosInstance.post()
    }
      return (
          <div>
            <Routes>
                <Route path='/' element= {<Layout/>}>
                    <Route path='/' element= {<HomePage isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn}/>}/>
                    <Route path='party/' element= {<PartyPage isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn}/>}/>
                    <Route path='*' element = {<NotFoundPage/>}/>
                </Route>
            </Routes>
          </div>
      );
}

export default App;
