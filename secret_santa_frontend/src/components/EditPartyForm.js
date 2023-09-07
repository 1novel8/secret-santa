import { useState} from "react";
import "../css/form.css"
import {axiosInstance} from "../utils/axios";
import toast from "react-hot-toast";
import {PARTY_URL} from "../utils/urls"

function EditPartyForm({updatePartyList, id, old_name, old_description}) {
    const [name, setName] = useState(old_name);
    const [description, setDescription] = useState(old_description);
    const onNameChange = (event) => {
        setName(event.target.value);
    }
    const onDescriptionChange = (event) => {
        setDescription(event.target.value);
    }
    const onSubmit = async (event) => {
        event.preventDefault();
        updateParty()

    }
    const updateParty = () => {
        axiosInstance.patch(
            PARTY_URL + id+'/',
            {
                'name': name,
                'description': description,
            }
        ).then((response) => {
            toast.success("Обновлено!");
            updatePartyList()
        }).catch(err => {
            console.log(err);
            toast.error("Что-то пошло не так.");
        })
    }

    return(
        <div>
            <form className="auth-form" onSubmit={onSubmit} encType="multipart/form-data">
                <h2>Создание группы</h2>
                <label>Придумайте название</label>
                <input
                    placeholder="название"
                    type="text"
                    value={name}
                    onChange={onNameChange}
                />
                <label>Краткое описание</label><br/>
                <textarea
                    placeholder="описание"
                    value={description}
                    onChange={onDescriptionChange}
                />
                <br/>
                <button className="login-button" type="submit">Обновить</button>
            </form>
        </div>
    )
}

export default EditPartyForm;
