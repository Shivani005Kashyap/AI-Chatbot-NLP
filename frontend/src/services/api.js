import axios from "axios";

const API = axios.create({
   baseURL: "https://ai-chatbot-nlp-hwbl.onrender.com",
});

export default API;
