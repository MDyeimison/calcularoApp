from django.urls import path

from calcularoApp.views import CalculateView

urlpatterns = [
    path('calcularo/<str:val1>/<str:val2>/<str:op>', CalculateView.as_view(), name='calculadora'),
]