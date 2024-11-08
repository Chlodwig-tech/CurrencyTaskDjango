from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Currency, ExchangeRate
# Create your tests here.

class CurrencyExchangeTests(TestCase):
    def setUp(self):
        self.currency_eur = Currency.objects.create(code='EUR')
        self.currency_usd = Currency.objects.create(code='USD')
        self.exchange_rate = ExchangeRate.objects.create(
            currency1=self.currency_eur,
            currency2=self.currency_usd,
            rate=1.034,
            date=timezone.now()
        )
    def test_currency_list(self):
        response = self.client.get(reverse('currency_view'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('EUR', response.content.decode())
        self.assertIn('USD', response.content.decode())
    
    def test_exchange_rate(self):
        response = self.client.get(reverse('exchange_rate_view', args=['EUR', 'USD']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['currency_pair'], 'EURUSD')
        self.assertEqual(response.json()['exchange_rate'], 1.034)

class CurrencyExchangeEmptyListTests(TestCase):
    def setUp(self):
        self.currency_eur = Currency.objects.create(code='EUR')
        self.currency_usd = Currency.objects.create(code='USD')

    def test_currency_empty_list(self):
        response = self.client.get(reverse('exchange_rate_view', args=['EUR', 'USD']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'No data')
    
class CurrencyExchangeListTests(TestCase):
    def setUp(self):
        now = timezone.now()
        self.x = 10
        self.currency_eur = Currency.objects.create(code='EUR')
        self.currency_usd = Currency.objects.create(code='USD')
        self.exchange_rates = [
            ExchangeRate.objects.create(
                currency1=self.currency_eur,
                currency2=self.currency_usd,
                rate=float(i ** 2),
                date=now + timedelta(minutes=(i + 1) * 2)
            )
            for i in range(self.x)
        ]

    def test_exchange_rate(self):
        response = self.client.get(reverse('exchange_rate_view', args=['EUR', 'USD']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['currency_pair'], 'EURUSD')
        rate = (self.x - 1) ** 2
        self.assertEqual(response.json()['exchange_rate'], rate)
        