<template>
	<div class="referals bgcbdr">
		<h3 class="mb2">Referrals</h3>
		<h4 class="mb1">Invite your friends by promocode</h4>
		<h4 class="mb1">Share the referral code</h4>
		<p class="mb3">
			You can also share your referral link by coping and sending or
			sharing it on your social media
		</p>
		<div class="ref_btn mb4">
			<h5 class="a_ref">{{ promocode }}</h5>
			<button class="btn_standart_small">Copy code</button>
		</div>

		<h4 class="mb2">Invitations counter</h4>
		<div class="counter_ref">
			<img src="@/assets/ArrowSquareOut.png" alt="" />
			<div>
				<h6>Invited</h6>
				<h4>{{ promo_count }}</h4>
			</div>
		</div>
	</div>
</template>

<script>
import axios from '../../../axios';

export default {
	name: "referals-dashboard",
	data() {
		return {
			promocode: null,
			promo_count: null
		}
	},
	methods: {
		async getPromo() {
			var self = this
			try {
				await axios.post('/auth/promocode/', {
					headers: {
						'Content-Type': 'application/json'
					},
					data: {
						username: localStorage.getItem('username')
					}
				})
					.then(function (response) {
						var promocode = response.data
						promocode = JSON.parse(promocode)
						self.promocode = promocode['promocode']
						self.promo_count = promocode['promo_count']
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
		this.getPromo();
	}
}
</script>

<style>
.main_big h3 {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
}

.main_big h4 {
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 23px;
}

.main_big p {
	font-style: normal;
	font-weight: 400;
	font-size: 16px;
	line-height: 18px;
	color: #cccccc;
}

.main_big input {
	background-size: 30px;
	width: 70%;
	height: 40px;
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 23px;
	padding: 0 0 0 2%;
	color: #fff !important;
	border: none;
	background-color: rgba(127, 179, 238, 0.5);
	box-shadow: inset -1.98073px -1.98073px 1.98073px rgba(255, 255, 255, 0.5),
		inset 1.98073px 1.98073px 1.98073px rgba(52, 65, 166, 0.5);
	border-radius: 0.990366px;
}

.main_big input::placeholder {
	color: #fff;
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 23px;
}

.main_big input:focus {
	outline: none;
}

.inp_btn button {
	border: none;
	background-color: #fff;
	border: solid 1px #fff;
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	color: #2a3587;
	padding: 0 35px;
	height: 40px;
	cursor: pointer;
}

.inp_btn button:hover {
	background-color: #2a3587;
	color: #fff;
}

.inp_btn {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	width: 90%;
}

.ref_btn {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	width: 90%;
}

.a_ref {
	width: 70%;
	height: 40px;
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 40px;
	padding: 0 0 0 2%;
	color: #fff !important;
	border: none;
	background-color: rgba(127, 179, 238, 0.5);
	box-shadow: inset -1.98073px -1.98073px 1.98073px rgba(255, 255, 255, 0.5),
		inset 1.98073px 1.98073px 1.98073px rgba(52, 65, 166, 0.5);
	border-radius: 0.990366px;
}



.counter_ref {
	display: flex;
	flex-direction: row;
	align-items: center;
}

.counter_ref h6 {
	font-style: normal;
	font-weight: 400;
	font-size: 16px;
	line-height: 18px;
	color: #cccccc;
}

.counter_ref h4 {
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 23px;
	color: #ffffff;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {


	.instruc li {
		font-size: 14px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {}

@media (min-width: 480px) and (max-width: 767px) {}

@media (max-width: 479px) {
	.ref_btn {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 100%;
		align-items: center;
	}

	.a_ref {
		width: 100%;
		font-size: 16px;
		text-align: center;
	}

	.ref_btn button {
		width: 50%;
	}
}
</style>
