import {axiosInstance} from "../utils/axios";
import {BASE_URL, PARTY_URL} from "../utils/urls";
import toast from "react-hot-toast";
import {useEffect, useState} from "react";
import {NavLink} from "react-router-dom";
import UserItem from "./UserItem";
import AnswerList from "./AnswerList";



function Results({partyId}){
    const [answerList, setAnswerList] = useState();
    const [receiver, setReceiver] = useState();
    const getPartyResult = () =>{
        axiosInstance.get(
            PARTY_URL + partyId +'/result/'
        ).then(response => {
            toast.success("Время кончилось! Посмотри результат!!!")
            setAnswerList(response.data.answer_list);
            setReceiver(response.data.receiver);
        }).catch(error => {
            toast.error("Время кончилось, но результатов пока нет(((")
            console.error('Error fetching data:', error);
        });
    }
    useEffect(() => {
        getPartyResult();
    }, []);

    return(
        <div className="party-block">
            <div className="party-block">
                <h1>Ну вот и все, время вышло!</h1>
                <br/>
                <p>Настало время наконец-то узнать результаты жеребьевки!</p>
                <p>Снизу ты видишь пользователя, которого ты должен удивить своим подарком.</p>
                <br/>
                <p>Нажав на его иконку ты можешь перейти на его профильм и ознакомиться с его предпочтениями.</p>
                <p>Возможно это поможет в выборе подарка.</p>
                <br/>
                <p>Так же не забудь про анкету! Мы ведь не просто так ее заполняли.</p>
                <p>Ответы пользователя ты так же можешь увидеть ниже.</p>
                <br/>
                <p>Но не забудь самое главное правило...</p>
                <h2>Никто не должен узнать, кто Санта!</h2>
            </div>
            {receiver &&
            <NavLink className="link-no-style" to={{pathname: "/profile"}} state={{userId: receiver.id}} key={receiver.id}>
                <h1>Тот кто ждет от вас подарка</h1>
                <UserItem item={receiver}/>
            </NavLink>
            }
            {answerList &&
                <AnswerList answers={answerList}/>
            }
        </div>
    )
}

export default Results;
