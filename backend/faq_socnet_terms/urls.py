from django.urls import path
from faq_socnet_terms import views


urlpatterns = [
    path("faq/", views.FAQListAPIView.as_view()),
    path("social_network/", views.SocialNetworksListAPIView.as_view()),
    path("terms/", views.TermsListAPIView.as_view()),
]