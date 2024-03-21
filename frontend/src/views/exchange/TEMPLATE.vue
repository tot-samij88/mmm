<template>
    <div class="main_page">
        <div class="central">
            <div class="StartExchange">
                <div class="blockExchange">
                    <div class="header_Exchange">
                        <button style="cursor: pointer">
                            &#215;
                        </button>

                        <h3 class="mb2">Exchange {{ full_pair.from_pair }} to {{ full_pair.to_pair }}</h3>
                        <p></p>
                        <ul>
                            <li :class="{ activeLi: stepExchange === 1 }">
                                <i class="fas fa-pencil-alt"></i>
                                <h5>Data input</h5>
                            </li>

                            <li :class="{ activeLi: stepExchange === 2 }">
                                <i class="fas fa-credit-card"></i>
                                Payment
                            </li>

                            <li :class="{ activeLi: stepExchange === 3 }">
                                <i class="fas fa-check"></i>
                                Status
                            </li>

                            <li :class="{ activeLi: stepExchange === 4 }">
                                <i class="fas fa-check-double"></i>
                                Completion
                            </li>
                        </ul>
                    </div>
                    <div class="enteringValues mh300 pay_time">
                        <h3 class="weight900 mt3 mb1">Attention!</h3>
                        <!-- ВСе текста должны генерироваться на беке -->
                        <p class="mb1">
                            This address only accepts Ethereum ETH. Please do not send any other
                            currency to this address. They will not be credited.
                        </p>
                        <p class="mb1">
                            Transfer the exact amount of 1 ETH to the specified address in one
                            transaction.
                        </p>
                        <p class="mb1">
                            Please transfer exactly the amount shown, otherwise you may
                            experience refunds and processing problems. The amount must be
                            transferred in one transaction, payment in multiple transactions is
                            not supported.
                        </p>
                        <p class="mb3">
                            The address given to you by the system for this deposit can only be
                            used once. Each new replenishment must be initiated anew.
                        </p>
                        <hr class="lineW mb3" />
                        <div class="id_date_main" v-if="error_getAddress === false">
                            <div class="id_date">
                                <h4>ID: {{ idRequest }}</h4>
                                <h4>Date: {{ dateCreate | moment }}</h4>
                            </div>
                        </div>
                        <div class="address mb4" v-if="error_getAddress === false">
                            <h5 class="address_link">{{ value }}</h5>
                            <button>Copy</button>
                        </div>
                        <div class="qr_code_pay_addres mb3" v-if="error_getAddress === false">
                            <!-- <img src="@/assets/qr_test.png" alt="qr-code address"> -->
                            <qrcode-vue :value="value" :size="size" level="H" />
                        </div>
                        <div class="error_getAddress" v-if="error_getAddress === true">
                            <p class="mt3 mb3">
                                {{ error_getAddress_message }}
                            </p>
                        </div>
                        <hr class="lineW mb3" />
                        <div class="btn_step2 mb5">
                            <button @click="cancel">Cancel</button>
                            <button @click="nextPaid">Yes, I paid</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
