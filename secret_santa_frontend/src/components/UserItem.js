import {BASE_URL} from "../utils/urls";

function Image({ imageUrl }) {
    return (
        <div className="image-container">
            <img src={BASE_URL + 'media/' + imageUrl} alt=":)" className="rounded-image"/>
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

export default UserItem;