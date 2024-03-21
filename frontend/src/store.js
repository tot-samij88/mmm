import Vue from "vue";
import Vuex from "vuex";
import jwt from "@/auth/index.js";
import router from "@/router";

Vue.use(Vuex);

const store = new Vuex.Store({
	state: {
		list_cryoto_payment:[
			{
				'id':1,
				'name':"Bitcoin",
				'shortName':'btc'
			},
			{
				'id':2,
				'name':"Ethereum",
				'shortName':'eth'
			}
		],
		list_tarif:[
			{
				'id':1,
				'name':"Elementary",
				'profit':0.2,
				'min_deposite':100,
				'max_deposite':500,
			},
			{
				'id':2,
				'name':"Advanced",
				'profit':0.5,
				'min_deposite':500,
				'max_deposite':1000,
			},
			{
				'id':3,
				'name':"Professional",
				'profit':1,
				'min_deposite':1000,
				'max_deposite':50000,
			},
		],
		openFormAuth: false,
		state_TEST_NET: false,
		isAuth: false,
		isUsername: "Anonim",
		stepExchange: 1,
		manualCancel: false,
		username: null,
		isTFA: false,
		registerData: {
			first_name: null,
			last_name: null,
			phone: null,
			email: null,
			password: null,
			conf_password: null,
			promocode: null,
		},
		selectedPAIR: {
			full_pair: null,
			from_pair: null,
			to_pair: null,
		},
		// data for exchange
		id_request: null,
		date_create: null,
		// Seqouia
		profile_menu_active:1
	},
	mutations: {
		setOpenFormAuth: (state, payload) => (state.openFormAuth = payload),
		setRegisterData: (state, payload) => (state.registerData = payload),
		TEST_NET: (state, payload) => (state.state_TEST_NET = payload),
		setIsAuth: (state, payload) => (state.isAuth = payload),
		setIsUsername: (state, payload) => (state.isUsername = payload),
		setStepExchange: (state, payload) => (state.stepExchange = payload),
		setManualCancel: (state, payload) => (state.manualCancel = payload),
		setUsername(state, payload) {
			state.username = payload;
		},
		setTFA(state) {
			state.isTFA = true;
		},
		setSelectedPAIR: (state, payload) => (state.selectedPAIR = payload),
		// data for exchange
		setIdRequest: (state, payload) => (state.id_request = payload),
		setDateCreate: (state, payload) => (state.date_create = payload),
		// Seqouia
		setProfileMenuActive: (state, payload) => (state.profile_menu_active = payload),
		setList_tarif: (state, payload) => (state.list_tarif = payload),
	},
	getters: {
		getList_tarif:(state) =>{
			return state.list_tarif
		},
		getList_cryoto_payment:(state) =>{
			return state.list_cryoto_payment
		},
		getOpenFormAuth: (state) => {
			return state.openFormAuth;
		},
		getRegisterData: (state) => {
			return state.registerData;
		},
		getIsAuth: (state) => {
			return state.isAuth;
		},
		getIsUsername: (state) => {
			return state.isUsername;
		},
		getStepExchange: (state) => {
			return state.stepExchange;
		},
		getManualCancel: (state) => {
			return state.manualCancel;
		},
		getSelectedPAIR: (state) => {
			return state.selectedPAIR;
		},
		// data for exchange
		getIdRequest: (state) => {
			return state.id_request;
		},
		getDateCreate: (state) => {
			return state.date_create;
		},
		// Seqouia
		getProfileMenuActive: (state) => {
			return state.profile_menu_active;
		},
	},
	actions: {
		// /////////////////////////////////////////////
		// Auth
		// /////////////////////////////////////////////
		loginJWT({ commit }, payload) {
			return new Promise((resolve, reject) => {
				jwt.login(
					payload.userDetails.email,
					payload.userDetails.password,
					payload.userDetails.otp
				)
					.then((response) => {
						if (response.status === 200 && response.data.otp) {
							store.state.isTFA = true;
						}
						if (response.status === 200 && response.data.access) {
							// Navigate User to homepage | was -> router.currentRoute.query.to ||
							// mizera@gmail.com
							// 88vlad88

							// Set accessToken

							//let userData = 0

							localStorage.setItem(
								"accessToken",
								response.data.access
							);
							localStorage.setItem(
								"refreshToken",
								response.data.refresh
							);
							localStorage.setItem(
								"username",
								payload.userDetails.email
							);

							//Update user details

							commit("setOpenFormAuth", false);
							commit("setIsAuth", true);
							commit("setIsUsername", payload.userDetails.email);
							commit("setUsername", payload.userDetails.email);
							resolve(response);
							router.push({
								name: "dashboard",
								path: "/dashboard",
							});
						} else {
							reject({ message: "Wrong Email or Password" });
						}
					})
					.catch((error) => {
						reject(error);
					});
			});
		},
		registerJWT({ commit }, payload) {
			return new Promise(() => {
				jwt.register(
					payload.email,
					payload.password,
					payload.first_name,
					payload.last_name,
					payload.phone,
					payload.promocode
				)
					.then((response) => {
						console.log("[REGISTER response]", response);

						// If there's user data in response
						// було ще && response.data.access_token
						if (
							response.status === 200 &&
							response.data.token.access
						) {
							// Navigate User to homepage | was -> router.currentRoute.query.to ||
							localStorage.setItem(
								"accessToken",
								response.data.token.access
							);
							localStorage.setItem(
								"refreshToken",
								response.data.token.refresh
							);
							localStorage.setItem("username", payload.email);
							commit("setOpenFormAuth", false);
							commit("setIsAuth", true);
							commit("setUsername", payload.email);
							commit("setIsUsername", payload.email);
							// commit("TEST_NET", true);
							router.push({
								name: "dashboard",
								path: "/dashboard",
							});
							// Set accessToken

							// ТУТ ДОЛЖНА БЫТЬ ОПИСАНА ЛОГИНА ШАЖКОВ, ДЛЯ ПРОВЕРКИ ЧТО ЭТО ЧЕЛИК
							// ТОЛЬКО ТОГДА ЕГО РЕДИРЕКТИТЬ В КАБИНЕТ, ЧТО БЫ ВВЁЛ КОД ПРОВЕРКИ
							// commit("setOpenFormAuth", false);
							// commit("setIsAuth", true);
							// resolve(response);
						}
						// else {
						// 	reject({ message: "Wrong Email or Password" });
						// }
					})
					.catch((error) => {
						console.log("[ERROR register catch]", error);
					});
			});
		},

		logOut({ commit }) {
			store.state.isTFA = false;
			localStorage.removeItem("accessToken");
			localStorage.removeItem("refreshToken");
			localStorage.removeItem("username");
			// was -> router.currentRoute.query.to ||
			router.push({
				name: "main",
				path: "/",
			});
			commit("setIsAuth", false);
			commit("setIsUsername", "Anonim");
		},
	},
});

export default store;
