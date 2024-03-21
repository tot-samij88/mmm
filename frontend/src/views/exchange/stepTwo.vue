<template>
	<div class="main_page">
		<div class="central">
			<div class="StartExchange">
				<div class="blockExchange">
					<div class="header_Exchange">
						<button style="cursor: pointer" @click="manualCloseExchange">
							&#215;
						</button>

						<h3 v-if="ws_payment">Exchange {{ ws_payment.from_pair }} to {{ ws_payment.to_pair }}</h3>

						<ul>
							<li>
								<i class="fas fa-pencil-alt"></i>
								<h5>Data input</h5>
							</li>

							<li class="activeLi">
								<i class="fas fa-credit-card"></i>
								Payment
							</li>

							<li>
								<i class="fas fa-check-double"></i>
								Completion
							</li>
						</ul>
					</div>
					<div class="enteringValues mh300 pay_time">
						<h3 class="weight900 mt3 mb1">Attention!</h3>
						<!-- ВСе текста должны генерироваться на беке -->
						<p class="mb1">
							This address only accepts Ethereum ETH. Please do not send any other
							currency to this address. They will not be credited.
						</p>
						<!-- 
						ws_id_request
						ws_payment
						ws_status
						-->
						<hr class="lineW mb3" />
						<div class="id_date_main" v-if="ws_payment">
							<div class="id_date">
								<h4>ID: {{ ws_id_request }}</h4>
								<h4>Date: {{ ws_payment.date_create | moment }}</h4>
							</div>
						</div>
						<div class="address mb4" v-if="ws_payment">
							<div class="address_link" v-if="ws_payment.type_pay_client == 1">
								<h5>{{ value | truncate}}</h5>
								<button @click="copyURL(value)">Copy</button>
							</div>
							<div class="address_link" v-if="ws_payment.type_pay_client == 2">
								<a :href="value" target="_blanc">{{ value }}</a>
								<button @click="copyURL(value)">Copy</button>
							</div>
							<qrcode-vue class="address_qr" :value="value" :size="size" level="H" />
						</div>

						<hr class="lineW mb3" />

					</div>
					<div class="main_wait_status mh300">
						<div class="wait_status" v-if="ws_status">
							<h3 class="">STATUS</h3>
							<!-- <button @click="checkStatus">Check manual</button> -->
							<img src="@/assets/loader.gif" alt="" width="60px">


							<h4> STEP - {{ ws_status.stage }} / 7 </h4>
							<h4> MESSAGE - {{ ws_status.message }}</h4>
							<p class="">
								Status change time : 13.07.2022, 14:57 <br />
								The page is updated every 60 seconds.
							</p>

						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import store from "@/store";
import QrcodeVue from 'qrcode.vue'
// import axios from '../../axios'
import moment from 'moment'

export default {
	name: "step-two",
	components: {
		QrcodeVue,
	},
	data() {
		return {
			value: '00...00',
			size: 125,
			type_pay_client: 99, // 99 NOT, 0 CRYPTO, 1 FIAT
			error_getAddress: true,
			error_getAddress_message: '',
			// Info by pair
			selectedPAIR: {
				full_pair: null,
				from_pair: null,
				to_pair: null,
			},
			idRequest: null,
			dateCreate: null,
			// ___________________________________
			ws_id_request: null,
			ws_payment: null,
			ws_status: null
		};
	},
	created: function () {
		// idRequest будет всегда, так как он в УРЛ
		// this.idRequest = this.$route.params.id_request
		// С помощью его делаем запрос на бек, что бы достать pair/dateCreate/АДРЕСС
		// _________________________
		// START CONNECTION WEBSOCKET
		this.startConnection()
	},

	mounted() {
		// this.getAddress()
		this.stepExchange = 2
	},
	filters: {
		moment: function (date) {
			// 10:12:32 12.12.2023
			return moment(date).format('HH:MM:SS DD.MM.YYYY');
			// YYYY-MM-DD H:M:S
		},
		truncate: function (addrs) {
			if (window.screen.width <= 479){
				let reqdString = ''
				let len = addrs.length
				let first = addrs.slice(0,8)
				let second = addrs.slice(len-8,len)
				reqdString = first +"..."+second
				console.log("reqdString",reqdString);
				return reqdString;
			}else{
				return addrs
			}
			
		}
	},
	methods: {
		closeConnect() {
			this.chatSocket.close()
		},
		startConnection() {
			let self = this;

			let url = "ws://" + "127.0.0.1:8000/" + "ws/order-status/" + self.$route.params.id_request

			this.chatSocket = new WebSocket(url)

			this.chatSocket.onopen = () => this.chatSocket.send(JSON.stringify({
				'commands': 'start'
			}));

			this.chatSocket.onmessage = function (e) {
				const data = JSON.parse(e.data);
				// console.log("data -> ", data);
				self.error_getAddress = false
				if (data.isEnd === true) {
					self.$router.push(
						{
							name: "step-4",
							path: `/order/${data.id_request}`,
							params: {
								'id_request': data.id_request,
							}
						})
					self.stepExchange = 4;
					self.closeConnect()
				} else {
					self.ws_id_request = data.id_request
					self.ws_payment = data.payment
					self.ws_status = data.status

					self.value = data.payment.payment_addres
				}

			};
			this.chatSocket.onclose = function (e) {
				const data = JSON.parse(e.data);
				console.log('Chat socket closed unexpectedly', data);
				this.closeConnect()
			};

		},
		copyURL(value) {
			navigator.clipboard.writeText(value);
		},
		// ________________________________________________________________________________
		nextPaid() {
			this.stepExchange = 3;
		},
		manualCloseExchange() {
			this.start_ex = false;
			this.stepExchange = 1
			this.$router.push(
				{
					name: "main",
					path: "/",
				})
		},
		// cancel() {
		// 	let self = this;
		// 	let data = {
		// 		"type_status_exchange": 101,
		// 		"id_request": self.idRequest
		// 	}
		// 	axios.post("/api/v1/private/update-status-exchange/", data)
		// 		.then(function (resp) {
		// 			if (resp.status === 200) {
		// 				// Обнулять
		// 				self.start_ex = false;
		// 				self.stepExchange = 1;
		// 				self.idRequest = null;
		// 				self.date_create = null;
		// 			} else {
		// 				console.log("Error", resp);
		// 			}
		// 		})

		// },
		// getAddress() {
		// 	let self = this;
		// 	// Проверять
		// 	this.stepExchange = 2;
		// 	let data = {
		// 		"id_request": self.idRequest,
		// 	}
		// 	print(data, "datadatadata")
		// 	axios.post("/api/v1/private/payment-data/", data)
		// 		.then(function (resp) {

		// 			if (resp.status === 200) {
		// 				// console.log("STATUS : 200; Doing what u want");
		// 				self.error_getAddress = false
		// 				if (resp.data.type_pay_client === 1) {
		// 					// get ADDRES
		// 					self.value = resp.data.payment_addres
		// 					// get other data
		// 					self.selectedPAIR.full_pair = resp.data.full_pair
		// 					self.selectedPAIR.from_pair = resp.data.from_pair
		// 					self.selectedPAIR.to_pair = resp.data.to_pair
		// 					self.dateCreate = resp.data.date_create
		// 				}
		// 				else if (resp.data.type_pay_client === 2) {
		// 					// get ADDRES
		// 					self.value = resp.data.payment_addres
		// 					// get other data
		// 					self.selectedPAIR.full_pair = resp.data.full_pair
		// 					self.selectedPAIR.from_pair = resp.data.from_pair
		// 					self.selectedPAIR.to_pair = resp.data.to_pair
		// 					self.dateCreate = resp.data.date_create

		// 				} else {
		// 					console.log(99);
		// 				}
		// 			}
		// 		})
		// 		.catch(err => {
		// 			// error_getAddress_message
		// 			if (err.response.status === 400) {
		// 				self.error_getAddress = true
		// 				self.error_getAddress_message = err.response.data.message
		// 				console.log(400);
		// 			}
		// 			else if (err.response.status === 503) {
		// 				self.error_getAddress = true
		// 				self.error_getAddress_message = err.response.data.message
		// 				console.log(503);
		// 			}
		// 			else if (err.response.status === 500) {
		// 				self.error_getAddress = true
		// 				self.error_getAddress_message = err.response.data.message
		// 				console.log(500);
		// 			}
		// 			else {
		// 				self.error_getAddress = true
		// 				self.error_getAddress_message = "Bad Request"
		// 				console.log(999);
		// 			}
		// 		});
		// }
	},
	computed: {
		stepExchange: {
			set: (payload) => store.commit("setStepExchange", payload),
			get: () => store.getters.getStepExchange,
		},
		start_ex: {
			set: (payload) => store.commit("setManualCancel", payload),
			get: () => store.getters.getManualCancel,
		},

	},
};
</script>

<style>
.pay_time h3 {}

.pay_time p {
	font-size: 14px;
	line-height: 18px;
}

.btn_step2 {
	display: flex;
	flex-direction: row;
	justify-content: space-around;
	width: 100%;
}

.lineW {
	width: 100%;
	border: solid 1px #fff;
}

.address {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	width: 100%;
}

.address_link {
	width: 70%;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	justify-content: center;
}

.address_qr {
	width: 30%;
	display: flex;
	flex-direction: column;
	align-items: flex-end;
	justify-content: flex-start;
}

.address_link h5 {
	margin: 0;
	height: 40px;
	font-style: normal;
	font-weight: 400;
	font-size: 18px;
	line-height: 40px;
	padding: 0 2% 0 2%;
	color: #fff !important;
	border: none;
	background-color: rgba(127, 179, 238, 0.5);
	border-radius: 0.990366px;
}

.address_link a {
	margin: 0;
	height: 40px;
	font-style: normal;
	font-weight: 400;
	font-size: 14px;
	width: 100%;
	line-height: 40px;
	padding: 0 2% 0 2%;
	color: #fff !important;
	border: none;
	background-color: rgba(127, 179, 238, 0.5);
	border-radius: 0.990366px;
}

.address_link button {
	border: none;
	background-color: transparent;
	color: rgba(249, 27, 231, 1);;
	cursor: pointer;
	width: 20%;
	font-size: 20px;
	padding: 0;
}

.address_link button:hover {
	border: none;
	background-color: transparent;
	color: #40afff;
	text-decoration: underline;
}

.qr_code_pay_addres {
	display: flex;
	flex-direction: row;
	justify-content: center;
}

.qr_code_pay_addres img {
	width: 30%;
}

/* id_date_main  */
.id_date {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	margin-bottom: 40px;
	font-weight: 700;
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.blockExchange {
		width: 86%;
		padding: 20px 20px;
	}

	.address_link h5 {
		font-size: 16px;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.blockExchange {
		width: 86%;
		padding: 20px 20px;
	}

	.id_date {
		font-size: 14px;
	}

	.address {
		display: flex;
		flex-direction: column;
		justify-content: center;
		width: 100%;
		align-items: center;
	}

	.address_link {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-bottom: 30px;
	}

	.address_qr {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: flex-start;
	}

	.wait_status {
		margin-top: 0;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.blockExchange {
		width: 90% !important;
		padding: 20px 20px;
	}

	.id_date {
		font-size: 16px;
	}

	.address {
		display: flex;
		flex-direction: column;
		justify-content: center;
		width: 100%;
		align-items: center;
	}

	.address_link {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-bottom: 30px;
	}

	.address_qr {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: flex-start;
	}

	.wait_status {
		margin-top: 0 !important;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.blockExchange {
		width: 92% !important;
		padding: 20px 20px;
	}

	.id_date {
		font-size: 16px;
	}

	.address {
		display: flex;
		flex-direction: column;
		justify-content: center;
		width: 100%;
		align-items: center;
	}

	.address_link {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-bottom: 30px;
	}

	.address_qr {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: flex-start;
	}

	.wait_status {
		margin-top: 0 !important;
	}

	.id_date {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		margin-bottom: 30px;
		font-weight: 700;
		height: 50px;
		align-items: flex-start;
	}

	.address_link h5 {
		font-size: 16px;
	}
}

@media (max-width: 479px) {
	.blockExchange {
		width: 100% !important;
		padding: 20px 20px;
	}

	.id_date {
		font-size: 14px;
	}

	.address {
		display: flex;
		flex-direction: column;
		justify-content: center;
		width: 100%;
		align-items: center;
	}

	.address_link {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin-bottom: 30px;
	}

	.address_qr {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: flex-start;
	}

	.wait_status {
		margin-top: 0 !important;
	}

	.id_date {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		margin-bottom: 30px;
		font-weight: 700;
		height: 50px;
		align-items: flex-start;
	}

	.address_link h5 {
		font-size: 14px;
	}
}
</style>
