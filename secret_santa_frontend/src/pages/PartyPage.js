import "../css/general.css"
import "../css/homepage.css"
import {Navigate} from "react-router-dom";
import Party from "../components/Party";
import PartyList from "../components/PartyList";
import {useEffect, useState} from "react";
import UserList from "../components/UserList";
import Modal from "../components/Modal";
import PartyForm from "../components/PartyForm";
import {axiosInstance} from "../utils/axios";
import {PARTY_URL} from "../utils/urls";
import QuestionForm from "../components/QuestionForm";

function PartyPage({isLoggedIn, setIsLoggedIn}){
    const [partyId, setPartyId] = useState(null);
    const [party, setParty] = useState(null);
    const [partyModalActive, setPartyModalActive] = useState(false)
    const [questionModalActive, setQuestionModelActive] = useState(false)
    const [partyList, setPartyList] = useState([]);

    const fetchPartyList = () => {
        axiosInstance.get(PARTY_URL)
            .then(response => {
                setPartyList(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    const fetchParty = () =>{
        axiosInstance.get(PARTY_URL + partyId)
            .then(response => {
                setParty(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    useEffect(() => {
        fetchPartyList();
    }, []);

    useEffect(() => {
        if(partyId !== null)
            fetchParty();
    }, [partyId]);

    if(isLoggedIn){
        return(
            <div >
                <div className="page-container">
                    <aside className="left-column">
                        <button className="oval-button" onClick={() =>{setPartyModalActive(true)}}>Создать группу</button>
                        <PartyList partyList={partyList} setPartyId={setPartyId}/>
                    </aside>
                    <main className="content">
                        {party ?
                            <Party setQuestionModalActive={setQuestionModelActive} updateParty={fetchParty} updatePartyList={fetchPartyList} key={party.id} party={party}/> :
                            <h2>Выберите группу из списка</h2>
                        }
                    </main>
                    <aside className="right-column">
                        <button className="oval-button">Пригласить участника</button>
                        {party ?
                            <UserList userList={party.users}/> :
                            <h2>Вы пока никого не добавили в группу</h2>
                        }
                    </aside>
                </div>
                <Modal active={partyModalActive} setActive={setPartyModalActive}>
                    <PartyForm setActiveModal={setPartyModalActive} updatePartyList={fetchPartyList}/>
                </Modal>
                <Modal active={questionModalActive} setActive={setQuestionModelActive}>
                    <QuestionForm setActiveModal={setQuestionModelActive} updateParty={fetchParty} partyId={partyId}/>
                </Modal>
            </div>
        )}
    return (<Navigate to="/"/>)

}

export default PartyPage;