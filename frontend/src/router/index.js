import Vue from "vue";
import VueRouter from "vue-router";
import Main from "../views/Main.vue";
import Home from "../views/Home.vue";
import Terms from "../views/Terms.vue";
import News from "../views/News.vue";
import Reviews from "../views/Reviews.vue";
import Contacts from "../views/Contacts.vue";
import WebSocket from "../views/WebSocket.vue";
import TestFirst from "../views/TEST_first.vue";
import TestSecond from "../views/TEST_second.vue";
// FORMS
import stepOne from "../views/exchange/stepOne.vue";
import stepTwo from "../views/exchange/stepTwo.vue";
// import stepThree from "../views/exchange/stepThree.vue";
import stepFour from "../views/exchange/stepFour.vue";
// import store from "@/store" TestSecond

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: Home,
	},
	{
		path: "/main",
		name: "main",
		component: Main,
	},
	// ###### EXCHANGE #######
	// ФОРМА
	{
		path: "/exchange/:pair?",
		name: "step-1",
		component: stepOne,
	},
	// ПОЛУЧЕНИЕ ИД_РИКВЕСТ | ВЫСТАВЛЕНИЕ СЧЕТА | СТАТУС ВЫПОЛНЕНИЯ
	{
		path: "/order/:id_request?",
		name: "step-2",
		component: stepTwo,
	},
	// {
	// 	path: "/exchange/:pair?/:id_request?",
	// 	name: "step-3",
	// 	component: stepThree,
	// },
	// ФИНАЛЬНАЯ СТРАНИЦА completed
	{
		path: "/completed/:id_request?",
		name: "step-4",
		component: stepFour,
	},
	{
		path: "/terms",
		name: "Terms",
		component: Terms,
	},
	{
		path: "/news",
		name: "News",
		component: News,
	},
	{
		path: "/reviews",
		name: "Reviews",
		component: Reviews,
	},
	{
		path: "/contacts",
		name: "Contacts",
		component: Contacts,
	},

	{
		path: "/test-exchange",
		name: "test_first",
		component: TestFirst,
	},
	{
		path: "/test-exchange/:pair?",
		name: "test_second",
		props: true,
		component: TestSecond,
	},
	{
		// after open here
		path: "/test-exchange/:pair?/:id_request?",
		name: "test_third",
		props: true,
		component: WebSocket,
	},
	{
		path: "/auth",
		name: "auth",
		component: () =>
			import(/* webpackChunkName: "about" */ "../components/Auth.vue"),
	},
	{
		path: "/payment",
		name: "payment",
		component: () =>
			import(/* webpackChunkName: "about" */ "../components/Payment.vue"),
	},
	{
		path: "/dashboard",
		name: "dashboard",
		component: () => import("../views/afterLogin/Dashboard.vue"),
		meta: {
			requiresAuth: true,
		},
	},
	// {
	// 	path: "/about",
	// 	name: "About",
	// 	component: () =>
	// 		import(/* webpackChunkName: "about" */ "../views/Terms.vue"),
	// },
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});
router.beforeEach((to, from, next) => {
	if (to.matched.some((record) => record.meta.requiresAuth)) {
		// this route requires auth, check if logged in
		// if not, redirect to login page.

		const token = localStorage.getItem("accessToken");
		if (!token) {
			next({ name: "Auth" });
		} else {
			next(); // go to wherever I'm going
		}
	} else {
		next(); // does not require auth, make sure to always call next()!
	}
});
export default router;
