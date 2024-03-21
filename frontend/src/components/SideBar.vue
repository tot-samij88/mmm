<template>
	<div class="sideBar">
		<ul class="sideBar_item">
			<!-- main -->
			<li><router-link :to="{ name: 'main' }">01 {{ $t("Main") }}</router-link></li>
			<li><router-link :to="{ name: 'Terms' }">02 {{ $t("Terms") }}</router-link></li>
			<li><router-link :to="{ name: 'News' }">03 {{ $t("News") }}</router-link></li>
			<li><router-link :to="{ name: 'Reviews' }">04 {{ $t("Reviews") }}</router-link></li>
			<li><router-link :to="{ name: 'Contacts' }">05 {{ $t("Contacts") }}</router-link></li>
			<!-- <li><router-link to="/test-exchange">06 StartTest</router-link></li> -->
		</ul>

	</div>
</template>

<script>
export default {};
</script>

<style scoped>
.sideBar {
	width: 15%;
	padding-left: 5%;
}

.sideBar_item {
	list-style-type: none;
	padding: 0;
}

.sideBar_item li {
	padding: 14px 0px 5px 0px;
}

.sideBar_item li a {
	color: white;
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	line-height: 32px;
	text-transform: uppercase;
	text-decoration: none;

}

.sideBar_item li a:hover {
	color: rgba(249, 27, 231, 1);;
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.sideBar_item li a {
		font-size: 22px;
		line-height: 28px;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.sideBar {
		width: 15%;
		padding-left: 2%;
	}

	.sideBar_item li a {
		font-size: 18px;
		line-height: 24px;
	}
}

@media (min-width: 992px) {
	.sideBar {
		display: block;
	}
}

@media (max-width: 991px) {
	.sideBar {
		display: none;
	}
}

@media (min-width: 768px) and (max-width: 991px) {}

@media (min-width: 480px) and (max-width: 767px) {}

@media (max-width: 479px) {}
</style>
