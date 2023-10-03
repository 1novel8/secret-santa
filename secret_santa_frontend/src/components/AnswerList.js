import "../css/homepage.css"

function AnswerItem({item}) {
    return (
            <div className="question">
                <p className="user-name">Вопрос: {item.question_name}</p>
                <p className="user-name">{item.question_text}</p>
                <p className="user-email">Ответ: {item.answer}</p>
            </div>
    );
}

function AnswerList({answers}) {

    return(
        <div>
            <h1>Ответы пользователя</h1>
            <div className="party-block">
                {answers.map(item => (
                        <AnswerItem item={item}/>
                ))}
            </div>
        </div>
    )
}

export default AnswerList;
