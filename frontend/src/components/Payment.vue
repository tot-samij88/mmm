<template>
    <div class="main_payment">
        
        <div class="payment">
            <h1>Предложить КоинБейс или лично без коммисии</h1>
            <p>Для коинбейс надо : юзернейм, опис, монета и сума. Це все для створення платіжки, щоб виглядала солідно</p>
            <p>Для прямої передачі, використати інструкцію + лінк на почту/телеграм</p>
            <h3>Форма оплаты</h3>
            <!-- <img src="@/assets/crypto_i/eth.png" alt=""> -->
            <select v-model="choice_crypto">
                <option v-for="(item, index) in getList_cryoto_payment" :key="index">
                    <img :src="require(`@/assets/crypto_i/${item.shortName}.png`)" alt="" />
                    {{item.name}}
                </option>
            </select>
            <div class="item_payment">
                <label for="z1">z1</label>
                <input type="text" name="z1" id="">
            </div>
            <div class="item_payment">
                <label for="z2">z2</label>
                <input type="text" name="z2" id="">
            </div>
            <div class="item_payment">
                <label for="z3">z3</label>
                <input type="text" name="z3" id="">
            </div>
            <button class="btn-fill">Отправить</button>
        </div>
    </div>
</template>

<script>
import store from "@/store";
// import Vue from "vue";
// import axios from '../axios';
// import { validationMixin } from 'vuelidate';
// import { email, required, numeric, alpha } from '@vuelidate/validators';
// import { required, alpha, numeric, email, sameAs, minLength } from 'vuelidate/lib/validators'


export default {
    data() {
        return {

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
.main_payment {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.payment {
    width: 40%;
    color: #fff;
    background: rgba(255, 255, 255, 0.1);
    border: solid 3px rgba(249, 27, 231, 1);
    border-radius: 15px;
    padding: 5% 2%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.payment h3{
    font-size: 24px;
    line-height: 28px;
    font-weight: 700;
    border-bottom: solid 2px rgba(249, 27, 231, 1);
    padding-bottom: 10px;
    margin-bottom: 25px;
    width: 100%;
    text-align: center;
}
.item_payment{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 70px;
}
.main_payment label{
    font-size: 24px;
    line-height: 28px;
}
.main_payment input {
	height: 40px;
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
	color: #fff !important;
	border: none;
	background-color: rgba(249, 27, 231, 0.1);
	border-radius: 0.990366px;
	border: solid 2px rgba(249, 27, 231, 1);
}

.main_payment input::placeholder {
	color: rgb(145, 145, 145);
	font-style: normal;
	font-weight: 600;
	font-size: 24px;
}

.main_payment input:focus {
	outline: none;
}
</style>
