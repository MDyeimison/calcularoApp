from django.urls import path

urlpatterns = [
    path('calcularo/', Calculate.as_view(), name='calculadora'),
]