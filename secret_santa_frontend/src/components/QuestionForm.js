import {axiosInstance} from "../utils/axios";
import {QUESTION_URL} from "../utils/urls";
import toast from "react-hot-toast";
import {useState} from "react";

function QuestionForm({updateParty, setActiveModal, partyId}) {
    const [name, setName] = useState('')
    const [text, setText] = useState('')

    const onNameChange = (event) => {
        setName(event.target.value);
    }
    const onTextChange = (event) => {
        setText(event.target.value);
    }

    const createQuestion = () => {
        axiosInstance.post(
            QUESTION_URL,
            {
                'name': name,
                'text': text,
                'party_id': partyId
            }
        ).then((response) => {
            toast.success("Вопрос добавлен!");

        }).catch(err => {
            console.log(err);
            toast.error("Что-то не так.");
        })
    }
    const onSubmitQuestion = (event) => {
        event.preventDefault();
        createQuestion();
        updateParty()
        setActiveModal(false);
    }

    return(
        <div>
            <form className="auth-form" onSubmit={onSubmitQuestion}>
                <h2>Добавить вопрос</h2>
                <label>Название</label>
                <input
                    placeholder="название"
                    type="text"
                    value={name}
                    onChange={onNameChange}
                />
                <label> Текст вопроса</label>
                <input
                    placeholder="вопрос"
                    type="text"
                    value={text}
                    onChange={onTextChange}
                />
                <button className="login-button" type="submit">Добавить</button>
            </form>
        </div>
    )
}

export default QuestionForm;
