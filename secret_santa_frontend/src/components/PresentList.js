import {BASE_URL} from "../utils/urls";

function Image({ imageUrl }) {
    console.log(imageUrl)
    return (
        <div className="image-container">
            <img src={BASE_URL+'media/' + imageUrl} alt=":)" className="rounded-image"/>
        </div>
    );
}
function PresentItem({item}) {
    return (
        <div className="party-item">
            <Image imageUrl={item.image}></Image>
            <div className="party-info-minimal">
                <p className="party-item-name">{item.name}</p>
                <p className="party-description">{item.description}</p>
            </div>
        </div>
    );
}

function PresentList({presentList, setPresentId}) {

    return(
        <div>
            <div className="party-list">
                {presentList.map(item => (
                    <div className="link-no-style" key={item.id} onClick={() => {setPresentId(item.id)}}>
                        <PresentItem item={item}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default PresentList;
