<template>
	<div class="main_news">
		<h1 class="mb2">News</h1>
		<h4 class="mb5">
			The cryptocurrency market, like the weather, is always
			unpredictable. Keep your hand on your pulse.
		</h4>
		<div class="news">
			<div class="arrow" @click.prevent="slidePrev">
				<i class="fas fa-chevron-left"></i>
			</div>
			<div class="slider">
				<hooper ref="carousel" @slide="updateCarousel" :settings="hooperSettings" :wheelControl="true"
					v-if="news_data.length > 0">
					<slide v-for="(item, index) in news_data" :key="index">
						<img :src="'data:image;base64,' + item.photo" alt="" />
						<p class="mt2">{{ item.title }}</p>
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
			tst_news_data: [
				{
					img: "@/assets/n1.png",
					txt: "Bitcoin price to drop to $29000, losing 70 per cent of its value, expert warns",
				},
				{
					img: "@/assets/n2.png",
					txt: "Cryptocrash: ‘I was arrested         for knocking on Luna boss's door'",
				},
				{
					img: "@/assets/n3.png",
					txt: "Crypto Crash Update 5/25: Top cryptocurrencies fall again; Bitcoin, Ethereum, Solana, Cardano             in the RED",
				},
			],
			news_data: []
		};
	},
	watch: {
		carouselData() {
			this.$refs.carousel.slideTo(this.carouselData);
		},
	},
	mounted() {
		this.get_news()
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
		get_news() {
			// console.log("full_pair", full_pair);
			let self = this;
			axios.get("/api/v1/news/")
				.then(function (resp) {
					console.log(resp.data);
					self.news_data = resp.data;
				})
		},
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
.main_news {
	width: 85%;
	/* height: 100%; */
	color: #fff;
	background-image: url("../assets/bgLogoTerms.png");
	background-repeat: repeat-x;
	background-position: bottom;
	background-size: 30%;
}

.main_news h1 {
	font-style: normal;
	font-weight: 900;
	font-size: 72px;
	line-height: 83px;
}

.main_news h4 {
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	line-height: 28px;
}

.news {
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

.slider img {
	width: 100%;
	height: 100%;
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
	font-weight: 700;
	font-size: 20px;
	line-height: 23px;
	padding: 0 20px;
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.main_news {
		width: 80%;
	}

	.main_news h1 {
		font-size: 60px;
		line-height: 60px;
	}

	.main_news h4[data-v-1aa8c6e6] {
		font-size: 22px;
		line-height: 24px;
		width: 80%;
	}

	.news {
		width: 96%;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.main_news {
		width: 80%;
	}

	.main_news h1 {
		font-size: 48px;
		line-height: 48px;
	}

	.main_news h4 {
		font-size: 18px;
		line-height: 22px;
		width: 80%;
	}

	.news {
		width: 96%;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.main_news {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.main_news h1 {
		width: 80%;
		font-size: 42px;
		line-height: 42px;
	}

	.main_news h4 {
		font-size: 18px;
		line-height: 22px;
		width: 80%;
	}

	.news {
		width: 96%;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.main_news {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.main_news h1 {
		width: 90%;
		font-size: 36px;
		line-height: 36px;
	}

	.main_news h4 {
		font-size: 16px;
		line-height: 20px;
		width: 90%;
	}

	.news {
		width: 90%;
	}

	.slider {
		width: 70%;
	}

	.slider img {
		width: 90%;
		height: 90%;
	}
}

@media (max-width: 479px) {
	.main_news {
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		background-image:none;
		background-size: 0%;
		background-repeat: no-repeat;
		background-position: unset;
	}

	.main_news h1 {
		width: 90%;
		font-size: 28px;
		line-height: 28px;
	}

	.main_news h4 {
		font-size: 14px;
		line-height: 18px;
		width: 90%;
	}

	.news {
		width: 90%;
		margin-bottom: 0;
	}

	.slider {
		width: 70%;
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
}
</style>
