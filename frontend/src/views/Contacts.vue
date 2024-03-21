<template>
	<div class="main_contacts">
		<div class="content_contacts">
			<h1 class="mb3">Contacts</h1>
			<h3>
				Feel free to contact us any time. we will get back to you as
				soon as we can!
			</h3>

			<div class="block_content_contacts">
				<div class="block_content_contacts_l">
					<input type="text" placeholder="Name" class="mb4" v-model="$v.name.$model"
						:state="$v.name.$dirty ? !$v.name.$error : null" />
					<div v-if="!$v.name.required">Name required</div>
					<input type="text" placeholder="E-mail" class="mb4" v-model="$v.email.$model"
						:state="$v.email.$dirty ? !$v.email.$error : null" />
					<div v-if="!$v.email.required">Email required</div>
					<div v-if="!$v.email.email">Invalid email</div>
					<input type="text" placeholder="Message" class="mb4" v-model="$v.message.$model"
						:state="$v.message.$dirty ? !$v.message.$error : null" />
					<div v-if="!$v.message.required">Message required</div>
					<div v-if="!$v.message.minLength">Message length must be at least 20 characters</div>
					<button @click="sendingMessage">SEND</button>
				</div>
				<div class="block_content_contacts_r">
					<a href="#email" class="mb4"><i class="fas fa-envelope"></i>
						<span>exmoney@gmail.com</span></a>
					<a href="#fb" class="mb4"><i class="fab fa-facebook-f"></i><span>Facebook</span></a>
					<a href="#tg" class="mb4"><i class="fab fa-telegram-plane"></i>
						<span>Telegram</span></a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { validationMixin } from 'vuelidate';
import { required, email, minLength } from 'vuelidate/lib/validators';
import axios from '../axios';


export default {
	name: "Home",
	components: {},
	data() {
		return {
			name: "",
			email: "",
			message: "",
		};
	},
	validations: {
		name: { required, minLength: minLength(3) },
		email: { required, email },
		message: {
			required,
			minLength: minLength(20)
		},
	},
	mixins: [validationMixin,],
	computed: {},

	methods: {
		sendingMessage() {
			this.$v.$touch();
			if (this.$v.$anyError) {
				console.log("We have error");
				return
			}
			console.log(`star req`);
			try {
				axios.post('api/v1//create_comments/', {
					headers: {
						'Content-Type': 'application/json'
					},
					data: {
						email: this.email,
						name: this.name,
						message: this.message,
					}
				})
					.catch(function (error) {
						console.log(error);
					});
				this.email = '',
					this.name = '',
					this.message = ''

			} catch (e) {
				alert('Error')
			}
		}
	},
};
</script>
<style scoped>
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

@media (min-width: 1200px) and (max-width: 1440px) {
	.content_contacts h1 {
		font-size: 60px;
		line-height: 60px;
	}

	.content_contacts {
		width: 80%;
	}

	.content_contacts h3 {
		font-style: normal;
		font-weight: 600;
		font-size: 22px;
		line-height: 24px;
		width: 80%;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.content_contacts h1 {
		font-size: 48px;
		line-height: 48px;
	}

	.content_contacts {
		width: 80%;
	}

	.content_contacts h3 {
		font-style: normal;
		font-weight: 600;
		font-size: 20px;
		line-height: 22px;
		width: 80%;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.main_contacts {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		background-image: none;
		background-repeat: no-repeat;
		background-position: unset;
		background-size: 0;
		padding: 0 2%;
	}

	.content_contacts {
		width: 100%;
		margin-bottom: 100px;
	}

	.content_contacts h1 {
		font-size: 42px;
		line-height: 42px;
	}

	.content_contacts h3 {
		font-size: 18px;
		line-height: 20px;
		width: 70%;
	}

	.block_content_contacts_l,
	.block_content_contacts_r {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		width: 40%;
		padding: 4%;
	}

	.block_content_contacts_l input {
		font-size: 18px;
		line-height: 24px;
	}

	.block_content_contacts_l input::placeholder {
		font-size: 18px;
		line-height: 24px;
		/* identical to box height */

		color: #cccccc;
	}

	.block_content_contacts_r a {
		font-size: 20px;
		line-height: 20px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.main_contacts {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		background-image: none;
		background-repeat: no-repeat;
		background-position: unset;
		background-size: 0;
		padding: 0 5%;
	}

	.content_contacts {
		width: 100%;
		margin-bottom: 100px;
	}

	.content_contacts h1 {
		font-size: 36px;
		line-height: 36px;
	}

	.content_contacts h3 {
		font-size: 16px;
		line-height: 18px;
		width: 80%;
	}

	.block_content_contacts {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
	}

	.block_content_contacts_l,
	.block_content_contacts_r {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		width: 80%;
		padding: 10% 0%;
	}

	.block_content_contacts_l input {
		font-size: 18px;
		line-height: 24px;
	}

	.block_content_contacts_l input::placeholder {
		font-size: 18px;
		line-height: 24px;
		/* identical to box height */

		color: #cccccc;
	}

	.block_content_contacts_r a {
		font-size: 20px;
		line-height: 20px;
	}

	.block_content_contacts_l button {
		font-size: 18px;
		color: #2a3587;
		padding: 0 20px;
		height: 40px;
		width: 50%;
		margin: 0 auto;
	}
}

@media (max-width: 479px) {
	.main_contacts {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		background-image: none;
		background-repeat: no-repeat;
		background-position: unset;
		background-size: 0;
		padding: 0 5%;
	}

	.content_contacts {
		width: 100%;
		margin-bottom: 100px;
	}

	.content_contacts h1 {
		font-size: 28px;
		line-height: 28px;
	}

	.content_contacts h3 {
		font-size: 14px;
		line-height: 16px;
		width: 80%;
	}

	.block_content_contacts {
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 100%;
	}

	.block_content_contacts_l,
	.block_content_contacts_r {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		width: 100%;
		padding: 10% 0%;
	}

	.block_content_contacts_l input {
		font-size: 14px;
		line-height: 24px;
	}

	.block_content_contacts_l input::placeholder {
		font-size: 14px;
		line-height: 24px;
		/* identical to box height */

		color: #cccccc;
	}

	.block_content_contacts_r a {
		font-size: 18px;
		line-height: 18px;
	}

	.block_content_contacts_l button {
		font-size: 16px;
		color: #2a3587;
		padding: 0 10px;
		height: 34px;
		width: 40%;
		margin: 0 auto;
	}
}
</style>
