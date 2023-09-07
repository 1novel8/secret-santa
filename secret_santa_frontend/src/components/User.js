import {BASE_URL} from "../utils/urls";

function User({user}){

    return(
        <div className="party-container">
            { user &&
            <div>
                <div className="big-image-container">
                    <img src={BASE_URL+user.image} alt=":)" className="big-rounded-image"/>
                </div>
                <div className="party-block">
                    <div>
                        <h1>{user.username}</h1>
                        <h2>{user.email}</h2>
                    </div>
                </div>
            </div>
            }
        </div>
    )
}

export default User;
