<template>
	<div class="user bgcbdr" >
		<div class="user_info">
			<div class="user_info_item">
				<img src="@/assets/logoProfile.png" alt="" class="" />
				<div>
					<h3 class="" v-if="user">{{ user.username }}</h3>
					<h4 v-if="user">{{ user.last_name }} {{ user.first_name }}</h4>
				</div>
			</div>
			<div class="user_info_balance">
				<h6>Balance : <span>10022.20$</span></h6>
				<h6>Locked : <span>100.20$</span></h6>
			</div>
			<!-- <h4 class="mb1">{{ user.email }}</h4> -->
		</div>
		<div class="user_menu">
			<div class="user_menu_item">
				<button class="btn_standart_small" @click="menu_active=1" :class="{ btn_standart_small_active: menu_active == 1 }">Main</button>
				<button class="btn_standart_small" @click="menu_active=2" :class="{ btn_standart_small_active: menu_active == 2 }">Payment</button>
				<button class="btn_standart_small" @click="menu_active=3" :class="{ btn_standart_small_active: menu_active == 3 }">Statistic</button>
				<button class="btn_standart_small" @click="menu_active=4" :class="{ btn_standart_small_active: menu_active == 4 }">2FA</button>
				<!-- Partnership -->
				<button class="btn_standart_small" @click="menu_active=5" :class="{ btn_standart_small_active: menu_active == 5 }">Partnership</button>
				<button class="btn_standart_small" @click="menu_active=6" :class="{ btn_standart_small_active: menu_active == 6 }">FAQ</button>
			</div>
			<div class="profileNav">
				<!-- <h5><i class="fas fa-info-circle"></i>Profile</h5> -->
				<h5 @click="menu_active=7"><i class="fas fa-cog"></i>Settings</h5>
				<h5 @click="logOut"><i class="fas fa-sign-out-alt"></i>Logout</h5>
			</div>
		</div>
		<!-- <img src="@/assets/logoProfile.png" alt="" class="mb1" />
		<h3 class="mb1" v-if="user">{{ user.username }}</h3>
		<h4 class="mb3" v-if="user">{{ user.last_name }} {{ user.first_name }}</h4> -->
		<!-- <h4 class="mb3">{{ user.email }}</h4> -->
		<!-- <div class="profileNav mb2">
			<h5><i class="fas fa-info-circle"></i>Profile</h5>
			<h5><i class="fas fa-cog"></i>Settings</h5>
			<h5 @click="logOut"><i class="fas fa-sign-out-alt"></i>Logout</h5>
		</div> -->
	</div>
</template>

<script>
import axios from '../../../axios';
import store from "@/store";

export default {
	name: "user-dashboard",
	data() {
		return {
			user: null
		}
	},
	computed: {
		// STORE
		menu_active: {
			set: (payload) => store.commit("setProfileMenuActive", payload),
			get: () => store.getters.getProfileMenuActive,
		},
	},
	methods: {
		logOut() {
			this.show_menu = false
			this.$store.dispatch("logOut");
		},
		async getLogHist() {
			var self = this
			try {
				await axios.post('/auth/user-info/', {
					headers: {
						'Content-Type': 'application/json'
					},
					data: {
						username: localStorage.getItem('username')
					}
				})
					.then(function (response) {
						self.user = response.data.user
					})
					.catch(function (error) {
						console.log(error);
					});

			} catch (e) {
				alert('Error')
			}
		}
	},
	mounted() {
		this.getLogHist();
	}
};
</script>

<style>
.user {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	color: #fff;
	height: auto;
	padding: 1% !important;
}
.user_info{
	width: 20%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.user_info_item{
	display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
	margin-bottom: 5px;
}
.user_info_item img{
	width: 30%;
}
.user_info_balance{
	border: solid 1px #fe1ae7;
	padding: 5px 15px;
}
.user_info_balance h6{
	font-size: 16px;
	line-height: 32px;
}
.user_info_balance span{
	font-weight: 800;
}
.user_menu {
	width: 80%;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}
.user_menu_item{
	width: 90%;
	display: flex;
	flex-direction: row;
	justify-content: center;
}
.user_menu_item button{
	margin-right: 15px;
	margin-left: 15px;
}
.user h3 {
	font-style: normal;
	font-weight: 400;
	font-size: 24px;
	line-height: 29px;
}

.user h4 {
	font-style: normal;
	font-weight: 400;
	font-size: 16px;
	line-height: 19px;
	color: #cccccc;
}

.profileNav {
	display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: 100px;
}

.profileNav h5 {
	display: flex;
    flex-direction: column;
    align-items: center;
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    margin-left: 15px;
}

.profileNav h5:hover {
	color: rgba(249, 27, 231, 1);;
	cursor: pointer;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {}

@media (min-width: 768px) and (max-width: 991px) {}

@media (min-width: 480px) and (max-width: 767px) {}

@media (max-width: 479px) {}
</style>
