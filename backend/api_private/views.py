import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import PlanInvestmentSerializer
from .models import PlanInvestment
import json
from rest_framework import status
# ____________
from datetime import datetime
# 
from py3cw.request import Py3CW
import http.client


class PlanInvestmentAPI(generics.ListAPIView):
    """Вивод списка умов користування"""
    serializer_class = PlanInvestmentSerializer
    
    def get_queryset(self):
        return PlanInvestment.objects.all()

p3cw = Py3CW(
    key='68bc8888852f4a7a984db30bc0b7fffd00726a68dd054780b1ae63b0cb487e88', 
    secret='bbe07091271407e0df7a2f484271875bd82d393926154e12e8aa85874f13b56417e1400bda4e3c51e0753d46c3179e0630e85a89e05d7590759f611d93cc26c45e8bd6d699df24ce4a07125454734863281a3675c327aacedc5f32f413a2628eefe78640',
    request_options={
        'request_timeout': 10,
        'nr_of_retries': 1,
        'retry_status_codes': [502],
        'retry_backoff_factor': 0.1
    }
)


class Test3Commas(APIView):
    #  http://127.0.0.1:8000/api/v1/private/statistic/
    # POST
    """
        {
            "current_stage":"4",
            "id_request":"uuid in str"
        }
    """
    def post(self, request):
        try:
            data = json.loads(request.body)
            print("DATA", data)
            # username == naming of bot, for easy cheking
            filter_by_name = data.get('username')
            filter_by_name = "DYDX/BUSD"
            error_grid_bots, data_grid_bots = p3cw.request(
                entity='grid_bots',
                action=''
            )
            if error_grid_bots:
                payload = {
                    "error":error_grid_bots,
                    "info":"Please, wait 1 minutes and try again"
                }
                Response(payload, status=status.HTTP_200_OK)
            else:
                # This is generator for serching bot == username, becode endpoint return ALL
                # Отримую словник {} 
                get_by_name_bot = next((item for item in data_grid_bots if item['name'] == str(filter_by_name)), None)
                id_bots_by_name = get_by_name_bot['id']
                # Отримаю список словників [{}]
                error_profits, data_profits = p3cw.request(
                    entity='grid_bots',
                    action='profits',
                    action_id=str(id_bots_by_name)
                )
                # На базе data_profits
                # Реализовать профит в день, там можно отправлять ФРОМ и ТУ
                # После чего сумировать доход и отправлять одним полем 
                # Брать дей_тудей 19.03.2023 и подставлять 00:00 и 23:59
                if error_profits:
                    payload = {
                        "error":error_grid_bots,
                        "info":"Please, wait 1 minutes and try again"
                    }
                    Response(payload, status=status.HTTP_200_OK)
                else:
                    payload = {
                        "id": get_by_name_bot["id"],
                        "is_enabled": get_by_name_bot["is_enabled"],
                        "created_at": get_by_name_bot["created_at"],
                        "lower_price": get_by_name_bot["lower_price"],
                        "upper_price": get_by_name_bot["upper_price"],
                        "name": get_by_name_bot["name"],
                        "pair": get_by_name_bot["pair"],
                        # "start_price": get_by_name_bot["start_price"],
                        "current_profit": get_by_name_bot["current_profit"],
                        "current_profit_usd": get_by_name_bot["current_profit_usd"],
                        "total_profits_count": get_by_name_bot["total_profits_count"],
                        "profit_percentage": get_by_name_bot["profit_percentage"],
                        # "current_price": get_by_name_bot["current_price"],
                        # это DyDx
                        'investment_base_currency': get_by_name_bot["investment_base_currency"],
                        # это BUSD
                        'investment_quote_currency': get_by_name_bot["investment_quote_currency"],
                        "profit":data_profits
                    }
                    return Response(payload, status=status.HTTP_200_OK)
        except Exception as ex:
            payload = {
                "error":ex,
                "info":"Please, wait 1 minutes and try again"
            }
            return Response(payload, status=status.HTTP_200_OK)
        

class PaymentCreate(APIView):
    def post(self,request):
        

        conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
        payload = {
            'name':'test_name',
            'description':'test_description',
            'pricing_type':'fixed_price',
            'local_price': {
                'amount':1,
                'currency':'ETH'
            },
            'metadata': {
                'customer_id':'1488-1312',
                'customer_name':'customer_name_ETH'
            },
            'metadata':'test_name',
            'name':'test_name',
            'name':'test_name',
        }
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-CC-Api-Key': '813feb08-12ef-4176-b210-8c64ffac1c47',
        'X-CC-Version':'2018-03-22'
        }
        conn.request("POST", "/charges", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

        """ Вот так я создаю адрес платежки, с фиксированой суммой, которую укажет клиент и к чему эта сумма == """
        # Ответ формы оплаты
        result = {
            "data": {
                "addresses": {
                    "polygon": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "pusdc": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "pweth": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "ethereum": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "usdc": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "dai": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "apecoin": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "shibainu": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "tether": "0x3179de1c4a4d33948107a7595f4928f0975b73d5",
                    "bitcoincash": "qrwg8ytpjakv636347hghs6367rcsgnr7uu4mm7f4f",
                    "dogecoin": "D6sgP4BqzsaTWwJgy8wF3HYUvbUcWYkmE6",
                    "litecoin": "MWBuKRJCt8GB5JhLPTTbVR5jFHLEGkiEbb",
                    "bitcoin": "3AbSLWkWQpB1KN3zfWKMWyGsWbdEYt5RWx"
                },
                "brand_color": "#122332",
                "brand_logo_url": "",
                "code": "28BTLBB4",
                "coinbase_managed_merchant": False,
                "created_at": "2023-03-19T22:00:54Z",
                "description": "test_description",
                "exchange_rates": {
                    "ETH-USD": "1796.44",
                    "BTC-USD": "28059.07",
                    "LTC-USD": "84.615",
                    "DOGE-USD": "0.0751",
                    "BCH-USD": "134.495",
                    "USDC-USD": "1.0",
                    "DAI-USD": "0.99995",
                    "APE-USD": "4.3115",
                    "SHIB-USD": "0.00001097",
                    "USDT-USD": "1.003075",
                    "PMATIC-USD": "1.17965",
                    "PUSDC-USD": "1.0",
                    "PWETH-USD": "1798.585"
                },
                "expires_at": "2023-03-19T23:00:54Z",
                "fee_rate": 0.01,
                "fees_settled": True,
                "hosted_url": "https://commerce.coinbase.com/charges/28BTLBB4", # Просто отдать пользователю линку!
                "id": "ed8fd631-2336-454c-8d02-254483856bab", # Отследить и все добавить в БД к конекретному пользователю
                "local_exchange_rates": {
                    "ETH-ETH": "1.000000000",
                    "BTC-ETH": "15.619263655",
                    "LTC-ETH": "0.047101490",
                    "DOGE-ETH": "0.000041805",
                    "BCH-ETH": "0.074867516",
                    "USDC-ETH": "0.000556656",
                    "DAI-ETH": "0.000556629",
                    "APE-ETH": "0.002400024",
                    "SHIB-ETH": "0.000000006",
                    "USDT-ETH": "0.000558368",
                    "PMATIC-ETH": "0.000656660",
                    "PUSDC-ETH": "0.000556656",
                    "PWETH-ETH": "1.001194028"
                },
                "logo_url": "",
                "metadata": {},
                "name": "test_name",
                "offchain_eligible": False,
                "organization_name": "",
                "payment_threshold": {
                    "overpayment_absolute_threshold": {
                        "amount": "5.00",
                        "currency": "USD"
                    },
                    "overpayment_relative_threshold": "0.005",
                    "underpayment_absolute_threshold": {
                        "amount": "5.00",
                        "currency": "USD"
                    },
                    "underpayment_relative_threshold": "0.005"
                },
                "payments": [],
                "pricing": {
                    "local": {
                        "amount": "1.000000000",
                        "currency": "ETH"
                    },
                    "polygon": {
                        "amount": "1522.858475000",
                        "currency": "PMATIC"
                    },
                    "pusdc": {
                        "amount": "1796.440000",
                        "currency": "PUSDC"
                    },
                    "pweth": {
                        "amount": "0.998807395813931507",
                        "currency": "PWETH"
                    },
                    "ethereum": {
                        "amount": "1.000000000",
                        "currency": "ETH"
                    },
                    "usdc": {
                        "amount": "1796.440000",
                        "currency": "USDC"
                    },
                    "dai": {
                        "amount": "1796.529826491324566228",
                        "currency": "DAI"
                    },
                    "apecoin": {
                        "amount": "416.662414472921257103",
                        "currency": "APE"
                    },
                    "shibainu": {
                        "amount": "163759343.664539653600729262",
                        "currency": "SHIB"
                    },
                    "tether": {
                        "amount": "1790.932881",
                        "currency": "USDT"
                    },
                    "bitcoincash": {
                        "amount": "13.35692777",
                        "currency": "BCH"
                    },
                    "dogecoin": {
                        "amount": "23920.63914780",
                        "currency": "DOGE"
                    },
                    "litecoin": {
                        "amount": "21.23075105",
                        "currency": "LTC"
                    },
                    "bitcoin": {
                        "amount": "0.06402350",
                        "currency": "BTC"
                    }
                },
                "pricing_type": "fixed_price",
                "pwcb_only": False,
                "resource": "charge",
                "support_email": "mizeravladik@gmail.com",
                "timeline": [
                    {
                        "status": "NEW",
                        "time": "2023-03-19T22:00:54Z"
                    }
                ],
                "utxo": False
            }
        }
