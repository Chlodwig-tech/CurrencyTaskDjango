from django.urls import path
from .views import currency_view, exchange_rate_view

urlpatterns = [
    path('', currency_view, name='currency_view'),
    path('<str:curr1>/<str:curr2>/', exchange_rate_view, name='exchange_rate_view'),
]