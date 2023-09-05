import Question from "./Question";

function QuestionList({updateParty, isOwner, questions}){
    return(
        <div className="party-block">
        <h1>Вопросы</h1>
            {questions.map(item => (
                <Question updateParty={updateParty} key={item.id} isOwner={isOwner} question={item} />
            ))}
    </div>
    )
}

export default QuestionList;