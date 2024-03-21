<template>
	<div class="partnership bgcbdr">
		<h3 class="mb3">Settings</h3>
		<h2>Реализовать смену:</h2>
		<h3>ПАРОЛЯ!</h3>
		<h3>ЕМЕЙЛА</h3>
		<h3>ИМЕНИ ПОЛЬЗОВАТЕЛЯ</h3>
		<h3>ИНСТРУКЦИЮ О ТОМ, ЧТО ДЕЛАТЬ КОГДА ПРОЕБАЛ 2FA</h3>
	</div>
</template>

<script>
export default {
	name: "settings-dashboard",
};
</script>

<style>
.partnership {
	color: #fff;
}

.partnership h3 {
	font-style: normal;
	font-weight: 500;
	font-size: 24px;
	line-height: 28px;
}

.partnership_one {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	width: 100%;
	align-items: center;
}

.partnership_one__l {
	width: 15%;
}

.partnership_one__r {
	width: 85%;
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 24px;
}

.partnership_one__r ul {
	list-style-type: disc;
}

.partnership_one__r ul li {
	margin-bottom: 10px;
}

.level {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

.level ul {
	width: 24%;
	list-style-type: none;
	text-align: center;
	padding: 0;
}

.level ul li {
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 32px;
}

.level_name_col {
	font-style: normal;
	font-weight: 400;
	font-size: 15px !important;
	line-height: 24px !important;
	color: #fff;
	border-bottom: 1px solid #fff;
	padding-bottom: 5px;
	margin-bottom: 10px;
	text-align: center;
	height: 60px;
	display: flex;
	flex-direction: row;
	align-items: flex-end;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {}

@media (min-width: 768px) and (max-width: 991px) {}

@media (min-width: 480px) and (max-width: 767px) {}

@media (max-width: 479px) {}
</style>
