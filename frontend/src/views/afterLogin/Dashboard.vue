<template>
	<div class="main_dashboard">
		<UserDashboard />
		<MainDashboard v-if="menu_active == 1" />
		<PaymentDashboard v-if="menu_active == 2" />
		<TransactionDashboard v-if="menu_active == 2" />
		<StatisticDashboard v-if="menu_active == 3" />
		<TwofactorDashboard v-if="menu_active == 4" />
		<p style="color: aliceblue;" v-if="menu_active == 5">
			!!! Позже УДАЛИТЬ!!! <br>
			0. ТЗ <br>
			1. Где-то на этой странице выводит СУММУ которую заработал КЛИЕНТ на реферальной системе <br>
			2. Обозначить мин. сумму на вывод! <br>
			3. Сделать кнопку "Вывести на основной счет" и Реализовать фичу : по которой будет происходит списование с этого счета, и добавление к основному <br><br>
		</p>
		<ReferalsDashboard v-if="menu_active == 5" />
		<PartnershipDashboard v-if="menu_active == 5" />
		<FaqDashboard v-if="menu_active == 6" />
		<div class="main_big">
			<div class="left_of_big">
				<SettingsDashboard v-if="menu_active == 7" />

			</div>
			<div class="right_of_big">
				<LogHistoryDashboard v-if="menu_active == 7" />
			</div>
		</div>

		<!-- будет идея доработать тогда -->

	</div>
</template>

<script>
import PaymentDashboard from "./item_dashboard/payment_dashboard.vue";
import StatisticDashboard from "./item_dashboard/statistic_dashboard.vue";
// __________________________________________________________________________
import FaqDashboard from "./item_dashboard/faq_dashboard.vue";
import ReferalsDashboard from "./item_dashboard/referals_dashboard.vue";
import TransactionDashboard from "./item_dashboard/transaction_dashboard.vue";
import UserDashboard from "./item_dashboard/user_dashboard.vue";
import LogHistoryDashboard from "./item_dashboard/log_history_dashboard.vue";// statistic_dashboard
import PartnershipDashboard from "./item_dashboard/partnership_dashboard.vue";
import TwofactorDashboard from "./item_dashboard/two_factor_avtorization.vue";
import MainDashboard from './item_dashboard/main_dashboard.vue'
import SettingsDashboard from './item_dashboard/settings_dashboard.vue'
// partnership 
import store from "@/store";
export default {
	components: {
		FaqDashboard,
		ReferalsDashboard,
		TransactionDashboard,
		TwofactorDashboard,
		UserDashboard,
		LogHistoryDashboard,
		StatisticDashboard,
		PartnershipDashboard,
		PaymentDashboard,
		MainDashboard,
		SettingsDashboard
	},
	computed: {
		// STORE
		menu_active: {
			set: (payload) => store.commit("setProfileMenuActive", payload),
			get: () => store.getters.getProfileMenuActive,
		},
	},
};
</script>

<style >
.main_dashboard {
	margin-top: 50px;
	width: 100%;
}

.referals h3 {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
}

.main_big {
	width: 100%;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	color: #fff;
}

/* left_of_big
right_of_big */
.left_of_big {
	width: 70%;
	display: flex;
	flex-direction: column;
}

.right_of_big {
	width: 25%;
	display: flex;
	flex-direction: column;
}

.bgcbdr {
	background: rgba(255, 255, 255, 0.1);
	padding: 5%;
	margin-bottom: 50px;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {
	.left_of_big {
		width: 65%;
	}

	.right_of_big {
		width: 30%;
	}

	.referals h3 {
		font-size: 20px;
		line-height: 24px;
	}

	.referals h4 {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.main_dashboard {
		width: 96%;
		padding: 0 2%;
	}

	.left_of_big {
		width: 65%;
	}

	.right_of_big {
		width: 30%;
	}

	.referals h3 {
		font-size: 18px;
		line-height: 24px;
	}

	.referals h4 {
		font-size: 16px;
		line-height: 20px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.main_dashboard {
		width: 96%;
		padding: 0 2%;
	}

	.main_big {
		width: 100%;
		display: flex;
		flex-direction: column-reverse;
		justify-content: space-between;
	}

	.right_of_big {
		width: 100%;
		flex-direction: row-reverse;
		justify-content: space-between;
	}

	.user {
		width: 40%;
	}

	.log_history {
		width: 40%;
	}

	.left_of_big {
		width: 100%;
	}

	.bgcbdr {
		padding: 3%;
	}

	.referals h3 {
		font-size: 16px;
		line-height: 20px;
		font-weight: 700;
	}

	.referals h4 {
		font-size: 14px;
		line-height: 18px;
	}
}

@media (max-width: 479px) {
	.main_dashboard {
		width: 96%;
		padding: 0 2%;
	}

	.main_big {
		width: 100%;
		display: flex;
		flex-direction: column-reverse;
		justify-content: space-between;
	}

	.right_of_big {
		width: 100%;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
	}

	.user {
		width: 80%;
	}

	.log_history {
		width: 80%;
	}

	.left_of_big {
		width: 100%;
	}

	.bgcbdr {
		padding: 3%;
	}

	.referals h3 {
		font-size: 16px;
		line-height: 20px;
		font-weight: 700;
	}

	.referals h4 {
		font-size: 14px;
		line-height: 18px;
	}

}
</style>
