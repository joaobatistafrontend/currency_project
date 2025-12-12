from django.shortcuts import render
import requests
from django.views.generic import TemplateView, ListView
from currency_app.models import CurrencyRate

class HomeView(TemplateView):
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        base = request.POST.get("base")
        target = request.POST.get("target")

        url = f"http://127.0.0.1:8000/currency/fetch/?base={base}&target={target}"
        response = requests.get(url).json()

        rate = response.get("rate")

        context = self.get_context_data(
            rate=rate,
            base=base,
            target=target
        )
        return self.render_to_response(context)

class CurrencyListView(ListView):
    model = CurrencyRate
    template_name = "currency_list.html"
    context_object_name = "rates"
    ordering = ["-created_at"]
    paginate_by = 15
