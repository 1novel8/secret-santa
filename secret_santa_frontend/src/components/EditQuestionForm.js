import {useState} from "react";
import {axiosInstance} from "../utils/axios";
import {QUESTION_URL} from "../utils/urls";
import toast from "react-hot-toast";

function EditQuestionForm({setEditQuestion, updateParty, questionId, old_name, old_text}) {
    const [name, setName] = useState(old_name)
    const [text, setText] = useState(old_text)

    const onNameChange = (event) => {
        setName(event.target.value);
    }
    const onTextChange = (event) => {
        setText(event.target.value);
    }

    const updateQuestion = () => {
        axiosInstance.put(
            QUESTION_URL + questionId + '/',
            {
                'name': name,
                'text': text,
            }
        ).then((response) => {
            toast.success("Вопрос обновлен!");
            console.log(response)
        }).catch(err => {
            console.log(err);
            toast.error("Что-то не так.");
        })
    }
    const onSubmitQuestion = (event) => {
        event.preventDefault();
        updateQuestion();
        updateParty();
        setEditQuestion(false);
    }

    return (
        <div>
            <form className="auth-form" onSubmit={onSubmitQuestion}>
                <h2>Обновить вопрос</h2>
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
                <button className="login-button" type="submit">Обновить</button>
            </form>
        </div>
    )
}

export default EditQuestionForm;
