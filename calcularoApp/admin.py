from django.contrib import admin
from .models import Calculadora

# Register your models here.

class CalculadoraAdmin(admin.ModelAdmin):
    list_display = ('num1', 'num2', 'op', 'result', 'log')
    search_fields = ['num1', 'num2']
    list_filter = ['op']
    readonly_fields = ['result', 'log']

admin.site.register(Calculadora, CalculadoraAdmin)