from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from calcularoApp.models import Calculadora

# Create your views here.
class CalculateView(TemplateView):
    model = Calculadora

    def get(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        val1 = float(kwargs['val1'])
        val2 = float(kwargs['val2'])
        op = kwargs['op']

        if op == 'ad':
            result = val1+val2
        elif op == 'sub':
            result = val1-val2
        elif op == 'mult':
            result = val1*val2
        elif op == 'div':
            result = float(val1/val2)
        elif op == 'exp':
            result = val1**val2

        print(f'{val1} {op} {val2} = {result}')
        return JsonResponse({"resultado":result})