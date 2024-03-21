<template>
    <div>
        <div class="  p_imp1">
            <div class="payment_menu">
                <button class="btn_standart_small" @click="menu_payment=1" :class="{ btn_standart_small_active: menu_payment == 1 }">Deposite</button>
                <button class="btn_standart_small" @click="menu_payment=2" :class="{ btn_standart_small_active: menu_payment == 2 }">Withdraw</button>
                <button class="btn_standart_small" @click="menu_payment=3" :class="{ btn_standart_small_active: menu_payment == 3 }">Manual</button>
            </div>
        </div>
        <div class="Payment">
            <div class="payment_form">
                <div class="deposite" v-if="menu_payment == 1">
                    <h4 class="name_form mb4">Deposite form</h4>
                    <div class="payment_form_selected mb2">

                        <v-select class="style-chooser" placeholder="Choose Crypto Ethereum" v-model="deposit_selected"
                            :reduce="(option) => option.name" :options="getList_cryoto_payment" label="name" name="id"
                            key="id" :clearable="false" :closeOnSelect="true" />
                    </div>
                    <div class="payment_form_input mb2">
                        <input type="text" class="input_pink" placeholder="Amount: 0.5ETH">
                        <h6>Вводить сумму относительно выбраной валюты!</h6>
                    </div>
                    <button class="btn-fill mb2">Pay</button>
                </div>
                <div class="withdraw" v-if="menu_payment == 2">
                    <h4 class="name_form mb4">Withdraw form</h4>
                    <div class="payment_form_selected mb2">

                        <v-select class="style-chooser" placeholder="Choose Crypto Ethereum" v-model="deposit_selected"
                            :reduce="(option) => option.name" :options="getList_cryoto_payment" label="name" name="id"
                            key="id" :clearable="false" :closeOnSelect="true" />
                    </div>
                    <div class="payment_form_input mb2">
                        <input type="text" class="input_pink" placeholder="Crypto Address">
                        <h6>Внимательно указывайте свой кошелёк <br> относительно выбраной валюты!</h6>
                    </div>
                    <div class="payment_form_input mb2">
                        <input type="text" class="input_pink" placeholder="Amount: 0.5ETH">
                        <h6>Вводить сумму относительно выбраной валюты!</h6>
                    </div>
                    <button class="btn-fill mb2">Send request</button>
                </div>
                <div class="manual" v-if="menu_payment == 3">
                    <h4 class="name_form mb4">Instruction</h4>
                    
                    <div class="manual_info">
                        <h3>About Deposite</h3>
                        <ul>
                            <li>Для начала выберете валюту из списка</li>
                            <li>Введити вручную сумму, которую хотите инвестировать</li>
                            <li>Для Вас будет сгенерирована платежка, через популярную платёжную систему CoinBase</li>
                            <li>Совершите переход по ссылки для вноса депозита</li>
                            <li>После оплаты, ваши деньги будут зачислены на Ваш баланс</li>
                            <li>CoinBase снимает коммисию 1%</li>
                            <li>Мы предоставляем ещё один способ, без коммисии, оплатить на прямую. Для этого нужно написать нашему администратору. Указав свой ЮЗЕРНЕЙМ, далее он вам поможет. Коммисия только в сети!</li>
                        </ul>
                    </div>
                    <hr class="hr_manual">
                    <div class="manual_info">
                        <h3>About Withdraw</h3>
                        <ul>
                            <li>Для начала выберете валюту из списка</li>
                            <li>Введити вручную сумму, которую хотите инвестировать</li>
                            <li>Для Вас будет сгенерирована платежка, через популярную платёжную систему CoinBase</li>
                            <li>Совершите переход по ссылки для вноса депозита</li>
                            <li>После оплаты, ваши деньги будут зачислены на Ваш баланс</li>
                            <li>CoinBase снимает коммисию 1%</li>
                            <li>Мы предоставляем ещё один способ, без коммисии, оплатить на прямую. Для этого нужно написать нашему администратору. Указав свой ЮЗЕРНЕЙМ, далее он вам поможет. Коммисия только в сети!</li>
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
// import axios from '../axios';
// import { validationMixin } from 'vuelidate';
// import { email, required, numeric, alpha } from '@vuelidate/validators';
// import { required, alpha, numeric, email, sameAs, minLength } from 'vuelidate/lib/validators'


export default {
    components: { 'v-select': vSelect, },
    data() {
        return {
            menu_payment:1,
            deposit_selected: ""
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

    },
    methods: {

    },
};
</script>

<style>
.Payment{
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
.name_form{
    text-align: center;
    color: white;
    font-size: 24px;
    line-height: 36px;
    border-bottom: solid 2px #fe1ae7;
    text-transform: uppercase;
    font-weight: 700;
    padding-bottom: 10px;
}
.payment_form_input{
    display: flex;
    flex-direction: column;
}
.payment_form_input h6{
    color: white;
    margin-top: 20px;
    font-style: italic;
    text-decoration: underline;
    font-weight: 800;
    font-size: 16px;
    text-align: center;
}
.deposite button{
    width: 35%;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-weight: 800;
}
.withdraw button{
    width: fit-content;
    margin: 0 auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    font-weight: 800;

}
.manual{
    color: #fff;
    display: flex;
    flex-direction: column;
    width: 80%;
}
.manual h3{
    font-size: 18px;
    line-height: 28px;
    font-weight: 600;
    margin-bottom: 20px;
}
.manual ul{
    list-style: decimal-leading-zero;
}
.manual ul li{
    font-size: 16px;
    line-height: 20px;
    margin-bottom: 10px;
}
.hr_manual{
    width: 100%;
    height: 2px;
    background: #fff;
    margin: 25px 0px;
}
</style>
