<template>
	<div class="main_page">
		<div class="central">
			<div class="StartExchange">
				<div class="blockExchange">
					<div class="header_Exchange">
						<div class="close_button_of_form">
							<button style="cursor: pointer" @click="manualCloseExchange">
								&#215;
							</button>
						</div>

						<h3>Exchange {{ selectedPAIR.from_pair }} to {{ selectedPAIR.to_pair }}</h3>

						<ul>
							<li :class="{ activeLi: stepExchange === 1 }">
								<i class="fas fa-pencil-alt"></i>
								<h5>Data input</h5>
							</li>

							<li :class="{ activeLi: stepExchange === 2 }">
								<i class="fas fa-credit-card"></i>
								Payment
							</li>
							<li :class="{ activeLi: stepExchange === 3 }">
								<i class="fas fa-check-double"></i>
								Completion
							</li>
						</ul>
					</div>
					<div class="mh300 enteringValues mb5" v-if="tradesEnabled == true || tradesEnabled == null">
						<div class="attention">
							<i class="fas fa-exclamation"></i>
							<p>
								<span class="weight900">ATTENTION! </span> <br />
								<br />
								This operation takes
								<span class="weight900">place automatically 24/7</span> and
								takes up to <span class="weight900">3 minutes</span> after
								receiving
								<span class="weight900">the first confirmation</span> of the
								transaction. <br /><br />
								• <span class="weight900">Course fixing rules</span>
								<br /><br />
								In order to counter the legalization of proceeds from crime and
								the financing of terrorism, AML checks are carried out in
								accordance with
								<span class="weight900">AML/CTF and KYC Policies</span>
							</p>

						</div>
						<p>CURRENT PRICE : {{ currentPrice }}</p>
						<div class="typeFromTo icons mb2" v-if="full_pair.from_pair">
							<h5>I give</h5>
							<div class="it_input">
								<!-- <img :src="require(`@/assets/currency_icons/png/${full_pair.from_pair}.png`)" alt="" /> -->
								<img :src="require(`@/assets/currency_icons/png/cash.png`)" alt="" />

								<input placeholder="0.004" name="" id="" v-model="amount_FROM"
									@keyup="calcInput_1(amount_FROM)" />
							</div>
							<div class="min_max">
								<h6>Min. {{ full_pair.aboutFROM.min_withdraw }} {{ full_pair.from_pair }}</h6>
								<h6>Max. {{ full_pair.aboutFROM.max_withdraw }} {{ full_pair.from_pair }}</h6>
							</div>
						</div>
						<div class="typeFromTo icons mb2" v-if="full_pair.to_pair">
							<h5>I get</h5>
							<div class="it_input">
								<!-- DYNAMIC IMG https://stackoverflow.com/questions/40491506/vue-js-dynamic-images-not-working -->
								<!-- <img :src="require(`@/assets/currency_icons/png/${full_pair.to_pair}.png`)" alt="" /> -->
								<img :src="require(`@/assets/currency_icons/png/cash.png`)" alt="" />
								<input placeholder="0.004" name="" id="" v-model="amount_TO"
									@keyup="calcInput_2(amount_TO)" />
							</div>
							<div class="min_max">
								<h6>Min. {{ full_pair.aboutTO.min_withdraw }} {{ full_pair.to_pair }}</h6>
								<h6>Max. {{ full_pair.aboutTO.max_withdraw }} {{ full_pair.to_pair }}</h6>
							</div>
						</div>
						<div class="typeFromTo mb2">
							<h5>Address</h5>
							<input placeholder="Address of Wallet" name="" id="" v-model="address_wallet" />
						</div>
						<div class="typeFromTo mb4">
							<h5>Email</h5>
							<input placeholder="test@gmail.com" name="" id="" v-model="email" />
						</div>

						<button class="btn_step1 mb5" @click="next">Next</button>
						<br />
						<br />
						<div class="rules">
							<h4 class="weight900 mb3">
								EXCHANGE ETHEREUM ETH TO ADVANCED CASH USD
							</h4>
							<p class="mb1">
								To make an exchange, you should perform several steps:
							</p>
							<ul class="mb2">
								<li>
									Fill in all fields of the submitted form. Click Exchange.
								</li>
								<li>
									Read the terms of the Agreement for Provision of Exchange
									Services; if you accept them, put a tick in the appropriate
									field and click Create Request.
								</li>
								<li>
									Pay an order. Follow the instructions on our website to
									transfer the required amount.
								</li>
								<li>
									On completion of specified actions, the system will move you
									to the Request Status page, where the status of your
									transfer is displayed.
								</li>
							</ul>
							<p class="mb3 warm_p">
								<i class="fas fa-exclamation"></i> The exchange rate is fixed in
								request if the Customer pays it within 30 minutes after
								creation. If payment is not received within 30 minutes, the
								request is automatically canceled, and to recover the request,
								the Customer should contact the website technical support. In
								this case, the amount of payment on the request may be
								recalculated.
							</p>
							<p class="warm_p">
								<i class="fas fa-exclamation"></i> If the Customer has paid the
								request but due to circumstances wants to refuse the exchange,
								the refund is minus 3% of the payment amount + commission of the
								payment system network and exchange rate difference (if exchange
								rate has changed by more than 3%).
							</p>
						</div>
					</div>
					<div class="mh300 enteringValues mb5" v-if="tradesEnabled == false">
						<div class="attention attention_tradesEnabled">
							<i class="fas fa-exclamation"></i>
							<p class="tradesEnabled">
								<span class="weight900">At the moment, the pair is not available for exchange!! </span>
								<br />
								<br />
								<span class="weight900">Try later!</span>
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
import axios from '../../axios'
export default {
	name: "step-one",
	data() {
		return {
			full_pair: [],
			currentPrice: null,
			firstInputSelected: true,
			// ______models form
			amount_FROM: 0,
			amount_TO: 0,
			address_wallet: "",
			email: "",
			tradesEnabled: null,
			// Info by pair
			selectedPAIR: {
				full_pair: null,
				from_pair: null,
				to_pair: null,
			},
		};
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
		isAuth: {
			set: (payload) => store.commit("setIsAuth", payload),
			get: () => store.getters.getIsAuth,
		},
		isUsername: {
			set: (payload) => store.commit("setIsUsername", payload),
			get: () => store.getters.getIsUsername,
		},

	},
	mounted() {
		
		this.stepExchange = 1
		// Здесь забрать пару из УРЛ, перезаписать и отправить на фронт
		// Или же в () хуярнуть УРЛ
		if (this.$route.params.pair) {
			this.pair = this.$route.params.pair
			this.selectedPAIR.full_pair = this.pair
			let ListPair = this.pair.split("_")
			this.selectedPAIR.from_pair = ListPair[0]
			this.selectedPAIR.to_pair = ListPair[1]

			this.post_receiveInfoPair()
			this.currentPrice_pair()
		} else {
			this.start_ex = false;
			this.stepExchange = 1
		}

	},
	methods: {

		manualCloseExchange() {
			this.$router.push({ name: "main", path: "/" })
			this.start_ex = false;
			this.stepExchange = 1
		},
		next() {
			if (localStorage.getItem("username")){
				this.isUsername = localStorage.getItem("username");
			}else{
				this.isUsername = 'Anonim'
			}
			
			let self = this;
			// Проверять
			let data = {
				"isAuth": this.isAuth, // Попозже передавать ІД юзера и будет пушка
				"isUsername": this.isUsername,
				"amount_from": this.amount_FROM,
				"amount_to": this.amount_TO,
				"address": this.address_wallet,
				"email": this.email,
				"pair_full": this.full_pair.from_pair + "_" + this.full_pair.to_pair,
				"pair_from": this.full_pair.from_pair,
				"pair_to": this.full_pair.to_pair,
				"get_provider": this.full_pair.full_pair,
			}

			axios.post("/api/v1/private/exchange/", data)
				.then(function (resp) {

					if (resp.status === 200) {
						// ТУТ РЕАЛИЗОВАТЬ ПЕРЕХОД с id_request
						self.$router.push(
							{
								name: "step-2",
								path: `/order/${resp.data.id_request}`,
								params: {
									'id_request': resp.data.id_request,
								}
							})
					} else {
						console.log(resp.data);
					}
				})

		},
		calcInput_1: function (value) {
			this.firstInputSelected = true;
			this.calculate(value);
		},
		calcInput_2: function (value) {
			this.firstInputSelected = false;
			this.calculate(value);
		},
		calculate: function (value) {
			if (isNaN(value)) {
				this.amount_FROM = 0;
				this.amount_TO = 0;
				return;
			}

			if (this.firstInputSelected) {
				this.amount_FROM = value;
				this.amount_TO = (value * this.currentPrice).toFixed(6);
			} else {
				this.amount_TO = value;
				this.amount_FROM = (value / this.currentPrice).toFixed(6);
			}
		},
		// REQUESTS
		post_receiveInfoPair() {
			let self = this;
			axios.post("/api/v1/coinlist/", this.selectedPAIR)
				.then(function (resp) {
					self.full_pair = resp.data
				})
		},
		currentPrice_pair() {
			let self = this;
			let full_pair = self.selectedPAIR.full_pair

			axios.get("/api/v1/coinlist/", {
				params: {
					type_pair: 2,
					full_pair: full_pair
				}
			})
				.then(function (resp) {
					self.tradesEnabled = resp.data.tradesEnabled
					self.currentPrice = resp.data.last_price;
				})
		}
	},
};
</script>

<style>
.tradesEnabled {
	text-transform: uppercase;
	text-align: center;
	font-size: 32px;
	line-height: 42px;
}
.attention_tradesEnabled {
	border-top: 1px solid #fff;
	padding-top: 25px;
}
.enteringValues button {
	cursor: pointer;
	background: #ffffff;
	border: 1px solid #ffffff;
	font-style: normal;
	font-weight: 600;
	font-size: 18px;
	color: #2a3587;
	padding: 0 50px;
	height: 40px;
	margin: 0 auto;
}

.enteringValues button:hover {
	background: #2a3587;
	border: 1px solid #ffffff;
	color: #fff;
}

.close_button_of_form {
	width: 100%;
	display: flex;
	flex-direction: row;
	justify-content: flex-end;
}

.typeFromTo {
	width: 100%;
}

.typeFromTo h5 {
	margin: 10px 0px;
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 23px;
}

.typeFromTo input {
	background-size: 30px;
	/* background-position: 98% center; */
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

.it_input {
	position: relative;
}

.it_input img {
	width: 30px;
	position: absolute;
	right: 0;
	top: 5px;
}

.typeFromTo input::placeholder {
	color: #fff;
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 23px;
}

.typeFromTo input:focus {
	outline: none;
}

.typeFromTo input {
	width: 100%;
}

.min_max {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

.min_max h6 {
	margin: 5px 0;
}

/* Attention */
.attention {
	display: flex;
	flex-direction: row;
	align-items: flex-start;
	margin: 25px 0;
	padding-bottom: 25px;
	border-bottom: 1px solid #fff;
}

.attention i {
	font-size: 60px;
	margin-right: 35px;
}

/* rules */
.rules {
	margin: 25px 0;
	padding-top: 25px;
	border-top: 1px solid #fff;
	display: flex;
	flex-direction: column;
}

.rules ul {
	list-style-type: disc;
	padding-left: 20px;
}

.rules ul li {
	font-size: 14px;
	line-height: 18px;
	margin-bottom: 10px;
}

.warm_p i {
	margin-right: 15px;
}

.warm_p {
	font-size: 14px;
	line-height: 18px;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {}

@media (min-width: 768px) and (max-width: 991px) {}

@media (min-width: 480px) and (max-width: 767px) {}

@media (max-width: 479px) {}
</style>
