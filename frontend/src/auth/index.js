import axios from "../axios.js";
import router from "@/router";
import store from "../store.js";

export default {
	init() {
		axios.interceptors.response.use(
			function (response) {
				return response;
			},
			function (error) {
				const { response } = error;
				if (response && response.status === 401) {
					if (router.history.current.name != "Auth") {
						store.commit("setIsAuth", false)
						localStorage.removeItem("accessToken");
						localStorage.removeItem("refreshToken");
						localStorage.removeItem("username");
						router.push("/auth");
					}
				}
				return Promise.reject({ message: response.data.detail });
			}
		);

		axios.interceptors.request.use(
			(config) => {
				if (!config.headers.Authorization) {
					const token = localStorage.getItem("accessToken");
					if (token) {
						config.headers.Authorization = `Bearer ${token}`;
					}
				}

				return config;
			},
			(error) => Promise.reject(error)
		);
	},

	login(username, pwd, otp) {
		let data = {
			username: username,
			password: pwd,
			otp: otp,
		};
		return axios.post("/auth/login/", data);
	},
	register(email, password, first_name, last_name, phone, promocode) {
		let data = {
			username: email,
			email: email,
			password: password,
			first_name: first_name,
			last_name: last_name,
			phone: phone,
			promocode: promocode,
		};
		return axios.post("/auth/register/", data);
	},
	refreshToken() {
		return axios.post("/auth/token/refresh/", {
			refresh: localStorage.getItem("refresh"),
		});
	},
};
