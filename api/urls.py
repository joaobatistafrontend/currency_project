from django.urls import path
from .views import RateListAPIView

urlpatterns = [
    path("rates/", RateListAPIView.as_view()),
]