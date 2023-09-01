import {NavLink, Outlet} from "react-router-dom";
import "../css/general.css"
import {FaUserNinja} from "react-icons/fa";

function Layout(){
    return(
        <div>
            <header className="header">
                <NavLink className="link-no-style" to="/">SecretSanta</NavLink>
                <NavLink className="link-no-style usual-link" to="/party">Группы</NavLink>
                <NavLink className="link-no-style usual-link" to="/presents">Подарки</NavLink>
                <NavLink className="link-no-style" to="/profile"><FaUserNinja/></NavLink>
            </header>
            <Outlet/>
        </div>
    )
}

export default Layout