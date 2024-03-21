<template>
	<div class="bgcbdr">
		
		<div style="margin-bottom: 50px;">
			
			<a class="btn-fill " @click="openPaymentForm">
				vvod sredstv
			</a>
		</div>

		<!-- <h4 v-if="isListToLoading">Loading...</h4>
		<div v-if="!isListToLoading">
			<ul v-for="(item, index) in test_data" :key="index">
				<li>{{ item }}</li>
			</ul>
		</div> -->
		
		<button @click="get_statistic">давай проверим?</button>
		<h4 v-if="isListToLoading">Loading...</h4>
		<div class="main_statistic" v-if="test_data && !isListToLoading">
			<div class="main_statistic_header">
				<div class="item_header">
					<h3 class="item_header_key">ID</h3>
					<h3 class="item_header_value">{{ test_data.id }}</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Name</h3>
					<h3 class="item_header_value">{{ test_data.name }}</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Доход</h3>
					<h3 class="item_header_value">{{ test_data.current_profit }}</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Доход в день</h3>
					<h3 class="item_header_value">{{ test_data.current_profit / 10 }}</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Статус</h3>
					<h3 class="item_header_value" v-if="test_data.is_enabled == true">Работает</h3>
					<h3 class="item_header_value" v-if="test_data.is_enabled == false">Остановлен</h3>
				</div>
			</div>
			<div class="main_statistic_body">
				<div class="main_statistic_left">
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Пара</h3>
						<h3 class="main_statistic_left_item_value">{{ test_data.pair }}</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Дата создания</h3>
						<h3 class="main_statistic_left_item_value">{{ test_data.created_at }}</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Верх цена</h3>
						<h3 class="main_statistic_left_item_value">{{ test_data.upper_price }}</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Низ цена</h3>
						<h3 class="main_statistic_left_item_value">{{ test_data.lower_price }}</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Выполеных сделок</h3>
						<h3 class="main_statistic_left_item_value">{{ test_data.total_profits_count }}</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">В ордерах</h3>
						<h3 class="main_statistic_left_item_value">{{test_data.investment_base_currency}} {{ test_data.pair | pair_from }} <br> {{test_data.investment_quote_currency}} {{ test_data.pair | pair_to}}</h3>
					</div>
				</div>
				<div class="main_statistic_right" >
					<h4>Доходы</h4>
					<div class="main_statistic_right_item" v-for="(item, index) in test_data.profit" :key="index">
						<h3 class="date">{{item.created_at | moment}}</h3>
						<h3 class="amount">+{{item.profit}}</h3>
					</div>
				</div>
			</div>
		</div>
		<div class="main_statistic" v-if="!test_data && !isListToLoading">
			<div class="main_statistic_header">
				<div class="item_header">
					<h3 class="item_header_key">ID</h3>
					<h3 class="item_header_value">100999</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Name</h3>
					<h3 class="item_header_value">NameBot</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Доход</h3>
					<h3 class="item_header_value">0.00</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Доход в день</h3>
					<h3 class="item_header_value">0.00</h3>
				</div>
				<div class="item_header">
					<h3 class="item_header_key">Статус</h3>
					<h3 class="item_header_value">Не Работает</h3>
				</div>
			</div>
			<div class="main_statistic_body">
				<div class="main_statistic_left">
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Пара</h3>
						<h3 class="main_statistic_left_item_value">Не выбрано</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Дата создания</h3>
						<h3 class="main_statistic_left_item_value">Не создано</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Верх цена</h3>
						<h3 class="main_statistic_left_item_value">0.00</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Низ цена</h3>
						<h3 class="main_statistic_left_item_value">0.00</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">Выполеных сделок</h3>
						<h3 class="main_statistic_left_item_value">0</h3>
					</div>
					<div class="main_statistic_left_item">
						<h3 class="main_statistic_left_item_key">В ордерах</h3>
						<h3 class="main_statistic_left_item_value">0.00 <br> 0.00</h3>
					</div>
				</div>
				<div class="main_statistic_right" >
					<h4>Доходы</h4>
					<div class="main_statistic_right_item">
						<h3 class="date">2023</h3>
						<h3 class="amount">+0.00</h3>
					</div>
				</div>
			</div>
		</div>

		<div class="example" style=" display: flex; flex-direction: row; justify-content: center; ">
			<img src="@/assets/want-it.png" alt="" style=" width: 60%; ">
		</div>
	</div>
</template>

<script>
// import store from "@/store";
import axios from '../../../axios'
import moment from 'moment'
export default {
	name: "Home",
	components: {},
	data() {
		return {
			isListToLoading:false,
			full_data: null,
			// test_data: {
			// 	"id": 1941438,
			// 	"is_enabled": true,
			// 	"created_at": "2023-03-13T16:27:33.670Z",
			// 	"lower_price": "2.232",
			// 	"upper_price": "3.205",
			// 	"name": "For API",
			// 	"pair": "BUSD_DYDX",
			// 	"current_profit": "47.53807817",
			// 	"current_profit_usd": "47.53807817",
			// 	"total_profits_count": "1024",
			// 	"profit_percentage": "5.9375370967147829469158237176519408702612389674415735",
			// 	'investment_base_currency': '114.892517974180151072653481097',
			// 	'investment_quote_currency': '472.397',
			// 	"profit": [
			// 		{
			// 			"grid_line_id": 228078365,
			// 			"profit": "0.04404",
			// 			"usd_profit": "0.04404",
			// 			"created_at": "2023-03-18T21:10:09.425Z",
			// 			"grid_line": {
			// 				"id": 228078365,
			// 				"price": "2.753",
			// 				"side": "sell",
			// 				"order_placed": true
			// 			}
			// 		},
			// 		{
			// 			"grid_line_id": 228078365,
			// 			"profit": "0.04404",
			// 			"usd_profit": "0.04404",
			// 			"created_at": "2023-03-18T21:10:09.425Z",
			// 			"grid_line": {
			// 				"id": 228078365,
			// 				"price": "2.753",
			// 				"side": "sell",
			// 				"order_placed": true
			// 			}
			// 		},
			// 		{
			// 			"grid_line_id": 228078365,
			// 			"profit": "0.04404",
			// 			"usd_profit": "0.04404",
			// 			"created_at": "2023-03-18T20:41:15.627Z",
			// 			"grid_line": {
			// 				"id": 228078365,
			// 				"price": "2.753",
			// 				"side": "sell",
			// 				"order_placed": true
			// 			}
			// 		}
			// 	]
			// }
			test_data:null
		};
	},
	computed: {
		// STORE
		// selectedPAIR: {
		// 	set: (payload) => store.commit("setSelectedPAIR", payload),
		// 	get: () => store.getters.getSelectedPAIR,
		// },
	},

	mounted() {

	},
	filters:{
		pair_to(fullpair){
			var nameList = fullpair.split("_");
			return nameList[0]
		},
		pair_from(fullpair){
			var nameList = fullpair.split("_");
			return nameList[1]
		},
		moment: function (date) {
			// 10:12:32 12.12.2023
			return moment(date).format('DD.MM.YYYY H:MM');
			// YYYY-MM-DD H:M:S
		},
	},
	methods: {
		openPaymentForm() {
			this.$router.push({ name: "payment", path: "/payment" }).catch(() => { });
		},
		get_statistic() {
			this.isListToLoading = true
			// console.log("from_pair", from_pair);
			let self = this;
			axios.post("/api/v1/private/statistic/", {
				headers: {
					'Content-Type': 'application/json'
				},
				data: {
					"username": localStorage.getItem('username')
				}
			})
				.then(function (resp) {
					console.log(resp.data);
					self.test_data = resp.data
					self.isListToLoading = false
				})
		},



	},
};
</script>
<style>
/* test */
.donate-with-crypto{
	font-size: 18px;
	line-height: 28px;
	color: #fff;
	background-color: black;
	padding: 15px 40px;
	border-radius: 15px;
	text-decoration: none;
	cursor: pointer;
}
.main_page {
	width: 100%;
	padding: 5%;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}
/* ========================= */
.main_statistic{
	border-radius: 5px;
    width: 100%;
    padding: 0%;
    display: flex;
    margin: 5% 0;
    flex-direction: column;
    color: #fff;
}
.main_statistic_header{
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	border: solid 3px rgba(249, 27, 231, 1);
	border-radius: 5px;
	padding: 2% 1%;
}
.item_header{
	display: flex;
	flex-direction: column;
	align-items: center;
}
.item_header_key{
	font-size: 20px;
	line-height: 32px;
	font-weight: 700;
}
.item_header_value{
	font-size: 20px;
	line-height: 32px;
}
/* ========================= */
.main_statistic_body{
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	padding: 2% 1% 5% 1%;
	border: solid 3px rgba(249, 27, 231, 1);
	margin-top: 20px;
	border-radius: 5px;
}
.main_statistic_left{
	width: 60%;
	display: flex;
	flex-direction: column;
}
.main_statistic_right{
	width: 40%;
	display: flex;
	flex-direction: column;
	max-height: 360px;
    overflow-y: scroll;
    padding-right: 2%;
}
.main_statistic_left_item{
	display: flex;
	flex-direction: column;
	height: 40px;
	justify-content: space-between;
	margin-bottom: 20px;
}
.main_statistic_left_item_key{
	font-size: 18px;
	line-height: 28px;
	font-weight: 700;
}
.main_statistic_left_item_value{
	font-size: 18px;
	line-height: 28px;
}
/* 
main_statistic_right_item
date
amount */
.main_statistic_right h4{
	font-size: 18px;
	line-height: 28px;
	font-weight: 700;
}
.main_statistic_right_item{
	margin-top: 10px;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}
.date{
	font-size: 18px;
	line-height: 28px;
}
.amount{
	font-size: 18px;
	line-height: 28px;
	color: rgba(249, 27, 231, 1);
}
@media (min-width: 1200px) and (max-width: 1440px) {
	.Pair img {
		width: 30px;
		height: 30px;
	}

	.item_block_left_name h5 {
		margin-left: 5px;
	}

	.item_crypto {
		padding: 10px 5px;
		margin-top: 20px;
	}

	.item_block_left_name h5,
	.item_block_right h5 {
		font-size: 16px;
	}

	.type_glasses {
		font-size: 24px;
		margin-top: 20px;
	}

	.list_crypto {
		padding: 0 15px;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.Pair img {
		width: 30px;
		height: 30px;
	}

	.item_block_left_name h5 {
		margin-left: 5px;
	}

	.item_crypto {
		padding: 10px 5px;
		margin-top: 20px;
	}

	.item_block_left_name h5,
	.item_block_right h5 {
		font-size: 16px;
	}

	.type_glasses {
		font-size: 24px;
		margin-top: 20px;
	}

	.list_crypto {
		padding: 0 15px;
	}

	/* HEADER OF FORM */
	.header_Exchange h3 {
		font-size: 28px;
		line-height: 36px;
		margin: 0px 0 15px 0;
	}

	.header_Exchange ul li {
		font-size: 16px;
	}

	.enteringValues {
		width: 90%;
	}

	.attention i {
		font-size: 42px;
		margin-right: 24px;
	}

	.attention p {
		font-size: 16px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.main_page {
		padding-left: 2%;
		width: 98%;
		height: 100%;
		background-image: none;
	}

	.Pair img {
		width: 30px;
		height: 30px;
	}

	.item_block_left_name h5 {
		margin-left: 5px;
	}

	.item_crypto {
		padding: 10px 5px;
		margin-top: 20px;
	}

	.item_block_left_name h5,
	.item_block_right h5 {
		font-size: 16px;
	}

	.type_glasses {
		font-size: 24px;
		margin-top: 20px;
	}

	.list_crypto {
		padding: 0 15px;
	}

	.central {
		width: 98%;
		margin-bottom: 100px;
	}

	.NextStart button {
		font-size: 28px;
		padding: 10px 40px;
	}

	/* HEADER OF FORM */
	.header_Exchange h3 {
		font-size: 28px;
		line-height: 36px;
		margin: 0px 0 15px 0;
	}

	.header_Exchange ul li {
		font-size: 16px;
	}

	.enteringValues {
		width: 92%;
	}

	.attention i {
		font-size: 36px;
		margin-right: 18px;
	}

	.attention p {
		font-size: 14px;
		line-height: 18px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.Pair {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
	}

	.PairBlock {
		width: 75%;
		margin-bottom: 50px;
	}

	.main_page {
		padding-left: 2%;
		width: 98%;
		height: 100%;
		background-image: none;
	}

	.Pair img {
		width: 30px;
		height: 30px;
	}

	.item_block_left_name h5 {
		margin-left: 5px;
	}

	.item_crypto {
		padding: 10px 5px;
		margin-top: 20px;
	}

	.item_block_left_name h5,
	.item_block_right h5 {
		font-size: 15px;
		font-weight: bold;
	}

	.type_glasses {
		font-size: 24px;
		margin-top: 20px;
	}

	.list_crypto {
		padding: 0 15px;
	}

	.central {
		width: 98%;
		margin-bottom: 50px;
	}

	.NextStart {
		margin-top: 0;
	}

	.NextStart button {
		font-size: 24px;
		padding: 10px 30px;
	}

	/* BIG PART OF FORM */
	.blockExchange {
		width: 96%;
		padding: 10px 10px;
	}

	.StartExchange {
		background-size: 96%;
	}

	.header_Exchange h3 {
		font-size: 18px;
		line-height: 28px;
		margin: 0px 0 15px 0;
	}

	.header_Exchange ul li {
		font-size: 14px;
	}

	.enteringValues {
		width: 92%;
	}

	.attention i {
		font-size: 36px;
		margin-right: 18px;
	}

	.attention p {
		font-size: 14px;
		line-height: 18px;
	}

	.header_Exchange button {
		font-size: 50px;
	}

	.header_Exchange ul {
		justify-content: space-between;
	}

	.typeFromTo h5 {
		margin: 5px 0px;
		font-size: 18px;
		line-height: 18px;
	}
}

@media (max-width: 479px) {
	.Pair {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
	}

	.PairBlock {
		width: 90%;
		margin-bottom: 50px;
	}

	.main_page {
		padding-left: 2%;
		width: 98%;
		height: 100%;
		background-image: none;
	}

	.Pair img {
		width: 20px;
		height: 20px;
	}

	.item_block_left_name h5 {
		margin-left: 5px;
	}

	.item_crypto {
		padding: 10px 5px;
		margin-top: 10px;
	}

	.item_block_left_name h5,
	.item_block_right h5 {
		font-size: 12px;
		font-weight: bold;
	}

	.type_glasses {
		font-size: 18px;
		margin-top: 10px;
	}

	.list_crypto {
		padding: 0 10px;
	}

	.central {
		width: 98%;
		margin-bottom: 50px;
	}

	.NextStart {
		margin-top: 0;
	}

	.NextStart button {
		font-size: 24px;
		padding: 10px 30px;
	}

	/* font-weight: bold; */
	.item_block_right h5 {
		font-weight: bold;
	}

	/* HEADER OF FORM */
	.blockExchange {
		width: 98%;
		padding: 10px 5px;
	}

	.StartExchange {
		background-size: 96%;
	}

	.header_Exchange h3 {
		font-size: 16px;
		line-height: 24px;
		margin: 0px 0 15px 0;
	}

	.header_Exchange ul li {
		display: flex;
		flex-direction: row;
		align-items: center;
		font-style: normal;
		font-weight: 500;
		line-height: 21px;
		font-size: 14px;
		padding: 10px 10px 5px 10px;
		border-bottom: 2px solid;
		width: 40%;
		justify-content: center;
	}

	.enteringValues {
		width: 100%;
	}

	.attention i {
		font-size: 28px;
		margin-right: 10px;
	}

	.attention p {
		font-size: 10px;
		line-height: 14px;
	}

	.header_Exchange button {
		font-size: 40px;
	}

	.header_Exchange ul {
		display: flex;
		flex-direction: column;
		/* justify-content: space-evenly; */
		list-style-type: none;
		color: #fff;
		align-items: center;
	}

	.typeFromTo h5 {
		margin: 5px 0px;
		font-size: 14px;
		line-height: 18px;
	}

	.min_max h6 {
		margin: 5px 0;
		font-size: 14px;
		line-height: 18px;
	}

	.typeFromTo input {
		font-size: 12px;
	}

	.rules {
		font-size: 12px;
		line-height: 18px;
	}

	.rules p {
		font-size: 12px;
		line-height: 14px;
	}

	.rules ul li {
		font-size: 12px;
		line-height: 14px;
		margin-bottom: 5px;
	}
}
</style>
