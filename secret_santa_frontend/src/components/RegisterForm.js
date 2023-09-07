import { useState} from "react";
import "../css/form.css"
import toast from "react-hot-toast";
import {axiosInstance} from "../utils/axios";
import {REGISTER_URL} from "../utils/urls";


function RegisterForm({token, setRegisterForm}) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password1, setPassword1] = useState('');

    const onEmailChange = (event) => {
        setEmail(event.target.value);
    }
    const onPasswordChange = (event) => {
        setPassword(event.target.value);
    }
    const onPassword1Change = (event) => {
        setPassword1(event.target.value);
    }
    const onSubmitRegister = (event) =>{
        event.preventDefault();
        if(token === null) {
            if (email.length === 0 || password1.length === 0 || password === 0 || password1 !== password)
                toast.error('Данные введены некорректно')
            else
                registerUser(email, password)
        }else{
            if (password1.length === 0 || password === 0 || password1 !== password)
                toast.error('Данные введены некорректно')
            else
                registerUserWithToken(password)
        }
    }

    const registerUserWithToken = (password) =>{
        axiosInstance.post(
            REGISTER_URL,
            {
                'token': token,
                'password': password
            },
        ).then((response) => {
            toast.success("Регистрация прошла успешно!\nТеперь вы можете войти")
            setRegisterForm(false)
        }).catch(err => {
            console.log(err)
            toast.error(err.data)
        })
    }

    const registerUser = (email, password) =>{
        axiosInstance.post(
            REGISTER_URL,
            {
                'email': email,
                'password': password
            }
        ).then((response) => {
            toast.success("Регистрация прошла успешно!\nТеперь вы можете войти")
            setRegisterForm(false)
        }).catch(err => {
            console.log(err)
            toast.error(err.data)
        })
    }

    return(
        <div>
            <form className="auth-form" onSubmit={onSubmitRegister}>
                <h2>Регистрация</h2>
                {token === null ?
                <input
                    placeholder="почта"
                    type="text"
                    value={email}
                    onChange={onEmailChange}
                />:
                <h4>Вас пригласили! Придумайте пароль для вашего аккаунта</h4>}
                <input
                    placeholder="пароль"
                    type="password"
                    value={password}
                    onChange={onPasswordChange}
                />
                <input
                    placeholder="повторите пароль"
                    type="password"
                    value={password1}
                    onChange={onPassword1Change}
                />
                <button type="submit">Зарегистрироваться</button>
            </form>
        </div>
    )
}

export default RegisterForm;
