<template>
	<div class="main_wait_status mh300">
		<div class="wait_status">
			<!-- <button @click="checkStatus">Check manual</button> -->
			<img src="@/assets/loader.gif" alt="" width="60px">
			<h3 class="">STATUS</h3>

			<div v-for="(k, v) in answear_stage" :key="k">
				<h4><span class="weight900">{{ k }} - {{ v }}</span></h4>
			</div>

			<!-- <p class="">
				Status change time : 13.07.2022, 14:57 <br />
				The page is updated every 60 seconds.
			</p> -->

		</div>
	</div>
</template>

<script>
import store from "@/store";
// import axios from '../../axios'
export default {
	name: "step-three",
	data() {
		return {
			// status_code: 2,
			// confirmations: null,
			// transactionMethod: "",
			// status_message: "Starting...",
			// intervalCheckStatus: null,
			// fullWithdraw:null
			chatSocket: null,
			answear_stage: null
		};
	},
	created: function () {
		// Explain
		// const chatSocket = new WebSocket(
		// 	'ws://'
		// 	+ window.location.host
		// 	+ '/ws/chat/'
		// 	+ roomName    | id_request и на стороне Бека получать его. Профит =)
		// 	+ '/'
		// );
		let self = this;
		// let url = "ws://" + "127.0.0.1:8000/" + "ws/chat/"
		let url = "ws://" + "127.0.0.1:8000/" + "ws/test/"
		this.chatSocket = new WebSocket(url)
		console.log(this.chatSocket);
		this.chatSocket.onopen = () => this.chatSocket.send(JSON.stringify({
			'next': '1', "id_request": self.idRequest
		}));

		this.chatSocket.onmessage = function (e) {
			const data = JSON.parse(e.data);
			console.log(data);
			// if (data.health) {
			// 	self.health = data.health
			// }
			// self.stage = data.stage
			// self.answear_stage = data
			// ____ N E W ______
			self.answear_stage = data
			if (data.current_stage == 2000) {
				self.stepExchange = 4;
				self.closeConnect()
			}
		};
		this.chatSocket.onclose = function (e) {
			const data = JSON.parse(e.data);
			console.error('Chat socket closed unexpectedly', data);
			this.closeConnect()
		};
	},
	methods: {
		closeConnect() {
			this.chatSocket.close()
		},
		// Проверка для Депозита
		// checkTX_Deposite() {
		// 	// let self = this;
		// 	this.chatSocket.send(JSON.stringify({
		// 		'next': '1',
		// 		"id_request": "3ef0d64b-c684-4b24-a216-6d07994749a8"
		// 	}));
		// },
		// // Интервал для Депозита
		// intervalcheckTX_Deposite: function () {
		// 	setInterval(() => {
		// 		this.checkTX_Deposite()
		// 	}, 60 * 1000)
		// },
		// // Проверка для выплаты 
		// checkTX_Withdraw() {
		// 	// let self = this;
		// 	this.chatSocket.send(JSON.stringify({
		// 		'next': '4',
		// 		"id_request": "3ef0d64b-c684-4b24-a216-6d07994749a8"
		// 	}));
		// },
		// // Интервал для выплаты
		// intervalcheckTX_Withdraw: function () {
		// 	setInterval(() => {
		// 		this.checkTX_Withdraw()
		// 	}, 60 * 1000)
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
		idRequest: {
			set: (payload) => store.commit("setIdRequest", payload),
			get: () => store.getters.getIdRequest,
		},
		dateCreate: {
			set: (payload) => store.commit("setDateCreate", payload),
			get: () => store.getters.getDateCreate,

		},
	},
	// watch: {

	// 	'stage': function (newValue) {

	// 		if (newValue === 2) {
	// 			// let self = this;
	// 			// чистим сетИнтервал
	// 			clearInterval(this.intervalcheckTX_Deposite)
	// 			// переходит к след Этапу TransferSwapTransfer
	// 			this.chatSocket.send(JSON.stringify({
	// 				'next': '2', "id_request": "3ef0d64b-c684-4b24-a216-6d07994749a8"
	// 			}));
	// 		}
	// 		if (newValue === 3) {
	// 			// let self = this;
	// 			// переходит к след Этапу Withdraw
	// 			this.chatSocket.send(JSON.stringify({
	// 				'next': '3', "id_request": "3ef0d64b-c684-4b24-a216-6d07994749a8"
	// 			}));
	// 		}
	// 		if (newValue === 4) {
	// 			// let self = this;
	// 			// переходит к след Этапу Withdraw
	// 			this.chatSocket.send(JSON.stringify({
	// 				'next': '4', "id_request": "3ef0d64b-c684-4b24-a216-6d07994749a8"
	// 			}));
	// 		}
	// 		if (newValue === 5) {
	// 			// let self = this;
	// 			// переходит к след Этапу Withdraw
	// 			this.chatSocket.send(JSON.stringify({
	// 				'next': '5', "id_request": "3ef0d64b-c684-4b24-a216-6d07994749a8"
	// 			}));
	// 		}
	// 		if (newValue === 6) {
	// 			// переходит к след Этапу CheckTX WITHDRAW
	// 			this.intervalcheckTX_Withdraw()
	// 		}
	// 		if (newValue === 7) {
	// 			clearInterval(this.intervalcheckTX_Withdraw) //WITHDRAW
	// 			this.stepExchange = 4; // Переход на прощальную страничку
	// 			this.closeConnect()
	// 		}
	// 	},
	// },
};
</script>

<style>
.main_wait_status {
	display: flex;
	flex-direction: column;
	justify-content: center;
	width: 85%;
	margin: 0 auto;
	color: #fff;
}

.wait_status {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	height: 300px;
	align-items: center;
	margin-top: 50px;
}

.wait_status h3 {
	line-height: 24px;
	font-size: 24px;
}

.wait_status p {
	line-height: 24px;
	font-size: 14px;
}
</style>
