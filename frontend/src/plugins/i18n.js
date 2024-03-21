import Vue from "vue";
import VueI18n from "vue-i18n";

Vue.use(VueI18n);
// синтаксис в компоненте - {{ $t("logIn") }}
const messages = {
	en: {
		// Header
		logIn: "Log in",
		logOut: "Log out",
		Profile: "Profile",
		Close: "Close",
		Menu: "Menu",
		Main: "Main",
		Terms: "Terms",
		News: "News",
		Reviews: "Reviews",
		Contacts: "Contacts",
		// Portfolio

		// Services

		// About studio

		// Contacts

		// Footer
	},
	ua: {
		// Header
		logIn: "Вхід",
		logOut: "Вихід",
		Profile: "Профіль",
		Close: "Закрити",
		Menu: "Меню",
		Main: "Головна",
		Terms: "Умови",
		News: "Новини",
		Reviews: "Відгуки",
		Contacts: "Контакти",
		// Portfolio

		// Services

		// About studio

		// Contacts

		// Footer
	},
};

const i18n = new VueI18n({
	locale: "en", // set locale
	fallbackLocale: "en", // set fallback locale
	messages, // set locale messages
});

export default i18n;
