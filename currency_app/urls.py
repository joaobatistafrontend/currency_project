from django.urls import path
from .views import fetch_and_save_rate

urlpatterns = [
    path("fetch/", fetch_and_save_rate),
]
