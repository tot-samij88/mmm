from datetime import datetime
from django.db import models
import uuid
# Create your models here.

# TYPE_FROM = (
#     (0, 'Не обрано',),
#     (1, 'Крипто'),
#     (2, 'Фіат')
# )

# class CreateExchange(models.Model):
#     id_request = models.UUIDField(
#         verbose_name="UUID Request", unique=True, default=uuid.uuid4)
#     client = models.CharField(max_length=255,verbose_name="Client", default="Anonim")
#     status_exchange = models.IntegerField(
#         choices=STATUS_EXCHANGE, verbose_name='Status Exchange', default=0)
#     pair_full = models.CharField(max_length=100, verbose_name="Coin FULL")
#     pair_from = models.CharField(max_length=100, verbose_name="Coin FROM")
#     pair_to = models.CharField(max_length=100, verbose_name="Coin TO")
#     provider_from = models.CharField(max_length=100, verbose_name="Provider FROM",null=True)
#     provider_to = models.CharField(max_length=100, verbose_name="Provider TO",null=True)
    
#     amount_from = models.CharField(max_length=100, verbose_name="Amount FROM")
#     amount_to = models.CharField(max_length=100, verbose_name="Amount TO")
#     address = models.CharField(max_length=100, verbose_name="Address to send")
#     email = models.CharField(max_length=100, verbose_name="Email user")
#     date_create = models.DateTimeField(
#         default=datetime.now, verbose_name='Date create', null=True)
#     type_from_is = models.IntegerField(
#         choices=TYPE_FROM, verbose_name='TYPE FROM_', default=0)
#     type_to_is = models.IntegerField(
#         choices=TYPE_TO, verbose_name='TYPE _TO', default=0)
#     own_address_crypto = models.CharField(
#         max_length=255, verbose_name="Own crypto address", default="-")
#     own_address_fiat = models.CharField(
#         max_length=255, verbose_name="Own fiat address", default="-")
#     # Поля для идентификации пользователя
#     # id_user = models.ForeignKey()
#     isAuthWebsite = models.BooleanField(
#         default=False, verbose_name="Он зареган?")
#     ip = models.CharField(
#         max_length=255, verbose_name="IP", blank=True, null=True)
#     phone = models.CharField(
#         max_length=255, verbose_name="Phone", blank=True, null=True)
#     fingerprint = models.TextField(
#         verbose_name="Fingerprint", blank=True, null=True)
#     # Deposit and Withdraw - TRUE
#     do_deposite = models.BooleanField(
#         default=False, verbose_name="ПОЛУЧИЛИ ОПЛАТУ")
#     do_withdraw = models.BooleanField(
#         default=False, verbose_name="ВЫПЛАТИЛИ")

#     class Meta:
#         verbose_name = 'CreateExchange'
#         verbose_name_plural = 'CreateExchanges'

class PlanInvestment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название Тарифа")
    pair = models.CharField(max_length=255, verbose_name="ПАРА", null=True)
    profit = models.FloatField(verbose_name="Процент заработка в день")
    min_deposite = models.IntegerField(verbose_name="Минимальный депозит")
    max_deposite = models.IntegerField(verbose_name="Максимальный депозит")
    period_min = models.IntegerField(verbose_name="Минимум дней")
    period_medium = models.IntegerField(verbose_name="Средина дней")
    period_max = models.IntegerField(verbose_name="Максимум дней")