<template>
	<div class="terms">
		<div class="terms__l">
			<h1 class="mb2">Terms</h1>
			<div class="terms__l__one">
				<h2>What are the terms and conditions?</h2>
				<p>
					These rules are considered to be subject to the conditions
					of the public offer, which enters into force at the time of
					submission of an application by the Customer and is one of
					the main components of this agreement. The information about
					the conditions of application submission specified by the
					Contractor, is a Public offer. The main part of a public
					offer are actions made in the completion of the application
					submission by the Customer showing his exact intentions to
					make a transaction on the terms proposed by the Contractor
					before the end of this application.
					<strong style="font-weight: 900">Read more</strong>
				</p>
			</div>
			<div class="terms__l__two mb5">
				<div class="terms__r" id="mobile_h2">
					<h2>
						What are <br />
						the main rules?
					</h2>
				</div>
				<div class="terms__l__two__block">
					<h3 class="mb1">
						Your reliable assistant requires the following:
					</h3>
					<p>
						All exchange operations are made only on our website:
						You make the request via special form, then our support
						consider it and write (on the website) the requisites
						for making payment or request any additional
						information. One exchange - one request. If someone,
						from our name, offer you the private exchange via
						telegram, skype, viber, whatsup etc., be assured - it is
						a scammer, you just lose your money (we know some such
						unfortunate incidents).
						<strong style="font-weight: 900">Read more</strong>
					</p>
				</div>
				<div class="terms__l__two__block">
					<h3 class="mb1">In an exchange to PayPal</h3>
					<p>
						According to paypal rules payments can not be sent to
						the address of the citizens of Russia, Belarus and some
						other countries. Check your acountry on URL:
						<a href="https://www.paypal.com/webapps/mpp/country-worldwide">paypal</a>.
						"PayPal is for everyone who pays or gets paid" (for
						example, Croatia) when viewing data on the country, it
						indicates the possibility of accepting payments, and
						"PayPal is for everyone who pays online" (for example,
						Belarus) means the impossibility of receiving payments.
						<strong style="font-weight: 900">Read more</strong>
					</p>
				</div>
				<div class="terms__l__two__block">
					<h3 class="mb1">In the exchange to cryptocurrencies</h3>
					<p>
						The preliminary rate is updated automatically when the
						client views the request, and then it is fixed if the
						payment is received or the exchange request is changed
						(a favorable rate for us is chosen, so do not delay the
						notification of the payment made).
					</p>
				</div>
			</div>
		</div>
		<div class="terms__r" id="desctop_h2">
			<h2>
				What are <br />
				the main rules?
			</h2>
		</div>
	</div>
</template>

<script>
export default {};
</script>

<style>
.terms {
	width: 85%;
	height: 100%;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	color: #fff;
}

.terms__l {
	width: 65%;
}

.terms__l h1 {
	font-style: normal;
	font-weight: 900;
	font-size: 72px;
	line-height: 83px;
}

.terms__r {
	width: 30%;
	display: flex;
	flex-direction: row;
	justify-content: flex-end;
	align-items: center;
	background-image: url("../assets/bgLogoTerms.png");
	background-repeat: repeat-x;
	background-position: bottom;
	background-size: 100%;
}

.terms__r h2 {
	font-style: normal;
	font-weight: 600;
	font-size: 44px;
	line-height: 64px;

	text-align: right;
}

.terms__l__one {
	display: flex;
	flex-direction: row;
	padding-bottom: 25px;
	width: 100%;
	border-bottom: 2px solid #fff;
}

.terms__l__one h2 {
	font-style: normal;
	font-weight: 600;
	font-size: 36px;
	line-height: 135%;
	width: 35%;
}

.terms__l__one p {
	font-style: normal;
	font-weight: 500;
	font-size: 20px;
	line-height: 135%;
	width: 50%;
}

.terms__l__two {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	margin-top: 25px;
}

.terms__l__two__block {
	width: 30%;
}

.terms__l__two__block h3 {
	font-style: normal;
	font-weight: 600;
	font-size: 20px;
	line-height: 135%;
}

.terms__l__two__block p {
	font-style: normal;
	font-weight: 300;
	font-size: 14px;
	line-height: 110%;
	text-align: justify;
}

@media (min-width: 1200px) and (max-width: 1440px) {
	.terms__r {
		width: 35%;
		justify-content: center;
	}

	.terms__l {
		width: 60%;
	}

	.terms__l h1 {
		font-size: 60px;
		line-height: 60px;
	}

	.terms__l__one h2 {
		font-size: 30px;
		line-height: 130%;
		width: 40%;
	}

	.terms__l__one p {
		font-size: 18px;
		line-height: 140%;
		width: 60%;
	}

	.terms__r h2 {
		font-size: 36px;
		line-height: 48px;
		text-align: right;
	}

	.terms__l__two__block h3 {
		font-size: 18px;
		line-height: 130%;
		height: 70px;
	}
}

@media (min-width: 992px) and (max-width: 1199px) {
	.terms__r {
		width: 35%;
		justify-content: center;
	}

	.terms__l {
		width: 60%;
	}

	.terms__l__one {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.terms__l h1 {
		font-size: 48px;
		line-height: 48px;
	}

	.terms__l__one h2 {
		font-size: 28px;
		line-height: 130%;
		width: 100%;
	}

	.terms__l__one p {
		font-size: 16px;
		line-height: 140%;
		width: 90%;
		padding-top: 15px;
	}

	.terms__l__two {
		display: flex;
		flex-direction: column;
		margin-top: 25px;
		align-items: center;
	}

	.terms__l__two__block {
		width: 90%;
	}

	.terms__r h2 {
		font-size: 28px;
		line-height: 36px;
		text-align: right;
	}

	.terms__l__two__block h3 {
		font-size: 18px;
		line-height: 130%;
		height: auto;
		margin-top: 30px;
	}
}

@media (min-width: 768px) and (max-width: 991px) {
	.terms {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		color: #fff;
	}

	.terms__l {
		width: 90%;
	}

	.terms__r {
		background-image: none;
	}

	.terms__l__one {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.terms__l h1 {
		font-size: 42px;
		line-height: 42px;
	}

	.terms__l__one h2 {
		font-size: 24px;
		line-height: 125%;
		width: 100%;
	}

	.terms__l__one p {
		font-size: 16px;
		line-height: 140%;
		width: 90%;
		padding-top: 15px;
	}

	.terms__l__two {
		display: flex;
		flex-direction: column;
		margin-top: 25px;
		align-items: center;
	}

	.terms__l__two__block {
		width: 90%;
	}

	.terms__r h2 {
		font-size: 24px;
		line-height: 32px;
		text-align: left;
	}

	.terms__l__two__block h3 {
		font-size: 18px;
		line-height: 130%;
		height: auto;
		margin-top: 20px;
	}
}

@media (min-width: 480px) and (max-width: 767px) {
	.terms {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		color: #fff;
	}

	.terms__l {
		width: 90%;
	}

	.terms__r {
		background-image: none;
	}

	.terms__l__one {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.terms__l h1 {
		font-size: 36px;
		line-height: 36px;
	}

	.terms__l__one h2 {
		font-size: 18px;
		line-height: 120%;
		width: 100%;
	}

	.terms__l__one p {
		font-size: 14px;
		line-height: 140%;
		width: 95%;
		padding-top: 10px;
	}

	.terms__l__two {
		display: flex;
		flex-direction: column;
		margin-top: 25px;
		align-items: center;
	}

	.terms__l__two__block {
		width: 90%;
	}

	.terms__r h2 {
		font-size: 18px;
		line-height: 24px;
		text-align: left;
	}

	.terms__l__two__block h3 {
		font-size: 16px;
		line-height: 120%;
		height: auto;
		margin-top: 20px;
	}
}

@media (max-width: 479px) {
	.terms {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: row;
		justify-content: center;
		color: #fff;
	}

	.terms__l {
		width: 90%;
	}

	.terms__r {
		background-image: none;
	}

	.terms__l__one {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.terms__l h1 {
		font-size: 28px;
		line-height: 28px;
	}

	.terms__l__one h2 {
		font-size: 16px;
		line-height: 125%;
		width: 100%;
	}

	.terms__l__one p {
		font-size: 13px;
		line-height: 135%;
		width: 100%;
		padding-top: 10px;
	}

	.terms__l__two {
		display: flex;
		flex-direction: column;
		margin-top: 25px;
		align-items: center;
	}

	.terms__l__two__block {
		width: 90%;
	}

	.terms__r h2 {
		font-size: 16px;
		line-height: 22px;
		text-align: left;
	}

	.terms__l__two__block h3 {
		font-size: 14px;
		line-height: 120%;
		height: auto;
		margin-top: 20px;
	}

	.terms__l__two__block p {
		font-size: 13px;
		line-height: 115%;
		text-align: justify;
	}
}

/* mobile_h2 desctop_h2 */
@media (min-width: 991px) {
	#mobile_h2 {
		display: none;
	}
}

@media (max-width: 991px) {
	#mobile_h2 {
		display: flex;
		flex-direction: row;
		justify-content: center;
		width: 100%;
	}

	#desctop_h2 {
		display: none;
	}
}
</style>
