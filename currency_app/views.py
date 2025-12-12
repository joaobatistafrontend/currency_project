from django.http import JsonResponse
from .services import get_currency_rate
from .models import CurrencyRate

def fetch_and_save_rate(request):
    base = request.GET.get("base", "USD") #se não passar moeda, usa USD
    target = request.GET.get("target", "EUR")

    data = get_currency_rate(base, target)
    #se serviço retornar erro → devolve JSON de erro
    if "error" in data:
        return JsonResponse({"error": data["error"]}, status=400)

    #apenas a taxa em si
    rate = data["rate"]

    #salva no banco
    item = CurrencyRate.objects.create(
        base_currency=base,
        target_currency=target,
        rate=rate
    )

    return JsonResponse({
        "message": "Taxa salva com sucesso",
        "rate": rate,
        "id": item.id
    })
