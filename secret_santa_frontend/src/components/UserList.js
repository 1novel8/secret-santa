import "../css/homepage.css"
import {Navigate, NavLink} from "react-router-dom";
import {FaUserNinja} from "react-icons/fa";


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
                    <NavLink className="link-no-style" to={{pathname: "/profile"}} state={{userId: item.id}} key={item.id}>
                            <UserItem item={item}/>
                    </NavLink>
                ))}
            </div>
        </div>
    )
}

export default UserList;
