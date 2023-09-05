import axios, { AxiosRequestConfig } from 'axios';

import storage from './storage';
import {TOKEN_REFRESH_URL} from "./urls";

export const isAxiosError = axios.isAxiosError;

const axiosConfig: AxiosRequestConfig = {
    baseURL: "http://localhost:8000/api/",
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
};

export const axiosInstance = axios.create(axiosConfig);

axiosInstance.interceptors.request.use((config) => {
    const token = storage.getToken();

    if (token && config.headers) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }

    return config;
});

axiosInstance.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        if (error.response && error.response.status === 401 && storage.getRefreshToken() !== null) {
            const refreshToken = storage.getRefreshToken();
            if (refreshToken) {
                try {
                    const refreshResponse = await axiosInstance.post(TOKEN_REFRESH_URL, {
                        refresh: refreshToken,
                    });
                    const newAccessToken = refreshResponse.data.access;
                    storage.setToken(newAccessToken);

                    // Повторяем оригинальный запрос с новым токеном
                    const originalRequest = error.config;
                    originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                    return axiosInstance(originalRequest);
                } catch (refreshError) {
                    // Обработка ошибки при обновлении токена
                    console.error('Error refreshing token:', refreshError);
                    // Вы можете также очистить хранилище токенов здесь, если обновление не удалось
                    storage.clearToken();

                    return Promise.reject(refreshError);
                }
            }
        }
        return Promise.reject(error);
    }
);
