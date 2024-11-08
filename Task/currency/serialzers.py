from rest_framework import serializers
from .models import Currency, ExchangeRate

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code']

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'