from pyexpat import model
import re
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from .models import ExmoneyUser, PaymentMethod, UsersLogins
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExmoneyUser
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'phone')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = str(tokens)
        access = str(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        user = ExmoneyUser.objects.create_user(validated_data['username'], password=validated_data['password'], first_name=validated_data['first_name'], 
                                                last_name=validated_data['last_name'],  email=validated_data['email'],  phone=validated_data['phone'])
        return user
# User serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExmoneyUser
        fields = '__all__'


class PaymentMethodSavingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('card_number', 'wallet')


class PaymentMethodGettingWalSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('wallet',)


class PaymentMethodGettingCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('card_number',)


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExmoneyUser
        fields = ('promocode',)


class LoginHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersLogins
        fields = '__all__'
