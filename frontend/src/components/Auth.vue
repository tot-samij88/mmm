<template>
	<div class="main_auth">
		<div class="main_form">
			<div class="content_auth" v-if="loginForm === true">
				<div class="header_auth">
					<button @click="closeFormAuth">
						<img src="@/assets/times.png" alt="" />
					</button>
				</div>
				<div class="body_auth">
					<input type="Email" placeholder="E-mail" v-model="email" />
					<input type="password" placeholder="Password" v-model="password" v-on:keyup.enter="loginJWT" />
					<input v-if="$store.state.isTFA" type="text" placeholder="000 000" v-model="otp" />
					<!-- <div class="check_box">
						<input type="checkbox" name="" id="" v-model="rememberMe" />
						<h4 @click="rememberMe = !rememberMe">Remember me</h4>
					</div> -->
				</div>
				<div class="footer_auth">
					<button class="btn-fill" :disabled="!validateForm" @click="loginJWT">
						Enter
					</button>
					<button @click="openRegisterForm" class="btn-fill-2">Register</button>
				</div>
			</div>
			<div class="content_auth" v-if="registerForm === true" v-click-outside="closeFormAuth">
				<div class="header_auth">
					<button @click="closeFormAuth">
						<img src="@/assets/times.png" alt="" /></button><br />
					<h1>Create an account</h1>
					<p>
						Create your account, it takes less than a minute. If you
						already have an account
						<span @click="closeRegisterForm">login</span>
					</p>
				</div>
				<div class="body_auth">
					<input type="Email" placeholder="First Name" name="FirstName" v-model="registerData.first_name" />
					<div class="error" v-if="!$v.registerData.first_name.required">First name required</div>
					<div class="error" v-if="!$v.registerData.first_name.alpha">First name should contain only alpha
					</div>
					<input type="Email" placeholder="Last Name" name="LastName" v-model="registerData.last_name" />
					<div class="error" v-if="!$v.registerData.last_name.required">Last name required</div>
					<div class="error" v-if="!$v.registerData.last_name.alpha">Last name should contain only alpha</div>
					<input type="Email" placeholder="E-mail" v-model="registerData.email" />
					<div class="error" v-if="!$v.registerData.email.required">Email required</div>
					<div class="error" v-if="!$v.registerData.email.email">Invalid email</div>
					<input type="password" placeholder="Password" v-model="registerData.password" />
					<div class="error" v-if="!$v.registerData.password.required">Password required</div>
					<div class="error" v-if="!$v.registerData.password.minLength">Passport length must be at least 8
						characters</div>
					<input type="password" placeholder="Confirm password" v-model="registerData.conf_password" />
					<div class="error" v-if="!$v.registerData.conf_password.required">Password required</div>
					<div class="error"
						v-if="!$v.registerData.conf_password.sameAs && $v.registerData.conf_password.required">Passwords
						not same</div>
					<input type="Email" placeholder="Promocode" name="Promocode" v-model="registerData.promocode" />

				</div>
				<br />
				<div class="footer_auth">
					<button class="btn-fill" @click="registerJWT">
						Register
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import store from "@/store";
import Vue from "vue";
import vClickOutside from "v-click-outside";
import axios from '../axios';
import { validationMixin } from 'vuelidate';
// import { email, required, numeric, alpha } from '@vuelidate/validators';
import { required, alpha, numeric, email, sameAs, minLength } from 'vuelidate/lib/validators'



Vue.use(vClickOutside);
export default {
	data() {
		return {
			email: "",
			password: "",
			otp: "",
			rememberMe: false,
			loginForm: true,
			registerForm: false,
			vcoConfig: {
				handler: this.handler,
				middleware: this.middleware,
				events: ["dblclick", "click"],
				// Note: The default value is true, but in case you want to activate / deactivate
				//       this directive dynamically use this attribute.
				isActive: true,
				// Note: The default value is true. See "Detecting Iframe Clicks" section
				//       to understand why this behavior is behind a flag.
				detectIFrame: true,
				// Note: The default value is false. Sets the capture option for EventTarget addEventListener method.
				//       Could be useful if some event's handler calls stopPropagation method preventing event bubbling.
				capture: false,
			},
		};
	},
	validations: {
		registerData: {
			first_name: { required, alpha },
			last_name: { required, alpha },
			phone: { required, numeric },
			email: { required, email },
			password: {
				required,
				minLength: minLength(8)
			},
			conf_password: {
				required,
				sameAs: sameAs('password')
			},
		},
	},
	mixins: [validationMixin,],
	computed: {
		registerData: {
			set: (payload) => store.commit("setRegisterData", payload),
			get: () => store.getters.getRegisterData,
		},
		openFormAuth: {
			set: (payload) => store.commit("setOpenFormAuth", payload),
			get: () => store.getters.getOpenFormAuth,
		},
		validateForm() {
			return this.email != "" && this.password != "";
		},
	},
	methods: {
		openRegisterForm() {
			this.registerForm = true;
			this.loginForm = false;
		},
		closeRegisterForm() {
			this.registerForm = false;
			this.loginForm = true;
		},
		closeFormAuth() {
			this.$router.push('/');
			this.openFormAuth = false;
		},
		handler(event) {
			console.log(
				"2000 Clicked outside (Using config), middleware returned true :)",
				event
			);
		},
		// Note: The middleware will be executed if the event was fired outside the element.
		//       It should have only sync functionality and it should return a boolean to
		//       define if the handler should be fire or not
		middleware(event) {
			return event.target.className !== "modal";
		},
		loginJWT() {
			//if (!this.checkLogin()) return;
			// Loading
			// this.$vs.loading();
			const payload = {
				userDetails: {
					email: this.email,
					password: this.password,
					otp: this.otp,
				},
			};

			try {
				axios.post('/auth/set_logging_history/', {
					headers: {
						'Content-Type': 'application/json'
					},
					data: {
						username: this.email
					}
				})
					.catch(function (error) {
						console.log(error);
					});

			} catch (e) {
				alert('Error')
			}

			// console.log("CREATE PAYLOAD", payload);
			this.$store
				.dispatch("loginJWT", payload)
				.then(function (data) {
					// this.$vs.loading.close();
					console.log("data", data);
				})
				.catch((err) => {
					console.log("err", err);
					// this.$vs.loading.close();
					// this.$vs.notify({
					// 	title: "Error",
					// 	text: error.message,
					// 	iconPack: "feather",
					// 	icon: "icon-alert-circle",
					// 	color: "danger",
					// });
				});
		},
		registerJWT() {
			//if (!this.checkLogin()) return;
			// Loading
			// this.$vs.loading();

			const payload = {
				email: this.registerData.email,
				password: this.registerData.password,
				// c_password: this.r_passwordRepeat, // убрать и проверять JS на ===
				phone: this.registerData.phone,
				first_name: this.registerData.first_name,
				last_name: this.registerData.last_name,
				promocode: this.registerData.promocode,
			};

			console.log(payload);
			this.$store
				.dispatch("registerJWT", payload)
				.then((resp) => {
					// this.$vs.loading.close();
					console.log(resp);
				})
				.catch((error) => {
					console.log("[ERROR] in registerJWT [AUTH.VUE]", error);
					// this.$vs.loading.close();
					// this.$vs.notify({
					// 	title: "Error",
					// 	text: error.message,
					// 	iconPack: "feather",
					// 	icon: "icon-alert-circle",
					// 	color: "danger",
					// });
				});
			// try {
			// 	axios.post('/auth/set_logging_history/', {
			// 		headers: {
			// 			'Content-Type': 'application/json'
			// 		},
			// 		data: {
			// 			username: this.registerData.email
			// 		}
			// 	})
			// 	.catch(function (error) {
			// 		console.log(error);
			// 	});
			// } catch (e) {
			// 	alert('Error')
			// 	}

		},
	},
};
</script>

<style>
.main_auth {
	position: fixed !important;
	z-index: 10;
	width: 100vw;
	height: 100vh;
	background: rgba(0, 0, 0, 0.3);
	top: 0;
	left: 0;
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
}

.main_form {
	width: 30%;
	background: rgba(255, 255, 255, 0.1);
	border: solid 3px rgba(249, 27, 231, 1);
	border-radius: 5px;

}

.content_auth {
	width: 90%;
	height: 90%;
	padding: 5%;
	background: rgba(0, 0, 0, 0.15);
	backdrop-filter: blur(150px);
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

/*  header_auth
        body_auth
        footer_auth 
    */
.header_auth {
	display: flex;
	flex-direction: row;
	justify-content: flex-end;
	flex-wrap: wrap;
	margin-bottom: 20px;
}

.header_auth h1,
.header_auth p {
	width: 100%;
	margin: 0;
	color: #fff;
}

.header_auth span {
	color: rgba(249, 27, 231, 1);
	cursor: pointer;
}

.header_auth span:hover {
	text-decoration: underline;
}

.header_auth h1 {
	font-style: normal;
	font-weight: 900;
	font-size: 28px;
    line-height: 39px;
}

.header_auth button {
	font-size: 32px;
	color: #fff;
	border: none;
	background-color: inherit;
	cursor: pointer;
	line-height: 20px;
}

.body_auth {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	height: 50%;
	/* margin-bottom: 25px; */
}

.body_auth input {
	margin-bottom: 25px;
}

.body_auth .check_box {
	display: flex;
	flex-direction: row;
	margin-top: 30px;
	margin-bottom: 25px;
}

.body_auth input {
	width: 100%;
	height: 40px;
}

.body_auth .check_box h4 {
	margin: 0;
	color: #fff;
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	line-height: 28px;
	cursor: pointer;
}

.body_auth h6 {
	margin: 0;
}

.body_auth input {
	height: 40px;
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	color: #fff !important;
	border: none;
	background-color: transparent;
	border-radius: 0.990366px;
	border-bottom: solid 2px rgba(249, 27, 231, 1);
}

.body_auth input::placeholder {
	color: rgba(249, 27, 231, 0.5);
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
}

.body_auth input:focus {
	outline: none;
}

.body_auth .check_box input[type="checkbox"] {
	height: 24px;
	width: 24px;
	border: solid 1px #fff !important;
	background-color: inherit !important;
	cursor: pointer;
	margin: 0 20px 0px 0;
}

.footer_auth {
	display: flex;
	flex-direction: row;
	justify-content: space-around;
}

.footer_auth button {
	min-width: 170px;
	padding: 10px 30px;
}

.active_button {
	color: #38005e !important;
	background-color: #fff !important;
}

.error {
	padding: 0px 0px 0px 1px;
	color: #999;
	max-height: 0;
	transition: 0.28s;
	color: red;
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.main_form {
		width: 40%;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.main_form {
		width: 50%;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.main_form {
		width: 60%;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.main_form {
		width: 80%;
	}

	.body_auth input {
		font-size: 18px;
	}

	.body_auth input::placeholder {
		font-size: 18px;
	}

	.body_auth .check_box {
		margin-top: 20px;
		margin-bottom: 20px;
	}

	.body_auth .check_box input[type="checkbox"] {
		height: 16px;
		width: 16px;
		border: solid 1px #fff !important;
		background-color: inherit !important;
		cursor: pointer;
		margin: 0 10px 0px 0;
	}

	.body_auth .check_box h4 {
		font-size: 16px;
		line-height: 16px;
		cursor: pointer;
	}

	.footer_auth button {
		min-width: 130px;
		padding: 10px 30px;
		font-size: 18px;
		line-height: 18px;
	}

	/* Registration */
	.header_auth h1 {
		font-size: 24px;
	}

	.header_auth p {
		font-size: 14px;
		margin-top: 5px;
	}
}

@media (max-width: 479px) {
	.main_form {
		width: 80%;
	}

	.body_auth input {
		font-size: 14px;
		height: 20px;
	}

	.body_auth input::placeholder {
		font-size: 14px;
	}

	.body_auth .check_box {
		margin-top: 20px;
		margin-bottom: 20px;
	}

	.body_auth .check_box input[type="checkbox"] {
		height: 16px;
		width: 16px;
		border: solid 1px #fff !important;
		background-color: inherit !important;
		cursor: pointer;
		margin: 0 10px 0px 0;
	}

	.body_auth .check_box h4 {
		font-size: 16px;
		line-height: 16px;
		cursor: pointer;
	}

	.footer_auth button {
		min-width: 100px;
		padding: 10px 20px;
		font-size: 16px;
		line-height: 16px;
	}

	/* Registration */
	.header_auth h1 {
		font-size: 18px;
	}

	.header_auth p {
		font-size: 14px;
		margin-top: 5px;
	}

	.error {
		padding: 0px 0px 0px 1px;
		max-height: 0;
		transition: 0.28s;
		color: red;
		font-size: 14px;
	}
}
</style>
