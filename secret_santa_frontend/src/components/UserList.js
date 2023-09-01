import {useEffect, useState} from "react";
import {axiosInstance} from "../utils/axios";
import {PARTY_URL} from "../utils/urls"
import {NavLink} from "react-router-dom";
import "../css/homepage.css"


function Image({ imageUrl }) {
    return (
        <div className="image-container">
            <img src={imageUrl} alt=":)" className="rounded-image"/>
        </div>
    );
}
function UserItem({item}) {
    return (
        <div className="user-item">
            <Image imageUrl={item.image}></Image>
            <div className="user-info-minimal">
                <p className="user-name">{item.username}</p>
                <p className="user-email">{item.email}</p>
            </div>
        </div>
    );
}

function UserList({userList}) {

    return(
        <div>
            <h1>Участники</h1>
            <div className="user-list">
                {userList.map(item => (
                    <div className="link-no-style" key={item.id}>
                        <UserItem item={item}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default UserList