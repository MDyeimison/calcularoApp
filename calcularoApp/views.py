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
        result = 0

        if op == 'ad':
            result = val1+val2
        elif op == 'sub':
            result = val1-val2
        elif op == 'mult':
            result = val1*val2
        elif op == 'div':
            if val2 != 0:
                result = float(val1/val2)
        elif op == 'exp':
            result = val1**val2
            
        obj = Calculadora(
            num1 = val1,
            num2 = val2,
            op = op,
            result = result,
        )
        obj.save()

        print(f'{val1} {op} {val2} = {result}')
        return JsonResponse({"resultado":result})
    
    
class DigitalView(TemplateView):
    template_name = "calcularoApp/index.html"
    
class AnalogicaView(TemplateView):
    template_name = "calcularoApp/analogica.html"