<template>
	<div class="main_contacts">
		<div class="content_contacts">
			<h1 class="mb3">First STEP</h1>
			<h6>{{ value }}</h6>
			<button @click="copyURL(value)">COPY</button>
			<p>_______________________________________</p>
			<div style="display:flex">
				<div>
					<h4>SEND</h4>
					<select v-model="selected_left">
						<option v-for="option in select_left" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>
				<div>
					<h4>Receive</h4>
					<select v-model="selected_right">
						<option v-for="option in select_right" :key="option" :value="option">
							{{ option }}
						</option>
					</select>
				</div>
			</div>
			<br>

			<span>Selected: {{ selected_left }} to {{ selected_right }}</span>
			<br>
			<br>
			<p>Start WS</p>
			<button @click="startEx">Start Exchange</button> 
			

			<p>
				{{answear_stage}}
			</p>

		</div>
	</div>
</template>

<script>
// import store from "@/store";

export default {
	name: "TestFirst",
	components: {},
	data() {
		return {
			value:"0x....999",
			select_left:[
				'BTC',
				'ETH',
			],
			select_right: [
				'UAH',
				'USD',
			],
			selected_left:"",
			selected_right:"",
			answear_stage:null
		};
	},
	methods: {
		startEx() {
			let pair = this.selected_left + "_" + this.selected_right
			this.$router.push({ path: "/test-exchange/" + pair, params: { 'pair': pair } })
		},
		copyURL(value) {
			navigator.clipboard.writeText(value);
		}
		
	},
	// computed: {
	// 	idRequest: {
	// 		set: (payload) => store.commit("setIdRequest", payload),
	// 		get: () => store.getters.getIdRequest,
	// 	},
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
