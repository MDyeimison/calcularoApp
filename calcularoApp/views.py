from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class CalculateView(TemplateView):
    # model = Calculadora

    # def get(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     periodo = TermoCompromissoPeriodo.objects.get(id=kwargs['duplicados'])
    #     termoPeriodo = periodo.termo
    #     termos = TermoCompromisso.objects.filter(aluno__pessoa__nomeCompleto=termoPeriodo.aluno.pessoa.nomeCompleto, semestre=termoPeriodo.semestre, disciplina=termoPeriodo.disciplina).order_by('dataCadastro')
    #     periodos = [termo.retornaUltimoPeriodo() for termo in termos]
    #     termosDuplicados = [p.termo for p in periodos if p.podeSerExcluido()!=None]
    #     pessoa = periodo.termo.aluno.pessoa.nomeCompleto
    #     tcesList = []
    #     for termo in termosDuplicados:
    #         termoDisplay = str(termo._get_FIELD_display.__self__)
    #         numero = str(termo.numero)
    #         dados = {
    #             "id":termo.id,
    #             "termo":termoDisplay,
    #             "numero":f'{numero[:5]}.{numero[5:]}',
    #             "nome":pessoa,
    #             "dataCadastro":termo.dataCadastro.strftime("%d/%m/%Y"),
    #             "quemCadastrou": termo.quemCadastrou.nomeCompleto if termo.quemCadastrou else '',
    #         }
    #         tcesList.append(dados)
    #     data = {"nome":pessoa, "termos":tcesList}
    #     return JsonResponse(data)