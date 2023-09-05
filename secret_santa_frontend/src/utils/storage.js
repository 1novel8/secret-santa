const storage = {
    getToken: () => {
        try {
            return JSON.parse(
                window.localStorage.getItem(`token`)
            )
        } catch {
            return null;
        }
    },
    setToken: (token) => {
        window.localStorage.setItem(`token`, JSON.stringify(token));
    },

    getRefreshToken: () => {
        try {
            return JSON.parse(
                window.localStorage.getItem(`refresh`)
            )
        } catch {
            return null;
        }
    },
    setRefreshToken: (token) => {
        window.localStorage.setItem(`refresh`, JSON.stringify(token));
    },

    clearToken: () => {
        window.localStorage.removeItem(`token`);
        window.localStorage.removeItem('refresh');
    },
};

export default storage;