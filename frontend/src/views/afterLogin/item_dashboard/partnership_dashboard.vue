<template>
	<div class="partnership bgcbdr">
		<h3 class="mb3">Partnership program</h3>
		<div class="partnership_one mb5">
			<div class="partnership_one__l">
				<img src="@/assets/Handshake.png" alt="" />
			</div>
			<div class="partnership_one__r">
				<h4 class="mb1">
					Exmoney invites owners and administrators of web-sites to
					join our partnership program. You will need to:
				</h4>
				<ul>
					<li>Register as a user on the web-site</li>
					<li>
						Invite your friends to follow personal partnership link
						available in client’s backoffice.
					</li>
					<li>
						After sharing a partnership link with your friend, each
						client taken to the web-site flashobmen.com by clicking
						the banner and performing transactions through our
						service is considered to be a client invited by you as a
						partner of the service. A partner receives profit in
						percentage from the amount of the profit of the service
						from each transaction performed by attracted client on
						web-site flashobmen.com. The interest amount which a
						partner receives depends on the partner’s level. The
						higher the level is the bigger share a partner receives.
						The amount of discount for personal exchanges is also
						calculated depending on the level of a partner.
						Partner’s level is defined by total amount of
						transactions (performed personally or by invited
						clients).
					</li>
					<li>
						The formula is the following: Total amount=Personal
						amount+(client’s amount) / 3
					</li>
				</ul>
			</div>
		</div>
		<div>
			<h3>Level</h3>
			<div class="level">
				<ul class="date">
					<li class="level_name_col">Partner’s level</li>
					<li>1</li>
					<li>2</li>
					<li>3</li>
					<li>4</li>
					<li>5</li>
				</ul>
				<ul class="ex_from">
					<li class="level_name_col">
						Total volume of transactions USD
					</li>
					<li>10</li>
					<li>100</li>
					<li>1000</li>
					<li>10000</li>
					<li>100000</li>
				</ul>
				<ul class="ex_to">
					<li class="level_name_col">
						Personal discount (in % from Service’s profit)
					</li>
					<li>5</li>
					<li>10</li>
					<li>15</li>
					<li>20</li>
					<li>25</li>
				</ul>
				<ul class="ex_to">
					<li class="level_name_col">
						Profit from customers’ exchange (in % from Service
						profit)
					</li>
					<li>5</li>
					<li>10</li>
					<li>15</li>
					<li>20</li>
					<li>25</li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "partnership-dashboard",
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
