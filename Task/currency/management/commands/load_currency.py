from django.core.management.base import BaseCommand
import yfinance as yf

from currency.models import Currency, ExchangeRate

class Command(BaseCommand):

    def handle(self, *args, **options):
        codes = ['EUR', 'USD', 'JPY', 'PLN']
        for code in codes:
            Currency.objects.get_or_create(code=code)
    
        currencies = ["EURUSD=X", "USDJPY=X", "PLNUSD=X"]
        for currency in currencies:
            data = yf.download(currency, interval='1d', period='1y')
            currency1 = Currency.objects.get(code=currency[:3])
            currency2 = Currency.objects.get(code=currency[3:6])
            if not data.empty:
                for date, row in data.iterrows():
                    currency_date = date.date()
                    exchange_rate = row['Close'].iloc[-1]
                    ExchangeRate.objects.get_or_create(
                        currency1=currency1,
                        currency2=currency2,
                        rate=float(exchange_rate),
                        date=currency_date
                    )
            else:
                print('Data not loaded')
