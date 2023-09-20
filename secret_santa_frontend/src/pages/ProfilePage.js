import "../css/general.css"
import "../css/homepage.css"
import {useEffect, useState} from "react";
import {axiosInstance} from "../utils/axios";
import {PARTY_URL, PRESENT_URL, USER_URL} from "../utils/urls";
import {Navigate} from "react-router-dom";
import User from "../components/User";
import Modal from "../components/Modal";
import PresentForm from "../components/PresentForm";
import storage from "../utils/storage";
import PresentList from "../components/PresentList";
import PartyList from "../components/PartyList";

function ProfilePage({isLoggedIn, setIsLoggedIn}){
    const [user, setUser] = useState(null);
    const [presentModalActive, setPresentModalActive] = useState(false);
    const [preferredPresentList, setPreferredPresentList] = useState(null);
    const [notPreferredPresentList, setNotPreferredPresentList] = useState(null);
    const [isPreferred, setIsPreferred] = useState(true);
    const [presentId, setPresentId] = useState(null);

    const fetchPresentList = () => {
        axiosInstance.get(PRESENT_URL)
            .then(response => {
                const data = response.data;
                setPreferredPresentList(data.filter(item => item.is_preferred === true));
                setNotPreferredPresentList(data.filter(item => item.is_preferred === false));

            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    useEffect(() => {
        fetchUser();
        fetchPresentList();
    }, []);

    const fetchUser = () =>{
        const id = storage.getUserId();

        axiosInstance.get(USER_URL + id)
            .then(response => {
                setUser(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    if(!isLoggedIn)
        return (<Navigate to="/"/>)
    return (
        <div >
            <div className="page-container">
                <aside className="left-column">
                    <h1>Список нежелаемых подарков</h1>
                    <button className="oval-button" onClick={() =>{setIsPreferred(false); setPresentModalActive(true)}}>Добавить</button>
                    {notPreferredPresentList &&
                    <PresentList presentList={notPreferredPresentList} setPresentId={setPresentId}/>
                    }
                </aside>
                <main className="content">
                    <h1>Мой профиль</h1>
                    {user &&
                        <User user={user}/>
                    }
                </main>
                <aside className="right-column">
                    <h1>Список желанных подарков</h1>
                    <button className="oval-button" onClick={() =>{setIsPreferred(true); setPresentModalActive(true)}}>Добавить</button>
                    {notPreferredPresentList &&
                        <PresentList presentList={preferredPresentList} setPresentId={setPresentId}/>
                    }
                </aside>
            </div>
            <Modal active={presentModalActive} setActive={setPresentModalActive}>
                <PresentForm updatePresentList={fetchPresentList} isPreferred={isPreferred} setIsPreferred={setIsPreferred} setActiveModal={setPresentModalActive}/>
            </Modal>
        </div>
    )

}

export default ProfilePage;
