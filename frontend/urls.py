from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("rates/", CurrencyListView.as_view(), name="rate_list"),

]
