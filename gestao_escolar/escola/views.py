from django.shortcuts import render
from escola.services.alunoservices import AlunoService
from django.core.exceptions import ValidationError


def home(request):
    contexto = AlunoService.obter_dados_home()
    return render(request, 'escola/home.html', contexto)

def alunos(request):
    return render(request, 'escola/alunos.html')

def cursos(request):
    return render(request, 'escola/cursos.html')

def relatorios(request):
    return render(request, 'escola/relatorios.html')

def cadastrar_aluno(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')

        try:
            aluno = AlunoService.criar_aluno(nome, email, cpf)
            return render(request, 'escola/cadastrar_aluno.html', {
                'mensagem': 'Aluno cadastrado com sucesso!'
            })
        except ValidationError as e:
            return render(request, 'escola/cadastrar_aluno.html', {
                'mensagem': str(e)
            })

    return render(request, 'escola/cadastrar_aluno.html')
