import {useEffect, useState} from "react";
import {axiosInstance} from "../utils/axios";
import {QUESTION_URL} from "../utils/urls";
import toast from "react-hot-toast";
import {AiFillDelete} from "react-icons/ai";
import {GrEdit} from "react-icons/gr";
import EditQuestionForm from "./EditQuestionForm";

function Question({updateParty, isOwner, question}) {
    const [answer, setAnswer] = useState('')
    const [editQuestion, setEditQuestion] = useState(false)

    useEffect(() => {
        axiosInstance.get(QUESTION_URL + question.id + '/get_answer')
            .then(response => {
                setAnswer(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, [question.id]);

    const onAnswerChange = (event) => {
        setAnswer(event.target.value);
    }

    const onSubmitAnswer = (event) =>{
        event.preventDefault();
        axiosInstance.post(
            QUESTION_URL + question.id + '/send_answer/',
            {
                'answer': answer
            }).then(response => {
                setAnswer(response.data);
                toast.success("Ответ сохранен")

            }).catch(error => {
                toast.error("Ответ не сохранен")
                console.error('Error fetching data:', error);
            });
    }

    const onDeleteQuestion = (event) =>{
        event.preventDefault();
        axiosInstance.delete(
            QUESTION_URL + question.id +'/'
        ).then(response => {
            updateParty()
            toast.success("Ответ сохранен")

        }).catch(error => {
            toast.error("Ответ не сохранен")
            console.error('Error fetching data:', error);
        });
    }

    return (
        <div className="question">
            {isOwner &&
                <div>
                    <AiFillDelete onClick={onDeleteQuestion}/>
                    <GrEdit onClick={() => {
                        console.log(editQuestion)
                        if(editQuestion===true)
                            setEditQuestion(false)
                        else
                            setEditQuestion(true)
                    }}/>
                </div>
            }
            {editQuestion ?
                <div>
                    <EditQuestionForm updateParty={updateParty} setEditQuestion={setEditQuestion} questionId={question.id} old_name={question.name} old_text={question.text}/>
                </div>
                :<div>
                    <h2 className="question-name">{question.name}</h2>
                    <h3 className="question-text">{question.text}</h3>
                    <form onSubmit={onSubmitAnswer}>
                        <input
                        placeholder={String(answer)}
                        type="text"
                        value={answer}
                        onChange={onAnswerChange}
                        />
                        <button type="submit">Сохранить</button>
                    </form>
                </div>
            }
        </div>
    );
}
export default Question;
