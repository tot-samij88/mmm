<template>
	<div class="log_history bgcbdr">
		<h3 class="mb3">Login history</h3>
		<ul class="list_log_history">
			<li v-for="item in history" :key="item.id">
				<h3>{{ item.date | moment }}</h3>
				<h4>{{ item.user_ip }}</h4>
				<h4>{{ item.user_agent }}</h4>
			</li>
		</ul>
	</div>
</template>

<script>
import axios from '../../../axios';
import moment from 'moment'

export default {
	name: "log-history-dashboard",
	data() {
		return {
			history: Array,
		}
	},
	filters: {
		moment: function (date) {
			return moment(date).format('HH:MM DD.MM.YYYY');
			// YYYY-MM-DD H:M:S
		}
	},
	methods: {
		async getLogHist() {
			var self = this
			try {
				await axios.post('/auth/get_logging_history/', {
					headers: {
						'Content-Type': 'application/json'
					},
					data: {
						username: localStorage.getItem('username')
					}
				})
					.then(function (response) {
						var histiry = response.data
						self.history = JSON.parse(JSON.stringify(histiry))
					})
					.catch(function (error) {
						console.log(error);
					});

			} catch (e) {
				alert('Error')
			}
		}
	},
	mounted() {
		this.getLogHist();
	}
};
</script>

<style>
.log_history {
	display: flex;
	flex-direction: column;
	align-items: center;
	color: #fff;
}

.log_history h3 {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
}

.list_log_history li {
	margin-bottom: 20px;
	font-weight: normal !important;
}

.list_log_history h3 {
	font-style: normal;
	font-weight: 400;
	font-size: 24px;
	line-height: 28px;
}

.list_log_history h4 {
	font-style: normal;
	font-weight: 400;
	font-size: 16px;
	line-height: 18px;
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.list_log_history h3 {
		font-size: 18px;
		line-height: 24px;
	}

	.list_log_history li {
		margin-bottom: 15px;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.list_log_history h3 {

		font-size: 16px;
		line-height: 18px;
	}

	.list_log_history li {
		margin-bottom: 15px;
	}

	.log_history h3 {
		font-size: 20px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.list_log_history h3 {

		font-size: 16px;
		line-height: 18px;
	}

	.list_log_history li {
		margin-bottom: 15px;
	}

	.log_history h3 {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.list_log_history h3 {

		font-size: 14px;
		line-height: 18px;
		font-weight: normal !important;
	}

	.list_log_history li {
		margin-bottom: 15px;
		font-size: 14px;
	}

	.log_history h3 {
		font-size: 18px;
		line-height: 20px;
	}
}

@media (max-width: 479px) {
	.list_log_history h3 {

		font-size: 14px;
		line-height: 18px;
		font-weight: normal !important;
	}

	.list_log_history li {
		margin-bottom: 15px;
		font-size: 14px;
	}

	.log_history h3 {
		font-size: 18px;
		line-height: 20px;
	}
}
</style>
