from django.db import models

OPERACOES = [
    ("ad", "Adição"),
    ("sub", "Subtração"),
    ("mult", "Multiplicação"),
    ("div", "Divisão"),
    ("exp", "Exponenciação"),
]

class Calculadora(models.Model):
    num1 = models.CharField("Primeiro Valor", max_length=50)
    num2 = models.CharField("Segundo Valor", max_length=50)
    op = models.CharField("Tipo de operação", max_length=50, choices=OPERACOES)
    result = models.CharField("Resultado", max_length=50)
    log = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    def __str__(self):
        operacao = self.op
        if operacao == 'ad':
            operacao = '+'
        elif operacao == 'sub':
            operacao = '-'
        elif operacao == 'mult':
            operacao = 'x'
        elif operacao == 'div':
            operacao = '/'
        elif operacao == 'exp':
            operacao = '^'
        return f'{self.num1} {operacao} {self.num2} = {self.result}'