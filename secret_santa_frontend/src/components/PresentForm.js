import { useState} from "react";
import "../css/form.css"
import {axiosInstance} from "../utils/axios";
import toast from "react-hot-toast";
import {PRESENT_URL} from "../utils/urls"

function PresentForm({updatePresentList, setActiveModal, isPreferred, setIsPreferred}) {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [image, setImage] = useState('');
    const [url, setUrl] = useState('');

    const onNameChange = (event) => {
        setName(event.target.value);
    }
    const onDescriptionChange = (event) => {
        setDescription(event.target.value);
    }
    const onImageChange = (event) => {
        setImage(event.target.files[0]);
    }
    const onUrlChange = (event) => {
        setUrl(event.target.value);
    }
    const onIsPreferredChange = (event) =>{
        setIsPreferred(!isPreferred);
    }
    const onSubmit = async (event) => {
        event.preventDefault();
        try {
            const formData = new FormData();
            formData.append('name', name);
            formData.append('description', description);
            formData.append('url', url);
            formData.append('image', image);
            formData.append('is_preferred', isPreferred)
            await CreatePresent(formData);
            updatePresentList();
            setActiveModal(false);
        } catch (error) {
            console.error("Error creating present:", error);
            toast.error("Что-то не так при создании.");
        }
    }
    const CreatePresent = async (formData) => {
        try {
            await axiosInstance.post(PRESENT_URL, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data' // Set the content type to multipart/form-data
                }
            });
            toast.success("Подарок добавлен!");
        } catch (error) {
            console.error("Error creating present:", error);
            toast.error("Что-то не так при создании.");
        }
    }

    return(
        <div>
            <form className="auth-form" onSubmit={onSubmit} encType="multipart/form-data">
                <h2>Добавление подарка</h2>
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
                <label>Ссылка на подарок</label>
                <input
                    type="url"
                    value={url}
                    onChange={onUrlChange}
                />
                <input
                    type={"checkbox"}
                    checked={isPreferred}
                    onChange={onIsPreferredChange}
                />
                <button className="login-button" type="submit">Добавить</button>
            </form>
        </div>
    )
}

export default PresentForm;
