import {format} from "date-fns";
import {toDate, utcToZonedTime} from "date-fns-tz";
import QuestionList from "./QuestionList";
import {GrEdit} from "react-icons/gr";
import {useState} from "react";
import EditPartyForm from "./EditPartyForm";
import {AiFillDelete} from "react-icons/ai";
import {axiosInstance} from "../utils/axios";
import {PARTY_URL} from "../utils/urls";
import toast from "react-hot-toast";


const timeZone = 'Europe/Minsk';

function Party({setParty, setQuestionModalActive, updateParty, updatePartyList, party}){
    const [editParty, setEditParty] = useState(false)

    const onDeleteParty = (event) =>{
        event.preventDefault();
        axiosInstance.delete(
            PARTY_URL + party.id +'/'
        ).then(response => {
            setParty(null);
            updatePartyList();
            toast.success("Группа Удалена")

        }).catch(error => {
            toast.error("Что-то пошло не так")
            console.error('Error fetching data:', error);
        });
    }

    return(
        <div className="party-container">
            <div>
                <div className="big-image-container">
                    <img src={'http://127.0.0.1:8000'+party.image} alt=":)" className="big-rounded-image"/>
                </div>
                <div className="party-block">
                    {party.is_owner &&
                        <div>
                            <AiFillDelete onClick={onDeleteParty}/>
                            <GrEdit onClick={()=>{
                                if (editParty===true)
                                    setEditParty(false);
                                else
                                    setEditParty(true)
                            }}/>
                        </div>
                    }
                    {editParty ?
                        <div>
                            <EditPartyForm updatePartyList={updatePartyList} id={party.id} old_name={party.name} old_description={party.description} old_image={party.image} old_finishTime={party.finish_time}/>
                        </div>
                        :
                        <div>
                            <h1>{party.name}</h1>
                            <h2>{party.description}</h2>
                            <div>{party.is_owner ? <p> Вы Владелец</p> :<p> Вы Участник</p>}</div>
                            <h3>Закончится: {party.finish_time && format(utcToZonedTime(toDate(party.finish_time), timeZone), 'dd.MM.yyyy HH:mm')}</h3>
                        </div>
                    }
                </div>
                {party.questions ?
                    <div>
                        {party.is_owner &&
                        <button className="oval-button" onClick={() =>{setQuestionModalActive(true)}}>Добавить вопрос</button>}
                        <QuestionList updateParty={updateParty} isOwner={party.is_owner} questions={party.questions}/>
                    </div>
                    :
                    <h2>У вас пока нет вопросов</h2>
                }
            </div>
        </div>
    )
}

export default Party;
