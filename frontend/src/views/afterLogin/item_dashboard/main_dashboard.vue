<template>
    <div>
        <div class="  p_imp1">
            <div class="payment_menu">
                <button class="btn_standart_small" @click="menu_main = 1"
                    :class="{ btn_standart_small_active: menu_main == 1 }">Make Bot</button>
                <button class="btn_standart_small" @click="menu_main = 3"
                    :class="{ btn_standart_small_active: menu_main == 3 }">Manual</button>
            </div>
        </div>
        <div class="Payment">
            <div class="payment_form">
                <div class="deposite" v-if="menu_main == 1">
                    <h4 class="name_form mb4">Sequoia Bot</h4>
                    <div class="payment_form_selected mb2" v-if="all_plan_info">
                        <div class="deposite_item">
                            <h5>Choose Plan</h5>
                            <v-select class="style-chooser" placeholder="Choose Plan" v-model="tarif_selected"
                                :reduce="(option) => option.name" :options="all_plan_info" label="name" name="id" key="id"
                                :clearable="false" :closeOnSelect="true" />
                        </div>
                        <div class="deposite_item">
                            <h5>Username</h5>
                            <input type="text" class="input_pink" placeholder="Username will be DISABLED">
                        </div>
                        <div class="deposite_item">
                            <h5>Pair</h5>
                            <input type="text" class="input_pink" placeholder="Pair will be DISABLED">
                        </div>
                        <div class="give_days">
                            
                            <button class="btn_standart_small" :class="{ btn_standart_small_active: plan_3_choice_days_active == 1 }"
                                @click="plan_3_period = plan_3_daysMin; plan_3_choice_days_active = 1">{{ plan_3_daysMin }}
                                дня</button>

                            <button class="btn_standart_small" :class="{ btn_standart_small_active: plan_3_choice_days_active == 2 }"
                                @click="plan_3_period = plan_3_daysMedium; plan_3_choice_days_active = 2">{{
                                    plan_3_daysMedium
                                }}
                                дней</button>

                            <button class="btn_standart_small" :class="{ btn_standart_small_active: plan_3_choice_days_active == 3 }"
                                @click="plan_3_period = plan_3_daysMax; plan_3_choice_days_active = 3">{{ plan_3_daysMax }}
                                дней</button>
                        </div>
                        <h3 class="amount_range">{{ amount }}$</h3>
                        <input type="range" v-model="amount" min=3 max=180>
                    </div>
                    <button class="btn-fill mb2 mt5">Create</button>
                </div>

                <div class="manual" v-if="menu_main == 3">
                    <h4 class="name_form mb4">Instruction</h4>

                    <div class="manual_info">
                        <h3>How to create Bot?</h3>
                        <ul>
                            <li>Для начала выберете валюту из списка</li>
                            <li>Введити вручную сумму, которую хотите инвестировать</li>
                            <li>Для Вас будет сгенерирована платежка, через популярную платёжную систему CoinBase</li>
                            <li>Совершите переход по ссылки для вноса депозита</li>
                            <li>После оплаты, ваши деньги будут зачислены на Ваш баланс</li>
                            <li>CoinBase снимает коммисию 1%</li>
                            <li>Мы предоставляем ещё один способ, без коммисии, оплатить на прямую. Для этого нужно написать
                                нашему администратору. Указав свой ЮЗЕРНЕЙМ, далее он вам поможет. Коммисия только в сети!
                            </li>
                        </ul>
                    </div>

                </div>


            </div>
        </div>
    </div>
</template>

<script>
import store from "@/store";
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
// import Vue from "vue";
import axios from '../../../axios.js';
// import { validationMixin } from 'vuelidate';
// import { email, required, numeric, alpha } from '@vuelidate/validators';
// import { required, alpha, numeric, email, sameAs, minLength } from 'vuelidate/lib/validators'


export default {
    components: { 'v-select': vSelect, },
    data() {
        return {
            all_plan_info: [],
            menu_main: 1,
            amount: 99,
            tarif_selected: "",
            deposit_selected: "",
        };
    },
    // validations: {
    //     registerData: {
    //         first_name: { required, alpha },
    //         last_name: { required, alpha },
    //         phone: { required, numeric },
    //         email: { required, email },
    //         password: {
    //             required,
    //             minLength: minLength(8)
    //         },
    //         conf_password: {
    //             required,
    //             sameAs: sameAs('password')
    //         },
    //     },
    // },
    // mixins: [validationMixin,], 
    computed: {
        getList_cryoto_payment: {
            get: () => store.getters.getList_cryoto_payment,
        },
        // list_tarif: {
        //     get: () => store.getters.getList_tarif,
        //     set: (payload) => store.commit("setList_tarif", payload),
        // },

    },
    methods: {
        get_plan_info() {
            // this.isListToLoading = true
            // console.log("from_pair", from_pair);
            let self = this;
            axios.get("/api/v1/private/plan-investment/", {
                headers: {
                    'Content-Type': 'application/json'
                },
                data: {
                    "username": localStorage.getItem('username')
                }
            })
                .then(function (resp) {
                    console.log(resp.data);
                    self.all_plan_info = resp.data
                    // self.isListToLoading = false
                })
        },
    },
    mounted() {
        this.get_plan_info()
    }
};
</script>

<style>
.Payment {
    margin-bottom: 50px;
}

.payment_menu {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 50%;
    margin: 0 auto;
}

.payment_form {
    display: flex;
    flex-direction: row;
    justify-content: center;
    background: rgba(255, 255, 255, 0.1);
    width: 50%;
    padding: 5% 0;
    margin: 0 auto;
    border-radius: 15px;
}

.name_form {
    text-align: center;
    color: white;
    font-size: 24px;
    line-height: 36px;
    border-bottom: solid 2px #fe1ae7;
    text-transform: uppercase;
    font-weight: 700;
    padding-bottom: 10px;
}

.payment_form_selected input {
    width: 100%;
}

.payment_form_input {
    display: flex;
    flex-direction: column;
}

.payment_form_input h6 {
    color: white;
    margin-top: 20px;
    font-style: italic;
    text-decoration: underline;
    font-weight: 800;
    font-size: 16px;
    text-align: center;
}
.deposite{
    width: 70%;
}
.deposite_item{
    margin: 20px 0px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}
.deposite_item .v-select, .deposite_item input{
    width: 60%;
}
.deposite_item h5{
    color: #fff;
    font-size: 20px;
    line-height: 28px;
    font-weight: 600;
    width: 40%;
}
.deposite button {
    width: 35%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-weight: 800;
}

.withdraw button {
    width: fit-content;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-weight: 800;

}

.give_days {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 40px 0px;
}
.give_days button{
    width: 28%;
}
.amount_range{
    color: #fff;
    text-align: center;
    font-size: 22px;
    line-height: 36px;
    font-weight: 600;
}
.manual {
    color: #fff;
    display: flex;
    flex-direction: column;
    width: 80%;
}

.manual h3 {
    font-size: 18px;
    line-height: 28px;
    font-weight: 600;
    margin-bottom: 20px;
}

.manual ul {
    list-style: decimal-leading-zero;
}

.manual ul li {
    font-size: 16px;
    line-height: 20px;
    margin-bottom: 10px;
}

.hr_manual {
    width: 100%;
    height: 2px;
    background: #fff;
    margin: 25px 0px;
}
</style>
