from rest_framework import generics
from currency_app.models import CurrencyRate
from .serializers import CurrencyRateSerializer



class RateListAPIView(generics.ListAPIView):
    serializer_class = CurrencyRateSerializer

    #filtra o queryset de acordo com parâmetros GET
    def get_queryset(self):
        base = self.request.GET.get("base")
        target = self.request.GET.get("target")

        qs = CurrencyRate.objects.all().order_by("created_at")

        if base:
            qs = qs.filter(base_currency__iexact=base)

        if target:
            qs = qs.filter(target_currency__iexact=target)

        return qs

