from django.shortcuts import render
from escola.services.alunoservices import AlunoService

def home(request):
    contexto = AlunoService.obter_dados_home()
    return render(request, 'escola/home.html', contexto)

def alunos(request):
    return render(request, 'escola/alunos.html')

def cursos(request):
    return render(request, 'escola/cursos.html')

def relatorios(request):
    return render(request, 'escola/relatorios.html')
