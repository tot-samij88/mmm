<template>
	<div class="main_reviews">
		<h1 class="mb2">Reviews</h1>
		<h4 class="mb5">
			The cryptocurrency market, like the weather, is always
			unpredictable. Keep your hand on your pulse.
		</h4>
		<div class="reviews">
			<div class="arrow" @click.prevent="slidePrev">
				<i class="fas fa-chevron-left"></i>
			</div>
			<div class="slider">
				<hooper ref="carousel" @slide="updateCarousel" :settings="hooperSettings" :wheelControl="true"
					v-if="reviews_data.length > 0">
					<slide v-for="(item, index) in reviews_data" :key="index">
						<div class="box_item">
							<div class="blured">
								<h3 class="mb1">{{ item.name }}</h3>
								<h5 class="mb2">{{ item.email }}</h5>
								<p>{{ item.message }}</p>
							</div>
						</div>
					</slide>
				</hooper>
			</div>
			<div class="arrow" @click.prevent="slideNext">
				<i class="fas fa-chevron-right"></i>
			</div>
		</div>
	</div>
</template>

<script>
import { Hooper, Slide } from "hooper";
import "hooper/dist/hooper.css";
import axios from '../axios'
export default {
	components: { Hooper, Slide },
	data() {
		return {
			carouselData: 0,
			hooperSettings: {
				itemsToShow: 3,
				centerMode: false,
				breakpoints: {

					992: {
						itemsToShow: 3,
					},
					768: {
						centerMode: false,
						itemsToShow: 2
					},
					0: {
						centerMode: false,
						itemsToShow: 1
					},
				}
			},
			tst_reviews_data: [
				{
					user: "James, 32",
					txt: "I am very pleased with the Exmoney service. Very comfortable. Quick registration and also very quickly got an answer to a question that interested me.",
				},
				{
					user: "David, 43",
					txt: "Your service was recommended to me by an acquaintance of mine. I tried and really did not regret it. Fast exchange.",
				},
				{
					user: "James, 32",
					txt: "I want to leave a positive review of Exmoney. I have extensive experience with cryptocurrency.I really have something to compare with.",
				},
			],
			reviews_data: []
		};
	},
	watch: {
		carouselData() {
			this.$refs.carousel.slideTo(this.carouselData);
		},
	},
	mounted() {
		this.get_reviews()
	},
	methods: {
		slidePrev() {
			this.$refs.carousel.slidePrev();
		},
		slideNext() {
			this.$refs.carousel.slideNext();
		},
		updateCarousel(payload) {
			this.myCarouselData = payload.currentSlide;
		},
		get_reviews() {
			// console.log("full_pair", full_pair);
			let self = this;
			axios.get("/api/v1/get-comments/")
				.then(function (resp) {
					console.log(resp.data);
					self.reviews_data = resp.data;
				})
		}
		// moment: function () {
		// 	return moment();
		// },
		// to_single_post(slug) {
		// 	// Щоб достукатись до конкретного Слогана, потрібно через клік передавати його.А не через this.item.slug
		// 	this.$router.push({ name: "post", query: { post: slug } });
		// },
	},
};
</script>

<style scoped>
.main_reviews {
	width: 85%;
	/* height: 100%; */
	color: #fff;
	background-image: url("../assets/bgLogoTerms.png");
	background-repeat: repeat-x;
	background-position: bottom;
	background-size: 30%;
}

.main_reviews h1 {
	font-style: normal;
	font-weight: 900;
	font-size: 72px;
	line-height: 83px;
}

.main_reviews h4 {
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	line-height: 28px;
}

.reviews {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 200px;
}

.hooper {
	height: auto;
}

.hooper-slide {
	flex-shrink: 0;
	height: 100%;
	margin: 0;
	padding: 0 10px;
	list-style: none;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: flex-start;
}

.hooper-track {
	display: flex;
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	padding: 0;
	flex-direction: row;
	justify-content: center;
}

.slider {
	width: 90%;
	display: flex;
	flex-direction: row;
	justify-content: center;
}

.arrow i {
	font-size: 60px;
	color: #fff;
	cursor: pointer;
}

.arrow i:hover {
	color: rgba(249, 27, 231, 1);;
}

.slider p {
	font-style: normal;
	font-weight: 400;
	font-size: 24px;
	line-height: 28px;
}

.slider h3 {
	font-style: normal;
	font-weight: 600;
	font-size: 32px;
	line-height: 37px;
}

.box_item {
	background-image: url("../assets/bg_pair.png");
	background-repeat: repeat-y;
	background-position: center center;
	background-size: 100%;
}

.blured {
	height: 360px;
	padding: 30px;
	display: flex;
	flex-direction: column;
	backdrop-filter: blur(50px);
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.main_reviews {
		width: 80%;
	}

	.main_reviews h1 {
		font-size: 60px;
		line-height: 60px;
	}

	.main_reviews h4[data-v-1aa8c6e6] {
		font-size: 22px;
		line-height: 24px;
		width: 80%;
	}

	.reviews {
		width: 96%;
	}

	.blured {
		height: 320px;
		padding: 20px;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.main_reviews {
		width: 80%;
	}

	.main_reviews h1 {
		font-size: 48px;
		line-height: 48px;
	}

	.main_reviews h4 {
		font-size: 18px;
		line-height: 22px;
		width: 80%;
	}

	.reviews {
		width: 96%;
	}

	.blured {
		height: 320px;
		padding: 20px;
	}

	.slider h3 {
		font-size: 24px;
		line-height: 28px;
	}

	.slider p {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.main_reviews {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.main_reviews h1 {
		width: 80%;
		font-size: 42px;
		line-height: 42px;
	}

	.main_reviews h4 {
		font-size: 18px;
		line-height: 22px;
		width: 80%;
	}

	.reviews {
		width: 86%;
	}

	.blured {
		height: 320px;
		padding: 20px;
	}

	.slider h3 {
		font-size: 24px;
		line-height: 28px;
	}

	.slider p {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.main_reviews {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.main_reviews h1 {
		width: 90%;
		font-size: 36px;
		line-height: 36px;
	}

	.main_reviews h4 {
		font-size: 16px;
		line-height: 20px;
		width: 90%;
	}

	.reviews {
		width: 90%;
	}

	.slider {
		width: 70%;
	}

	.slider img {
		width: 90%;
		height: 90%;
	}

	.blured {
		height: 320px;
		padding: 20px;
	}

	.slider h3 {
		font-size: 20px;
		line-height: 24px;
	}

	.slider p {
		font-size: 16px;
		line-height: 20px;
	}

	.arrow i {
		font-size: 45px;
	}
}

@media (max-width: 479px) {
	.main_reviews {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		background-image: none;
		background-size: 0%;
		background-repeat: no-repeat;
		background-position: unset;
	}

	.main_reviews h1 {
		width: 90%;
		font-size: 28px;
		line-height: 28px;
	}

	.main_reviews h4 {
		font-size: 14px;
		line-height: 18px;
		width: 90%;
	}

	.reviews {
		width: 90%;
		margin-bottom: 0;
	}

	.slider {
		width: 80%;
	}

	.slider img {
		width: 95%;
		height: 95%;
	}

	.slider p {
		font-size: 16px;
		line-height: 20px;
	}

	.arrow i {
		font-size: 30px;
	}

	.blured {
		height: 280px;
		padding: 20px;
	}

	.slider h3 {
		font-size: 16px;
		line-height: 20px;
	}

	.slider p {
		font-size: 14px;
		line-height: 18px;
	}
}
</style>
