from django.db import models

class CurrencyRate(models.Model):
    base_currency = models.CharField(max_length=10)
    target_currency = models.CharField(max_length=10)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.base_currency} → {self.target_currency} = {self.rate}"
