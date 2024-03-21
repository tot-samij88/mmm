<template>
	<div class="transaction bgcbdr">
		<h3 class="mb3">Resent transactions</h3>
		<div>
			<vue-table-dynamic :params="params" style="text-align: center !important;"></vue-table-dynamic>
		</div>
		<!-- 
			https://github.com/TheoXiong/vue-table-dynamic
			https://theoxiong.github.io/vue-table-dynamic/
		-->
	</div>
</template>

<script>
import axios from '../../../axios';
import store from "@/store";
import VueTableDynamic from 'vue-table-dynamic'
export default {
	name: "transaction-dashboard",
	components: { VueTableDynamic },
	data() {
		return {
			params: null
		}
	},
	mounted() {
		this.get_history_client_tx()
	},
	computed: {
		isUsername: {
			set: (payload) => store.commit("setIsUsername", payload),
			get: () => store.getters.getIsUsername,
		},

	},
	methods: {
		get_history_client_tx() {
			if (localStorage.getItem("username")) {
				this.isUsername = localStorage.getItem("username");
			} else {
				this.isUsername = 'Anonim'
			}
			let self = this;
			// Проверять
			let data = {
				"username": this.isUsername
			}

			axios.post("/api/v1/private/history-client-tx/", data)
				.then(function (resp) {
					if (resp.data) {
						console.log(resp.data);
						// ТУТ РЕАЛИЗОВАТЬ ПЕРЕХОД с id_request
						self.params = resp.data
					} else {
						console.log(resp.data);
					}
				})
		}
	}
};
</script>

<style>
/* Custom style table */
.v-table-row {
	border-bottom: 1px solid #fff !important;
	background-color: transparent !important;
	color: #fff !important;
	font-size: 16px !important;
}

.v-table:before {
	border-bottom: none !important;
}

.transaction {
	color: #fff;
	width: 90%;
}

.transaction h3 {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
}

.list_trans {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

.list_trans ul {
	width: 33%;
	list-style-type: none;
	text-align: center;
	padding: 0;
}

.list_trans ul li {
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 32px;
}

.name_col {
	font-style: normal;
	font-weight: 400;
	font-size: 24px;
	line-height: 28px;
	color: #cccccc;
	border-bottom: 1px solid #ccc;
	padding-bottom: 5px;
	margin-bottom: 10px;
	text-align: center;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {
	.transaction h3 {
		font-size: 20px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.transaction h3 {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.transaction h3 {
		font-size: 18px;
		line-height: 24px;
		font-weight: 700;
	}
}

@media (max-width: 479px) {
	.transaction h3 {
		font-size: 16px;
		line-height: 20px;
		font-weight: 700;
	}

	.v-table-row {
		border-bottom: 1px solid #fff !important;
		background-color: transparent !important;
		color: #fff !important;
		font-size: 13px !important;
	}
}
</style>
