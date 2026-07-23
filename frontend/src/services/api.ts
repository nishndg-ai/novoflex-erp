import axios from "axios";

const api = axios.create({
  baseURL: "/",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 15000,
});

api.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => Promise.reject(error)
);

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error);
    return Promise.reject(error);
  }
);

export default api;