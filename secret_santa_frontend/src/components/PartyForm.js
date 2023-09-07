import { useState} from "react";
import "../css/form.css"
import {axiosInstance} from "../utils/axios";
import storage from "../utils/storage";
import toast from "react-hot-toast";
import {PARTY_URL} from "../utils/urls"

function PartyForm({updatePartyList, setActiveModal}) {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] = useState()
    const [finishTime, setFinishTime] = useState('')
    const onNameChange = (event) => {
        setName(event.target.value);
    }
    const onDescriptionChange = (event) => {
        setDescription(event.target.value);
    }
    const onImageChange = (event) => {
        setImage(event.target.files[0]);
    }
    const onFinishTimeChange = (event) => {
        setFinishTime(event.target.value);
    }
    const onSubmit = async (event) => {
        event.preventDefault();
        try {
            const formData = new FormData();
            formData.append('name', name);
            formData.append('description', description);
            formData.append('finish_time', finishTime);
            formData.append('image', image);
            await CreateParty(formData);
            setActiveModal(false);
            updatePartyList();
        } catch (error) {
            console.error("Error creating party:", error);
            toast.error("Что-то не так при создании.");
        }
    }
    const CreateParty = async (formData) => {
        try {
            await axiosInstance.post(PARTY_URL, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data' // Set the content type to multipart/form-data
                }
            });
            toast.success("Группа создана!");
        } catch (error) {
            console.error("Error creating party:", error);
            toast.error("Что-то не так при создании.");
        }
    }

    function calculateMinDate() {
        const now = new Date();
        now.setHours(now.getHours() + 24); // Добавляем 24 часа
        return now.toISOString().slice(0, 16); // Преобразуем в формат ГГГГ-ММ-ДДTЧЧ:ММ
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
                <label>Картинка</label>
                <input
                    type="file"
                    required={false}
                    accept="image/*"
                    onChange={onImageChange}
                />
                <label>Дата окончачния</label>
                <input
                    type="datetime-local"
                    value={finishTime}
                    onChange={onFinishTimeChange}
                    min={calculateMinDate()}
                />
                <button className="login-button" type="submit">Создать</button>
            </form>
        </div>
    )
}

export default PartyForm;
