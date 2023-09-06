import Modal from "./Modal";
import {useState} from "react";
import {axiosInstance} from "../utils/axios";
import {PARTY_URL} from "../utils/urls";
import toast from "react-hot-toast";

function Image({ imageUrl }) {
    return (
        <div className="image-container">
            <img src={imageUrl} alt=":)" className="rounded-image"/>
        </div>
    );
}
function PartyItem({item}) {
    return (
            <div className={item.is_confirmed ?"party-item": "party-item not_confirmed"}>
                <Image imageUrl={item.image}></Image>
                <div className="party-info-minimal">
                    <p className="party-item-name">{item.name}</p>
                    <p className="party-description">{item.description}</p>
                </div>
            </div>
    );
}

function PartyList({updatePartyList, partyList, setPartyId}) {
    const [joinModalActive, setJoinModelActive] = useState(false)
    const [joinPartyId, setJoinPartyId] = useState(null)
    const join = (id) =>{
        axiosInstance.post(PARTY_URL + id + '/join/')
            .then(response => {
                toast.success('Вы присоединились')
                updatePartyList();
            })
            .catch(error => {
                toast.error('Что-то пошло не так');
                console.error('Error fetching data:', error);
            });
    }
    return(
        <div>
            <h1>Твои группы</h1>
            <div className="party-list">
                {partyList.map(item => (
                    <div className="link-no-style" key={item.id}
                         onClick={() => {
                             if(item.is_confirmed === true){
                                 setPartyId(item.id)
                             }else{
                                 setJoinPartyId(item.id);
                                 setJoinModelActive(true);
                             }}}>
                        <PartyItem item={item}/>
                    </div>
                ))}
            </div>
            <Modal active={joinModalActive} setActive={setJoinModelActive}>
                <button className="oval-button" onClick={() =>{
                    join(joinPartyId)
                    setJoinModelActive(false);
                }}>Присоединиться</button>
            </Modal>
        </div>
    )
}

export default PartyList