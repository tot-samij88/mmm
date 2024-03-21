<template>
	<div class="main_contacts">
		<div class="content_contacts">
			<h1 class="mb3">Second STEP <br> {{ pair }}</h1>

			<p>Any forms for give data</p>
			<br>

			<button @click="sendData">Start Connection</button>



		</div>
	</div>
</template>

<script>
import store from "@/store";
// import axios from '../axios'
export default {
	name: "TestSecond",
	components: {},
	data() {
		return {
			pair: null,
			chatSocket: null,
			answear_stage: null,
			the_end: false,
		};
	},
	methods: {

		sendData() {
			let self = this;
			self.$router.push(
				{
					path: `/test-exchange/${self.pair}/1488aaaf-f0ec-4ada-86de-a2573265495e`,
				})
			// let data = {
			// 	"pair_full": self.pair
			// }
			// // test-exchange/
			// axios.post("/api/v1/private/test-exchange/", data)
			// 	.then(function (resp) {
			// 		let path = `/test-exchange/${self.pair}/${resp.data.id_request}`
			// 		// /exchange/:pair?/:id_request?
					
			// 		self.$router.push(
			// 			{
			// 				path: path,
			// 			})
			// 		store.commit('setIdRequest', resp.data.id_request);
			// 		store.commit('setDateCreate', resp.data.date_create);

			// 	})
		},

	},
	computed: {
		idRequest: {
			set: (payload) => store.commit("setIdRequest", payload),
			get: () => store.getters.getIdRequest,
		},
	},
	mounted() {
		// this.$route.query.test_second
		this.pair = this.$route.params.pair
	},
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
