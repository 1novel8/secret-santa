import "../css/general.css"
import "../css/homepage.css"
import {useEffect, useState} from "react";
import {axiosInstance} from "../utils/axios";
import {PRESENT_URL, USER_URL} from "../utils/urls";
import {Navigate} from "react-router-dom";
import User from "../components/User";

function ProfilePage({isLoggedIn, setIsLoggedIn}){
    const [user, setUser] = useState(null)
    const [presentList, setPresentList] = useState(null)

    useEffect(() => {
        fetchUser();
        fetchPresentList();
    }, []);

    const fetchUser = () =>{
        axiosInstance.get(USER_URL + 'me/')
            .then(response => {
                setUser(response.data);
                console.log(user)
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        }
    const fetchPresentList = () =>{
        axiosInstance.get(PRESENT_URL + 'me/')
            .then(response => {
                setPresentList(response.data);
                console.log(user)
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        }
    if(!isLoggedIn)
        return (<Navigate to="/"/>)
    return (
        <div>
            <main className="content">
                <h1>Мой профиль</h1>
                {user &&
                    <User user={user}/>
                }
            </main>
            <aside className="right-column">
                <h1>Список желанных подарков</h1>
                <div>Не реализовано на бэке</div>
            </aside>
        </div>
    )

}

export default ProfilePage;