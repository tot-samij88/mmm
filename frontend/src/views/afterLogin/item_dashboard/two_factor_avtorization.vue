<template>
    <div class="referals bgcbdr">
        <h3 class="mb2">2FA Authenticate </h3>
        <div class="set_2fa">
            <div class="child" v-if="is2fa">
                <h4>Уже подключено 2FA <br>Для сброса напишите администратору @ Email @</h4>
            </div>
            <div class="child" v-else>
                <h4>Instructions!</h4>
                <ul class="instruc">
                    <li>Download <a
                            href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en&gl=US"
                            target="_blank">Google Authenticator</a> on your mobile.</li>
                    <li>Scan the QR-code or enter secret-key in the form.</li>
                    <li>Save the secret key to restore access to two-factor authentication.</li>
                    <li>Сonfirm the addition of two-factor authentication by entering a one-time password.</li>
                </ul>
            </div>
            <hr v-if="!is2fa">
            <button v-if="!is2fa" type="button" @click="get_secret" class="btn-fill">Add</button>
            <div class="created_2fa" v-if="add_2fa">
                <div class="left_block">
                    <div class="content_left_block">
                        <input type="text" name="" id="" placeholder="000 000" v-model="otp">
                        <button type="button" @click="check_OTP" class="btn_standart">Approve</button>
                        <h1 v-show="invalid_otp" style="color:red;">invalid OTP</h1>
                    </div>
                </div>

                <div class="right_block" v-show="add_2fa">
                    <div class="right_block_left">
                        <qrcode-vue :value="this.qr_secret_token" :size="150" level="H" />
                    </div>
                    <div class="right_block_right">
                        <textarea type="text" id="secret" :value="this.secret_token"></textarea>
                        <button type="button" @click="copySecret" class="btn_standart">Copy</button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import axios from '../../../axios';
import QrcodeVue from 'qrcode.vue'


export default {
    name: "twofactor-dashboard",
    data() {
        return {
            add_2fa: false,
            is2fa: false,
            invalid_otp: false,
            secret_token: '',
            qr_secret_token: '',
            otp: '',
            show_2fa:false
        }
    },
    components: {
        QrcodeVue,
    },
    methods: {
        check_secret_available() {
            var self = this
            try {
                axios.post('/auth/token_check_available/', {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: {
                        username: localStorage.getItem('username')
                    }
                })
                    .then(function (response) {
                        var ans = JSON.parse(JSON.stringify(response.data));
                        self.is2fa = ans['is_tfa']
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            } catch (e) {
                alert('Error')
            }
        },
        check_OTP() {
            var self = this
            try {
                axios.post('/auth/token_check/', {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: {
                        username: localStorage.getItem('username'),
                        otp: this.otp
                    }
                })
                    .then(function (response) {
                        var ans = JSON.parse(JSON.stringify(response.data));
                        self.is2fa = ans['result']
                        self.add_2fa = !ans['result']
                        self.invalid_otp = !ans['result']
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            } catch (e) {
                alert('Error')
            }
        },
        get_secret() {
            var self = this
            if (!this.add_2fa) {
                try {
                    axios.post('/auth/token_create/', {
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        data: {
                            username: localStorage.getItem('username')
                        }
                    })
                        .then(function (response) {
                            var ans = JSON.parse(JSON.stringify(response.data));
                            self.secret_token = ans['users_token'];
                            self.qr_secret_token = ans['url'];
                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                } catch (e) {
                    alert('Error')
                }
            }
            this.add_2fa = !this.add_2fa
        },
        copySecret() {
            /* Get the text field */
            var copyText = document.getElementById("secret");

            /* Select the text field */
            copyText.select();
            copyText.setSelectionRange(0, 99999); /*For mobile devices*/

            /* Copy the text inside the text field */
            document.execCommand("copy");

            alert("Successfully copied TOTP secret token!");
        },
    },
    mounted() {
        this.check_secret_available();
    },
};

</script>

<style>
.referals{
    color: #fff;
}
.created_2fa {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 150px;
    padding: 30px 0px 10px 0px;
}

.left_block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 40%;
    height: 100%;
}

.content_left_block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    height: 100%;
}

.content_left_block input {
    background-size: 30px;
    width: 150px;
    text-align: center;
    height: 40px;
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
    line-height: 23px;
    padding: 10px;
    color: #fff !important;
    border: none;
    background-color: rgba(127, 179, 238, 0.5);
    box-shadow: inset -1.98073px -1.98073px 1.98073px rgb(255 255 255 / 50%), inset 1.98073px 1.98073px 1.98073px rgb(52 65 166 / 50%);
    border-radius: 0.990366px;
}

.right_block {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 60%;
    height: 100%;
}

.right_block_left {
    width: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.right_block_right {
    width: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    ;
    height: 100%;
}

.right_block textarea {
    background-size: 30px;
    width: 150px;
    height: 40px;
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 20px;
    text-align: center;
    padding: 10px;
    color: #fff !important;
    border: none;
    background-color: rgba(127, 179, 238, 0.5);
    box-shadow: inset -1.98073px -1.98073px 1.98073px rgb(255 255 255 / 50%), inset 1.98073px 1.98073px 1.98073px rgb(52 65 166 / 50%);
    border-radius: 0.990366px;
    resize: none;
}

.right_block textarea:focus {
    outline: none;
}

.set_2fa button {
    min-width: 170px;
}



.instruc {
    display: flex;
    flex-direction: column;
    list-style-type: disc;
    margin: 10px 0;
}

.instruc li {
    font-size: 16px;
    line-height: 28px;
}

.instruc li a {
    color: rgba(249, 27, 231, 1);;
    cursor: pointer;
    text-decoration: none;
}

.child {
    margin: 0 10px;
}

.righted {
    order: 999;
    margin-left: auto;
}

@media (min-width: 1200px) and (max-width: 1440px) {}

@media (min-width: 992px) and (max-width: 1199px) {
    .created_2fa {
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        height: auto;
        padding: 30px 0px 10px 0px;
    }

    .right_block {
        width: 100%;
        margin-bottom: 30px;
    }
}

@media (min-width: 768px) and (max-width: 991px) {
    .created_2fa {
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        height: auto;
        padding: 30px 0px 10px 0px;
    }

    .right_block {
        width: 100%;
        margin-bottom: 30px;
    }
}

@media (min-width: 480px) and (max-width: 767px) {
    .created_2fa {
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        height: auto;
        padding: 30px 0px 10px 0px;
    }

    .right_block {
        width: 100%;
        margin-bottom: 30px;
    }
}

@media (max-width: 479px) {
    .created_2fa {
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        height: auto;
        padding: 30px 0px 10px 0px;
    }

    .right_block {
        width: 100%;
        margin-bottom: 30px;
    }

    .instruc li {
        font-size: 14px;
        line-height: 18px;
    }

    .set_2fa button {
        font-size: 16px;
        min-width: 120px;
    }


    .right_block textarea {
        width: 100px;
        height: 60px;
        font-size: 14px;
        line-height: 20px;
        padding: 10px;
    }

    .right_block canvas {
        width: 120px !important;
        height: 120px !important;
    }

    .content_left_block input {
        width: 100px;
        height: 30px;
        font-size: 16px;
        line-height: 20px;
    }
}
</style>
