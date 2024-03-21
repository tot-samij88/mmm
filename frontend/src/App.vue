<template>
	<div id="app">
		<Header />
		<Auth v-if="openFormAuth === true" />
		<div class="content">
			<!-- <SideBar /> -->
			<router-view />
		</div>
		<Footer />
	</div>
</template>
<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
// import SideBar from "@/components/SideBar.vue";
import Auth from "@/components/Auth.vue";
// ____
import store from "@/store";
import jwt from "@/auth/index.js";

export default {
	name: "Home",
	components: {
		Header,
		Footer,
		// SideBar,
		Auth,
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
	mounted() {
		const token = localStorage.getItem("accessToken");
		if (token) {
			this.isAuth = true;
		}
	},
	async created() {
		jwt.init();
	},
};
</script>
<style>
@import './assets/reset.min.css';

body {
	margin: 0;
}

#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	background: #38005e;
	min-height: 100vh;
	display: flex;
	flex-direction: column;
}

.content {
	display: flex;
	flex-direction: row;
	max-width: 1440px;
	width: 100%;
	margin: 0 auto;
	min-height: 69vh;
	flex: 1 1 auto;
}

.btn_standart {
	border: solid 1px #fe1ae7;
	background-color: transparent;
	color: #fff;
	border-radius: 10px;
	cursor: pointer;
	font-size: 24px;
	padding: 15px 30px;
	font-weight: 600;
}

.btn_standart:hover {
	border: solid 1px #7f3bd5;
	background-color: #fe1ae7;
	color: #fff;
}

.btn_standart_active {
	border: solid 1px #7f3bd5;
	background-color: #fe1ae7;
	color: #fff;
}

.btn_standart_small {
	border: solid 1px #fe1ae7;
	background-color: transparent;
	color: #fff;
	border-radius: 10px;
	cursor: pointer;
	font-size: 18px;
	padding: 10px 20px;
	font-weight: 600;
}

.btn_standart_small:hover {
	border: solid 1px #7f3bd5;
	background-color: #fe1ae7;
	color: #fff;
}

.btn_standart_small_active {
	border: solid 1px #7f3bd5;
	background-color: #fe1ae7;
	color: #fff;
}

.btn-fill {
	background: linear-gradient(73.05deg, #7f3bd5 -2.78%, #fe1ae7 101.85%);
	border-radius: 10px;
	text-decoration: none;
	color: #fff;
	border: none;
	cursor: pointer;
	font-size: 24px;
	padding: 15px 30px;
}

.btn-fill:hover {
	background: linear-gradient(73.05deg, #fe1ae7 -2.78%, #7f3bd5 101.85%);
}

.btn-fill-2 {

	background: linear-gradient(73.05deg, #fe1ae7 -2.78%, #7f3bd5 101.85%);
	border-radius: 10px;
	text-decoration: none;
	color: #fff;
	border: none;
	cursor: pointer;
	font-size: 24px;
	padding: 15px 30px;
}

.btn-fill-2:hover {
	background: linear-gradient(73.05deg, #7f3bd5 -2.78%, #fe1ae7 101.85%);
}

/* width */
::-webkit-scrollbar {
	width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
	box-shadow: inset 0 0 1px rgba(249, 27, 231, 1);
	;
	border-radius: 5px;
}

/* Handle */
::-webkit-scrollbar-thumb {
	background: rgba(249, 27, 231, 1);
	;
	border-radius: 5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
	background: rgba(249, 27, 231, 1);
	;
}

/* VALIDATION  and Select*/

.custom_invalid {
	width: 100%;
	margin-top: 0.25rem;
	font-size: 80%;
	color: #dc3545;
}

.style-chooser .vs__selected {
	color: #fff;
	fill: #fe1ae7;
}

.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {
	background: #290044;
	border: none;
	color: #fff;
	text-transform: lowercase;
	font-variant: small-caps;
	height: fit-content;
	
}
.style-chooser .vs__selected-options{
	flex-wrap: nowrap;
}
/* 
--vs-dropdown-option--active-bg: #664cc3;
  --vs-dropdown-option--active-color: #eeeeee;
*/
.style-chooser .vs__dropdown-option:hover{
	background-color: #fe1ae7;
	cursor: pointer;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
	fill: #fff;
}

/* Input */
.input_classic {
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

.input_classic::placeholder {
	color: rgba(249, 27, 231, 0.5);
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
}

.input_classic:focus {
	outline: none;
}
.input_pink {
    height: 34px;
    font-style: normal;
    font-weight: 600;
    font-size: 18px;
    line-height: 24px;
    color: #fff !important;
    border: none;
    text-align: center;
    padding: 5px;
    background-color: transparent;
    border-radius: 0.990366px;
    border-bottom: solid 2px rgba(249, 27, 231, 1);
}

.input_pink::placeholder {
	color: #fff;
	font-style: normal;
	font-weight: 600;
	font-size: 18px;
}

.input_pink:focus {
	outline: none;
}
.p_imp1{
	padding: 1% !important;
}
.mb1 {
	margin-bottom: 10px;
}

.mb2 {
	margin-bottom: 20px;
}

.mb3 {
	margin-bottom: 30px;
}

.mb4 {
	margin-bottom: 40px;
}

.mb5 {
	margin-bottom: 50px;
}

.mt1 {
	margin-top: 10px;
}

.mt2 {
	margin-top: 20px;
}

.mt3 {
	margin-top: 30px;
}

.mt4 {
	margin-top: 40px;
}

.mt5 {
	margin-top: 50px;
}

.mr1 {
	margin-right: 10px;
}

.mh300 {
	min-height: 300px;
}

.w100 {
	width: 100%;
}

.w50 {
	width: 50%;
}

.w40 {
	width: 40%;
}

.weight900 {
	font-weight: 900;
}

.txt-l {
	text-align: left;
}

.txt-c {
	text-align: center;
}

.txt-r {
	text-align: right;
}

.txt-j {
	text-align: justify;
}

/* input range */
input[type=range] {
	height: 22px;
	-webkit-appearance: none;
	margin: 10px 0;
	width: 100%;
	background: transparent;
}

input[type=range]:focus {
	outline: none;
}

input[type=range]::-webkit-slider-runnable-track {
	width: 100%;
	height: 5px;
	cursor: pointer;
	animate: 0.2s;
	box-shadow: 0px 0px 0px #000000;
	background: #FE1AE7;
	border-radius: 5px;
	border: 0px solid #000000;
}

input[type=range]::-webkit-slider-thumb {
	box-shadow: 1px 1px 5px #000000;
	border: 0px solid #000000;
	height: 15px;
	width: 15px;
	border-radius: 50px;
	background: #fff;
	cursor: pointer;
	-webkit-appearance: none;
	margin-top: -5px;
}

input[type=range]:focus::-webkit-slider-runnable-track {
	background: #FE1AE7;
}

input[type=range]::-moz-range-track {
	width: 100%;
	height: 5px;
	cursor: pointer;
	animate: 0.2s;
	box-shadow: 0px 0px 0px #000000;
	background: #FE1AE7;
	border-radius: 5px;
	border: 0px solid #000000;
}

input[type=range]::-moz-range-thumb {
	box-shadow: 1px 1px 5px #000000;
	border: 0px solid #000000;
	height: 15px;
	width: 15px;
	border-radius: 50px;
	background: #290044;
	cursor: pointer;
}

input[type=range]::-ms-track {
	width: 100%;
	height: 5px;
	cursor: pointer;
	animate: 0.2s;
	background: transparent;
	border-color: transparent;
	color: transparent;
}

input[type=range]::-ms-fill-lower {
	background: #FE1AE7;
	border: 0px solid #000000;
	border-radius: 10px;
	box-shadow: 0px 0px 0px #000000;
}

input[type=range]::-ms-fill-upper {
	background: #FE1AE7;
	border: 0px solid #000000;
	border-radius: 10px;
	box-shadow: 0px 0px 0px #000000;
}

input[type=range]::-ms-thumb {
	margin-top: 1px;
	box-shadow: 1px 1px 5px #000000;
	border: 0px solid #000000;
	height: 15px;
	width: 15px;
	border-radius: 50px;
	background: #290044;
	cursor: pointer;
}

input[type=range]:focus::-ms-fill-lower {
	background: #FE1AE7;
}

input[type=range]:focus::-ms-fill-upper {
	background: #FE1AE7;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {}

@media (min-width: 768px) and (max-width: 991px) {}

@media (min-width: 480px) and (max-width: 767px) {}

@media (max-width: 479px) {}</style>
