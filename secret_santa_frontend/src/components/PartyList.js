
function Image({ imageUrl }) {
    return (
        <div className="image-container">
            <img src={imageUrl} alt=":)" className="rounded-image"/>
        </div>
    );
}
function PartyItem({item}) {
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

function PartyList({partyList, setPartyId}) {

    return(
        <div>
            <h1>Твои группы</h1>
            <div className="party-list">
                {partyList.map(item => (
                    <div className="link-no-style" key={item.id} onClick={() => {setPartyId(item.id)}}>
                        <PartyItem item={item}/>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default PartyList