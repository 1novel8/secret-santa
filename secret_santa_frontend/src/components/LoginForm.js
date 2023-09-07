import { useState} from "react";
import "../css/form.css"
import {axiosInstance} from "../utils/axios";
import storage from "../utils/storage";
import toast from "react-hot-toast";
import {LOGIN_URL} from "../utils/urls"

function LoginForm({setAuthModalActive, setIsLoggedIn}) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const onEmailChange = (event) => {
        setEmail(event.target.value);
    }
    const onPasswordChange = (event) => {
        setPassword(event.target.value);
    }
    const onSubmitLogin = (event) =>{
        event.preventDefault();
        logInUser(email, password)
    }

    const logInUser = (email, password) => {
        axiosInstance.post(
            LOGIN_URL,
            {
                'email': email,
                'password': password
            }
        ).then((response) => {
            storage.setToken(response.data['access']);
            storage.setRefreshToken(response.data['refresh']);
            setIsLoggedIn(true);
            setAuthModalActive(false);
            toast.success("Добро пожаловать!");
        }).catch(err => {
            console.log(err);
            toast.error("Что-то не так.\n Возможно пароль или логин некорректны");
        })
    }

    return(
        <div>
            <form className="auth-form" onSubmit={onSubmitLogin}>
                <h2>Вход в аккаунт</h2>
                <label>Введите вашу почту</label>
                <input
                    placeholder="почта"
                    type="text"
                    value={email}
                    onChange={onEmailChange}
                />
                <label> Введите пароль</label>
                <input
                    placeholder="пароль"
                    type="password"
                    value={password}
                    onChange={onPasswordChange}
                />
                <button className="login-button" type="submit">Войти</button>
            </form>
        </div>
    )
}

export default LoginForm;
