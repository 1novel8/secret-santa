import {useEffect, useState} from "react";
import Modal from "../components/Modal";
import LoginForm from "../components/LoginForm";
import RegisterForm from "../components/RegisterForm";
import "../css/general.css"
import "../css/homepage.css"
import {Navigate, useSearchParams} from "react-router-dom";
import PartyPage from "./PartyPage";

function HomePage({isLoggedIn, setIsLoggedIn}){
    const [authModalActive, setAuthModalActive] = useState(false);
    const [registerForm, setRegisterForm] = useState(false);
    const [searchParams, setSearchParams] = useSearchParams();
    const token = searchParams.get('token')
    const onCreatePartyClick = (event) =>{
        event.preventDefault();
        if(isLoggedIn === false) {
            setAuthModalActive(true);
        } else {
            return <Navigate to="party"/>;
        }
    }
    useEffect(() => {
        if (token !== null) {
            setRegisterForm(true);
            setAuthModalActive(true);
        }
    },[]);
    return(
        <div >
            <main>
                <h1 className="big-text">Тайный санта</h1>
                <p className="filler">Тайный Санта - это веселая загадка в стиле подарков! Все выбирают получателя подарка и становятся настоящими шерлоками, скрывая свои следы. Когда подарок найден, волшебство начинается! Этот дружелюбный обмен подарками полон улыбок, намеков и радостных сюрпризов. Подарите себе и другим дозу загадочного веселья с Тайным Сантой!</p>
                <button className="oval-button" onClick={onCreatePartyClick}>Создать группу</button>
            </main>
            <Modal active={authModalActive} setActive={setAuthModalActive}>
                {registerForm ?
                    <div>
                        <RegisterForm token={token} setRegisterForm={setRegisterForm}></RegisterForm>
                        <button onClick={() =>{setRegisterForm(false)}}>
                            У меня уже есть аккунт</button>
                    </div>
                    :
                    <div>
                        <LoginForm
                        setAuthModalActive={setAuthModalActive}
                        setIsLoggedIn={setIsLoggedIn}/>
                        <button onClick={() =>{setRegisterForm(true)}}>
                            У меня нет аккунта</button>
                    </div>
                }
            </Modal>
        </div>
    )
}

export default HomePage;
