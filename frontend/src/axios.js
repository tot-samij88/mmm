// axios
import axios from "axios";

// const apiUrl = process.env.VUE_APP_API_ENDPOINT;
const apiUrl = "http://127.0.0.1:8000";
// const apiUrl = "http://192.168.10.235:8000"; // Наш сервер внутри

export default axios.create({
	baseURL: apiUrl,
});
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";
