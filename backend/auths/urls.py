from django.urls import path
from .api import RegisterApi
from . import views

urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('set_pay_meth/', views.PaymentMethodSetAPIView.as_view()),
    path('get_pay_meth/', views.PaymentMethodGetAPIView.as_view()),
    path("token_create/", views.TwoFA_keysAPIView.as_view()),
    path("token_check_available/", views.TwoFA_keysAvailableAPIView.as_view()),
    path("token_check/", views.TwoFA_keysCheckAPIView.as_view()),
    path("promocode/", views.PromoCodeGetAPIView.as_view()),
    path("user-info/", views.UserInfo.as_view()),
    path("set_logging_history/", views.SetLoggingHistoryAPIView.as_view()),
    path("get_logging_history/", views.GetLoggingHistoryAPIView.as_view()),
    path("ref_test/", views.ReferalTestAPIView.as_view()),
    # UserInfo

]
