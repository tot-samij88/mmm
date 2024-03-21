from django.shortcuts import render
from rest_framework import generics
from .serializers import FAQSerializer, SocialNetworksSerializer, TermsSerializer
from .models import FAQ, SocialNetworks, Terms


class FAQListAPIView(generics.ListAPIView):
    """Вивод списка поширених питаннь"""
    serializer_class = FAQSerializer
    
    def get_queryset(self):
        return FAQ.objects.filter(is_published = True)


class SocialNetworksListAPIView(generics.ListAPIView):
    """Вивод списка соціальни мереж"""
    serializer_class = SocialNetworksSerializer
    
    def get_queryset(self):
        return SocialNetworks.objects.filter(is_published = True)


class TermsListAPIView(generics.ListAPIView):
    """Вивод списка умов користування"""
    serializer_class = TermsSerializer
    
    def get_queryset(self):
        return Terms.objects.filter(is_published = True)