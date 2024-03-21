<template>
	<div class="main_page">
		<div class="central">
			<div class="StartExchange">
				<div class="blockExchange">
					<div class="header_Exchange">
						<button style="cursor: pointer" @click="manualCloseExchange">
							&#215;
						</button>

						<h3>Exchange completed successfully</h3>

						<ul>
							<li>
								<i class="fas fa-pencil-alt"></i>
								<h5>Data input</h5>
							</li>

							<li>
								<i class="fas fa-credit-card"></i>
								Payment
							</li>

							<li class="activeLi">
								<i class="fas fa-check-double"></i>
								Completion
							</li>
						</ul>
					</div>
					<div class="main_completion mh300">
						<h2>Thank you for using our service</h2>
						<h3>You can leave a review here <span>click</span></h3>
						<h3>
							For registered users there is a discount on the commission and many
							other goodies.
						</h3>
						<p>Заебися пахне пися :) </p>
						<h4>
							Forms for reviews
						</h4>
						<p>
							Можно отправлять запрос, по ИД, что бы точно описать завершение обмена
						</p>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import store from "@/store";
export default {
	name: "step-four",
	data() {
		return {};
	},
	methods: {
		manualCloseExchange() {
			this.$router.push({ name: "main", path: "/" })
			this.start_ex = false;
			this.stepExchange = 1
		},
	},
	computed: {
		stepExchange: {
			set: (payload) => store.commit("setStepExchange", payload),
			get: () => store.getters.getStepExchange,
		},
	},
	mounted() {
		this.stepExchange = 3
	},
};
</script>

<style>
.main_completion {
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	width: 100%;
	margin: 0 auto;
	color: #fff;
	text-align: center;
}

.main_completion h2 {
	font-size: 24px;
	font-weight: 700;
	line-height: 36px;
}

.main_completion h3 {
	font-size: 18px;
	font-weight: 500;
	line-height: 28px;
}
</style>
