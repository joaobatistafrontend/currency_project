from rest_framework import serializers
from currency_app.models import CurrencyRate

class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = "__all__"
#converte objetos do banco → JSON