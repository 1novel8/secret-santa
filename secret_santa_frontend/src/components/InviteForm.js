import {useState} from "react";
import {axiosInstance} from "../utils/axios";
import {PARTY_URL} from "../utils/urls";
import toast from "react-hot-toast";

function InviteForm({setActiveModal, updateParty, partyId}) {
    const [email, setEmail] = useState('')

    const onEmailChange = (event) => {
        setEmail(event.target.value);
    }

    const invite = () => {
        axiosInstance.post(
            PARTY_URL + partyId + '/invite/',
            {
                'email': email
            }
        ).then((response) => {
            toast.success("Приглашение отправлено!");
        }).catch(err => {
            console.log(err);
            toast.error("Что-то не так.");
        })
    }
    const onSubmitQuestion = (event) => {
        event.preventDefault();
        invite();
        updateParty();
        setActiveModal(false);
    }

    return (
        <div>
            <form className="auth-form" onSubmit={onSubmitQuestion}>
                <h2>Пригласить пользователя</h2>
                <label>Почта</label>
                <input
                    placeholder="email"
                    type="text"
                    value={email}
                    onChange={onEmailChange}
                />
                <button className="login-button" type="submit">Пригласить</button>
            </form>
        </div>
    )
}

export default InviteForm;