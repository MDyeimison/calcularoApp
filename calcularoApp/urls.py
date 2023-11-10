from django.urls import path

from calcularoApp.views import CalculateView, DigitalView, AnalogicaView

urlpatterns = [
    path('calcularo/<str:val1>/<str:val2>/<str:op>', CalculateView.as_view(), name='calculadora'),
    path('calcularo/digital', DigitalView.as_view(), name='calculadoraApp'),
    path('calcularo/analogica', AnalogicaView.as_view(), name='calculadoraApp'),
]