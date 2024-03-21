<template>
	<div class="header">
		<div class="header_item">
			<router-link to="/"><img src="@/assets/new/LogoText.png" alt="" class="logo_img" /></router-link>
			<!-- <div class="logo" @click="nextPage('home')">
				<img src="@/assets/new/Profile.png" alt="" />
				<h1>Sequoia</h1>
			</div> -->
			<div class="header_item_right" id="desctop_header">
				<h4 v-if="chainUS" class="lang" @click="changeLocale(languages[0].language)">
					ENG
				</h4>
				<h4 v-if="chainUA" class="lang" @click="changeLocale(languages[1].language)">
					UKR
				</h4>
				<button class="btn_auth btn" @click="openAuthForm" v-if="isAuth === false">
					{{ $t("logIn") }}
				</button>
				<!-- isAuth -->
				<button class="btn_auth btn" @click="toDashboard" v-if="isAuth === true">
					{{ $t("Profile") }}
				</button>

				<button class="btn_auth btn" @click="logOut" v-if="isAuth === true">
					{{ $t("logOut") }}
				</button>

			</div>
			<div class="header_item_right" id="mobile_header">
				<button class="btn_auth btn" @click="show_menu = true">
					{{ $t("Menu") }}
				</button>
			</div>
		</div>
		<Transition name="slide-fade">
			<div class="mobile_sidebar" v-if="show_menu == true">
				<div class="header_of_mobile_sidebar">
					<button class="btn_menu btn1" @click="show_menu = false">{{ $t("Close") }}</button>
				</div>
				<hr style=" width: 100%; ">
				<div class="btn_header_of_mobile_sidebar">
					<button class="btn_menu btn1" @click="openAuthForm" v-if="isAuth === false">
						{{ $t("logIn") }}</button>
					<button class="btn_menu btn1" @click="toDashboard" v-if="isAuth === true">
						{{ $t("Profile") }}</button>
					<button class="btn_menu btn1" @click="logOut" v-if="isAuth === true">
						{{ $t("logOut") }}</button>
				</div>
				<hr style=" width: 100%; ">
				<ul class="mobile_sidebar_of_item">
					<!-- main -->
					<li @click="nextPage('main')"><a>01 {{ $t("Main") }}</a></li>
					<li @click="nextPage('Terms')"><a>02 {{ $t("Terms") }}</a></li>
					<li @click="nextPage('News')"><a>03 {{ $t("News") }}</a></li>
					<li @click="nextPage('Reviews')"><a>04 {{ $t("Reviews") }}</a></li>
					<li @click="nextPage('Contacts')"><a>05 {{ $t("Contacts") }}</a></li>
					<!-- <li><router-link to="/test-exchange">06 StartTest</router-link></li> -->
				</ul>
				<hr style=" width: 100%; ">
				<div class="multi_lang">
					<img src="@/assets/lang/usa.png" alt="" @click="changeLocale(languages[0].language)">
					<img src="@/assets/lang/ukr.png" alt="" @click="changeLocale(languages[1].language)">
					<!-- <h4 v-if="chainUS" class="lang" @click="changeLocale(languages[0].language)">
						ENG
					</h4>
					<h4 v-if="chainUA" class="lang" @click="changeLocale(languages[1].language)">
						UKR
					</h4> -->
				</div>

			</div>
		</Transition>

	</div>
</template>

<script>
import store from "@/store";
import i18n from "@/plugins/i18n";
export default {
	data() {
		return {
			languages: [
				{ flag: "us", language: "en", title: "English" },
				{ flag: "ua", language: "ua", title: "Ukraine" },
			],
			chainUA: true,
			chainUS: false,
			show_menu: false,
		};
	},
	computed: {
		openFormAuth: {
			set: (payload) => store.commit("setOpenFormAuth", payload),
			get: () => store.getters.getOpenFormAuth,
		},
		isAuth: {
			set: (payload) => store.commit("setIsAuth", payload),
			get: () => store.getters.getIsAuth,
		},
	},
	methods: {
		nextPage(name) {
			this.$router.push({ name: name, })
			this.show_menu = false
		},
		changeLocale(locale) {
			i18n.locale = locale;
			if (i18n.locale === "ua") {
				this.chainUA = false;
				this.chainUS = true;
			} else {
				this.chainUA = true;
				this.chainUS = false;
			}
		},
		openAuthForm() {
			this.show_menu = false
			this.$router.push({ name: "auth", path: "/auth" }).catch(() => { });
			this.openFormAuth = true;

		},
		toDashboard() {
			this.show_menu = false
			this.$router.push({ name: "dashboard", path: "/dashboard" });
		},
		logOut() {
			this.show_menu = false
			this.$store.dispatch("logOut");
		},
	},
};
</script>

<style scoped>
.logo_img{
	width: 140px;
}
.logo{
	display: flex;
	flex-direction: row;
	align-items: center;
	cursor: pointer;
}
.logo img{
	width: 100px;
}
.logo h1{
	font-weight: 900;
	font-size: 48px;
}
.lang:hover{
	color: rgba(249, 27, 231, 1);;
}
.slide-fade-enter-active {
	opacity: 0;
	transform: translateX(25%);
	transition: all 0.3s ease-in;
}

.slide-fade-leave-active {
	transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
	transform: translateX(25%);
	opacity: 0;
}

.mobile_sidebar {
	position: absolute;
	top: 0;
	right: 0;
	display: flex;
	flex-direction: column;
	background-color: #290044 ;
	color: #fff;
	width: 25%;
	overflow: hidden;
	min-height: 100vh;
	z-index: 100;
	transition: 0.2s cubic-bezier(0.81, -0.02, 1, 1);
}

.header_of_mobile_sidebar {
	width: 100%;
	height: 200px;
	margin: 0 auto;
	color: white;
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
}

.btn_header_of_mobile_sidebar {
	width: 100%;
	height: 150px;
	margin: 0 auto;
	color: white;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	align-items: center;
}


.mobile_sidebar_of_item {
	list-style-type: none;
	display: flex;
	flex-direction: column;
	align-items: center;
}

.mobile_sidebar_of_item li {
	width: 70%;
	text-align: left;
	padding: 14px 0px 5px 0px;
}

.mobile_sidebar_of_item li a {
	color: white;
	font-style: normal;
	font-weight: 600;
	font-size: 18px;
	line-height: 28px;
	text-transform: uppercase;
	text-decoration: none;

}

.mobile_sidebar_of_item li a:hover {
	color: rgba(249, 27, 231, 1);;
}

.multi_lang {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	width: 70%;
	margin: 0 auto;
}

.multi_lang img {
	width: 50px;
}

/* _______________ */
.header {
	width: 100%;
	height: 130px;
	margin: 0 auto;
	color: white;
	/* max-width: 1440px; */
	background-color: #290044 !important;
}

.header_item {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	height: 100%;
	padding: 0 5%;
	max-width: 1440px;
    margin: 0 auto;
}

.header_item_right {
	display: flex;
	flex-direction: row;
	align-items: center;
}

.header_item_right h4 {
	font-style: normal;
	font-weight: 700;
	font-size: 20px;
	line-height: 24px;
	cursor: pointer;
	width: 100px;
}

.header_item_right button {
	font-style: normal;
	font-weight: 700;
	font-size: 20px;
	color: #fff;
	height: 50px;
	width: 150px;
	margin-left: 25px;
}

.btn {
	border: 1px solid #fff;
	cursor: pointer;
	-webkit-tap-highlight-color: transparent;
	background-color: transparent;
	display: flex;
	align-items: center;
	justify-content: center;
	position: relative;
	z-index: 0;
	transition: 0.5s;
}

.btn::before,
.btn::after {
	position: absolute;
	background: #290044 ;
	z-index: -1;
	transition: 0.5s;
	content: "";
}

.btn::before {
	height: 50px;
	width: 130px;
}

.btn::after {
	width: 150px;
	height: 30px;
}

.noselect {
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

.btn:hover::before {
	width: 0px;
	background: #290044 ;
}

.btn:hover::after {
	height: 0px;
	background: #290044 ;
	
}

.btn:hover {
	background: #38005e;
	/* color: rgba(249, 27, 231, 1); */
	border-color: rgba(249, 27, 231, 1);
}

/* _____________________________ */
.header_of_mobile_sidebar button {
	font-style: normal;
	font-weight: 700;
	font-size: 20px;
	color: #fff;
	height: 50px;
	width: 150px;
}

.btn_header_of_mobile_sidebar button {
	font-style: normal;
	font-weight: 700;
	font-size: 20px;
	color: #fff;
	height: 50px;
	width: 150px;
}

.btn1 {
	border: 1px solid #fff;
	cursor: pointer;
	-webkit-tap-highlight-color: transparent;
	background-color: transparent;
	display: flex;
	align-items: center;
	justify-content: center;
	position: relative;
	z-index: 0;
	transition: 0.5s;
}

.btn1::before,
.btn1::after {
	position: absolute;
	background: #290044 ;
	z-index: -1;
	transition: 0.5s;
	content: "";
}

.btn1::before {
	height: 50px;
	width: 130px;
}

.btn1::after {
	width: 150px;
	height: 30px;
}

.noselect {
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

.btn1:hover::before {
	width: 0px;
	background: #290044 ;
}

.btn1:hover::after {
	height: 0px;
	background: #290044 ;
}

.btn1:hover {
	background: #290044 ;
}

/* 
#desctop_header
#mobile_header
*/
@media (min-width: 992px) {
	#desctop_header {
		display: flex;
	}

	#mobile_header {
		display: none;
	}
}

@media (max-width: 991px) {
	#desctop_header {
		display: none;
	}

	#mobile_header {
		display: block;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.header_item {
		padding: 0 2%;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.header_item {
		padding: 0 2%;
	}

	.header_item img {
		width: 75%;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.header_item {
		padding: 0 5%;
	}

	.header_item img {
		width: 75%;
	}

	.mobile_sidebar {
		width: 40%;
	}
}

@media (max-width: 479px) {
	.header_item {
		padding: 0 5%;
	}

	.header_item img {
		width: 75%;
	}

	.mobile_sidebar {
		width: 60%;
	}

	.mobile_sidebar_of_item li a {
		font-size: 16px;
		line-height: 24px;
	}
}
</style>
