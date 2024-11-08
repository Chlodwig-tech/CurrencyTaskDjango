from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

from .models import Currency, ExchangeRate
from .serialzers import CurrencySerializer, ExchangeRateSerializer

def currency_view(request):

    objects = Currency.objects.all()
    serializer = CurrencySerializer(objects, many=True)
    data = serializers.serialize('json', objects, fields=('code'))
    return JsonResponse(serializer.data, safe=False)

def exchange_rate_view(request, curr1, curr2):
    currency1 = get_object_or_404(Currency, code=curr1)
    currency2 = get_object_or_404(Currency, code=curr2)
    exchange_rates = ExchangeRate.objects.filter(currency1=currency1, currency2=currency2)
    if not exchange_rates.exists():
        return JsonResponse({
            'message': 'No data'
        })

    # exchange_rate = get_object_or_404(ExchangeRate, currency1=currency1, currency2=currency2)
    exchange_rate = exchange_rates.latest('date')
    data = {
        'currency_pair': f'{curr1}{curr2}',
        'exchange_rate': exchange_rate.rate
    }
    return JsonResponse(data)