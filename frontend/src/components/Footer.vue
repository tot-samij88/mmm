<template>
	<div class="footer">
		<p>(c) 2023</p>
		<!-- <ul class="footerBar">
			<li><router-link to="/">Main</router-link></li>
			<li><router-link to="/terms">Terms</router-link></li>
			<li><router-link to="/news">News</router-link></li>
			<li><router-link to="/reviews">Reviews</router-link></li>
			<li><router-link to="/contacts">Contacts</router-link></li>
		</ul> -->
	</div>
</template>

<script>
export default {};
</script>

<style>
.footer {
	background-color: #290044!important;
	min-height:100px;
	display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-end;
}
.footer p{
	font-size: 18px;
	line-height: 24px;
	color: #fff;
	text-align: center;
}
.footerBar {
	width: 50%;
	margin: 0 auto;
	display: flex;
	flex-direction: row;
	justify-content: space-around;
	align-items: center;
	height: 100%;
	list-style-type: none;
}

.footerBar li a {
	color: #fff;
	font-style: normal;
	font-weight: 600;
	font-size: 18px;
	line-height: 135%;
	text-decoration: none;
	text-transform: uppercase;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {
	.footerBar {
		width: 70%;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.footerBar {
		width: 80%;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.footerBar {
		width: 80%;
	}

	.footerBar li a {
		font-size: 14px;
		line-height: 135%;
	}
}

@media (max-width: 479px) {
	.footerBar {
		width: 80%;
		flex-direction: column;
	}

	.footerBar li a {
		font-size: 14px;
		line-height: 135%;
	}

	.footer {
		padding: 25px 0;
	}
}
</style>
