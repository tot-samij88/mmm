<template>
	<div class="faq_dashboard bgcbdr">
		<h3 class="mb3">FAQ</h3>
		<div class="faq_content">
			<div class="faq_left">
				<ul>
					<li v-for="(item_faq, index) in pool_faq" :key="index">
						<h4 @click="show_question(item_faq.id)" :class="{ faq_active: choice_filed === item_faq.id }">
							<i class="fas fa-plus" v-if="choice_filed != item_faq.id"></i>
							<i class="fas fa-minus" v-if="choice_filed === item_faq.id"></i>{{ item_faq.question }}
						</h4>
						<transition name="drop">
							<p v-if="choice_filed === item_faq.id">
								{{ item_faq.answer }}
							</p>
						</transition>
					</li>
				</ul>
			</div>
			<div class="faq_right">
				<h4 class="mb2">
					Didn’t find the answer? <br> You can ask your question here
				</h4>
				<textarea class="mb2" name="" id="" cols="30" rows="10"></textarea>
				<button class="mb2 btn-fill">SEND</button>
			</div>
		</div>
	</div>
</template>

<script>
import axios from '../../../axios';

export default {
	name: "faq-dashboard",
	data() {
		return {
			faq1: false,
			faq2: false,
			faq3: false,
			faq4: false,
			pool_faq: null,
			open_some_filed: false,
			choice_filed: null
		};
	},
	methods: {
		// http://127.0.0.1:8000/api/v1/faq/
		async getFAQ() {
			var self = this
			try {
				await axios.get('/api/v1/faq/', {
					headers: {
						'Content-Type': 'application/json'
					}
				})
					.then(function (response) {
						self.pool_faq = response.data
					})
					.catch(function (error) {
						console.log(error);
					});

			} catch (e) {
				console.error("Error : getFAQ()")
			}
		},
		show_question(id) {
			this.open_some_filed = true
			this.choice_filed = id
		}
	},
	mounted() {
		this.getFAQ();
	}
};
</script>

<style>
/* faq_dashboard
faq_content
faq_left */
.faq_dashboard {
	color: #fff;
}

.faq_dashboard h3 {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
}

.faq_content {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	width: 100%;
}

.faq_left {
	width: 70%;
}

.faq_left ul {
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;

	justify-content: space-between;
}

.faq_left ul li {
	width: 48%;
	margin-bottom: 50px;
}

.faq_left ul li h4 {
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 24px;
	margin-bottom: 20px;
	cursor: pointer;
}

.faq_left ul li h4:hover {
	color: rgba(249, 27, 231, 1);;
}

.faq_active {
	color: rgba(249, 27, 231, 1);;
}

.faq_left ul li h4 i {
	margin-right: 10px;
}

.faq_left ul li p {
	font-style: normal;
	font-weight: 400;
	font-size: 16px;
	line-height: 24px;
	max-height: 500px;
}

/* Animation */
.drop-enter,
.drop-leave-to {
	transform: translateY(-20%);
	opacity: 0;
}

.drop-enter-active {
	transition: all 0.3s ease;
}

.drop-leave-active {
	transition: all 0.3s ease;
}

.faq_right {
	width: 25%;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	justify-content: flex-start;
}

.faq_right h4 {
	font-style: normal;
	font-weight: 500;
	font-size: 18px;
	line-height: 22px;
}

.faq_right textarea {
	background-color: transparent;
	height: 70px;
	width: 92%;
	font-style: normal;
	font-weight: 400;
	font-size: 14px;
	line-height: 23px;
	padding: 3%;
	color: #fff !important;
	border: solid 1px #fff !important;
}

.faq_right textarea::placeholder {
	color: #fff;
	font-style: normal;
	font-weight: 400;
	font-size: 14px;
}

.faq_right textarea:focus {
	outline: none;
}

.faq_right button {
	/* font-style: normal;
	font-weight: 600;
	font-size: 20px;
	color: #2a3587;
	background: #fff;
	border: none; */
	min-width: 100%;
	/* padding: 10px 0;
	cursor: pointer;
	border: solid 1px #fff; */
}


@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {
	.faq_dashboard h3 {
		font-size: 20px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.faq_dashboard h3 {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.faq_dashboard h3 {
		font-size: 18px;
		line-height: 24px;
		font-weight: 700;
	}

	.faq_content {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 100%;
		align-items: center;
		margin-bottom: 30px;
	}

	.faq_left {
		width: 90%;
	}

	.faq_left ul li h4 {
		font-size: 16px;
		line-height: 24px;
		margin-bottom: 20px;
		text-align: center;
	}

	.faq_left ul li p {
		font-size: 14px;
		line-height: 18px;
		text-align: center;
	}

	.faq_right {
		width: 90%;
	}

	.faq_right h4 {
		font-size: 16px;
		line-height: 20px;
	}

	.faq_right button {
		min-width: 33%;
		margin: 0 auto;
	}
}

@media (max-width: 479px) {
	.faq_dashboard h3 {
		font-size: 16px;
		line-height: 20px;
		font-weight: 700;
	}

	.faq_content {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 100%;
		align-items: center;
		margin-bottom: 30px;
	}

	.faq_left {
		width: 90%;
	}

	.faq_left ul li h4 {
		font-size: 16px;
		line-height: 24px;
		margin-bottom: 20px;
		text-align: center;
	}

	.faq_left ul li p {
		font-size: 14px;
		line-height: 18px;
		text-align: center;
	}

	.faq_right {
		width: 90%;
	}

	.faq_right h4 {
		font-size: 16px;
		line-height: 20px;
	}

	.faq_right button {
		min-width: 30%;
		margin: 0 auto;
	}
}
</style>
