<template>
	<div class="main_contacts">
		<div class="content_contacts">
			<h1 class="mb3">Web Socket Server</h1>
			<h3> 111{{ params }}</h3>
			<button @click="startConnection">Start Connection</button>
			<button @click="closeConnect">closeConnect</button><br><br>

			<div>
				<!-- <p>LOGS by STAGE - {{ stage }}</p> -->
				<ul v-for="(k, v) in answear_stage" :key="k">
					<li>{{ v }} - {{ k }}</li>
				</ul>

				<h3>ID : {{ ws_id_request }}</h3>
				<br>
				<h4>PAYMENT DATA</h4>
				<ul v-for="(k, v) in ws_payment" :key="k">
					<li>{{ v }} - {{ k }}</li>
				</ul>
				<br>
				<h4>STATUS DATA</h4>
				<ul v-for="(k, v) in ws_status" :key="k">
					<li>{{ v }} - {{ k }}</li>
				</ul>
			</div>
			<!-- </div> -->
			<div v-if="the_end">
				<h3>Прощальное письмо и просьба оставить отзыв!</h3>
			</div>

		</div>

	</div>
</template>

<script>
import store from "@/store";
// import axios from '../axios'

export default {
	name: "WBS",
	components: {},
	data() {
		return {
			chatSocket: null,
			answear_stage: null,
			the_end: false,
			params: null,
			nenaibav: true,
			// ____________
			ws_id_request: null,
			ws_payment: null,
			ws_status: null
		};
	},
	mounted() {
		// this.$route.query.test_second
		// this.params = this.$route.params
		// this.checkTxs()
		this.params = this.$route.fullPath

	},
	methods: {
		// checkTxs() {
		// 	let self = this;
		// 	let data = {
		// 		"test_tx": this.$route.query.id_request
		// 	}
		// 	// test-exchange/
		// 	axios.post("/api/v1/private/test-exchange/", data)
		// 		.then(function (resp) {
		// 			self.nenaibav = resp.data.result

		// 		})
		// },
		closeConnect() {
			this.chatSocket.close()
		},
		startConnection() {
			let self = this;

			let url = "ws://" + "127.0.0.1:8000/" + "ws/order-status/" + self.$route.params.id_request
			// let url = "ws://" + "127.0.0.1:8000/" + "ws/chat/"
			this.chatSocket = new WebSocket(url)

			this.chatSocket.onopen = () => this.chatSocket.send(JSON.stringify({
				'commands': 'start', 'id_request': '8008a2af-f0ec-4ada-86de-925732658008'
			}));

			this.chatSocket.onmessage = function (e) {
				const data = JSON.parse(e.data);
				console.log("data -> ", data);
				if (data.isEnd === true) {
					console.log("i`m here");
					self.the_end = true
				} else {
					self.ws_id_request = data.id_request
					self.ws_payment = data.payment
					self.ws_status = data.status
				}

			};
			this.chatSocket.onclose = function (e) {
				const data = JSON.parse(e.data);
				console.error('Chat socket closed unexpectedly', data);
				this.closeConnect()
			};

		},
	},
	computed: {
		idRequest: {
			set: (payload) => store.commit("setIdRequest", payload),
			get: () => store.getters.getIdRequest,
		},
	},
	// created: function () {
	// 	let self = this;
	// 	let url = "ws://" + "127.0.0.1:8000/" + "ws/chat/"
	// 	this.chatSocket = new WebSocket(url)

	// 	this.chatSocket.onmessage = function (e) {
	// 		const data = JSON.parse(e.data);
	// 		console.log(data);
	// 		self.answear_stage = data.data
	// 		console.log(self.answear_stage);
	// 		document.querySelector('#chat-log').value += (data.data.status + '\n');
	// 	};

	// 	this.chatSocket.onclose = function (e) {
	// 		const data = JSON.parse(e.data);
	// 		console.error('Chat socket closed unexpectedly', data);
	// 	};

	// },
};
</script>
<style>
.main_contacts {
	width: 85%;
	height: 100%;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	background-image: url("../assets/BG_RIGHT.png");
	background-repeat: repeat-y;
	background-position: right;
	background-size: 15%;
	color: #fff;
}

.content_contacts {
	width: 84%;
	margin-bottom: 150px;
}

.content_contacts h1 {
	font-style: normal;
	font-weight: 900;
	font-size: 72px;
	line-height: 83px;
	text-align: left;
}

.content_contacts h3 {
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	line-height: 28px;
}

.block_content_contacts {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

.block_content_contacts_l,
.block_content_contacts_r {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	width: 50%;
	padding: 5%;
}

.block_content_contacts_l input {
	height: 25px;
	width: 100%;
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	line-height: 28px;
	padding: 0;
	color: #fff !important;
	border-bottom: solid 1px #fff !important;
	background-color: transparent;
	box-shadow: none;
	border-color: transparent;
}

.block_content_contacts_l input::placeholder {
	font-weight: 600;
	font-size: 24px;
	line-height: 28px;
	/* identical to box height */

	color: #cccccc;
}

.block_content_contacts_l input:focus {
	outline: none;
}

.block_content_contacts_l button:hover {
	background: #2a3587;
	border: 1px solid #ffffff;
	color: #fff;
}

.block_content_contacts_l button {
	cursor: pointer;
	background: #ffffff;
	border: 1px solid #ffffff;
	font-style: normal;
	font-weight: 600;
	font-size: 22px;
	color: #2a3587;
	padding: 0 50px;
	height: 50px;
	width: 100%;
}

.block_content_contacts_r a {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
	text-decoration: none;
	color: #fff;
	display: flex;
	flex-direction: row;
	align-items: flex-start;
	width: 100%;
}

.block_content_contacts_r a i {
	width: 10%;
	text-align: center;
}

.block_content_contacts_r a span {
	width: 90%;
}
</style>
