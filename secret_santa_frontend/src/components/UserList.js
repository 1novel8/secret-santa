import "../css/homepage.css"
import {NavLink} from "react-router-dom";
import UserItem from "./UserItem";


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
