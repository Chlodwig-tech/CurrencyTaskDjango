from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        return self.code
    
class ExchangeRate(models.Model):
    currency1 = models.ForeignKey(Currency, related_name='currency1', on_delete=models.CASCADE)
    currency2 = models.ForeignKey(Currency, related_name='currency2', on_delete=models.CASCADE)
    rate      = models.FloatField()
    date      = models.DateTimeField()

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        return f'{self.currency1}-{self.currency2}: {self.rate} ({self.date})'