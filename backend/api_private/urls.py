from django.urls import path
from . import views


urlpatterns = [
    path("statistic/", views.Test3Commas.as_view()),
    path("plan-investment/", views.PlanInvestmentAPI.as_view()),
]
