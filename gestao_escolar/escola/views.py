from django.shortcuts import render
from escola.services.alunoservices import AlunoService
from escola.services.cursoservices import CursoService
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

def cadastrar_curso(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        carga_horaria = request.POST.get('carga_horaria')
        valor_inscricao = request.POST.get('valor_inscricao')
        status = request.POST.get('status', 'ATIVO')

        try:
            carga_horaria = int(carga_horaria)
            valor_inscricao = float(valor_inscricao)

            CursoService.criar_curso(nome, carga_horaria, valor_inscricao, status)
            return render(request, 'escola/cadastrar_curso.html', {
                'mensagem': 'Curso cadastrado com sucesso!'
            })

        except ValidationError as e:
            return render(request, 'escola/cadastrar_curso.html', {
                'mensagem': str(e)
            })
        except ValueError:
            return render(request, 'escola/cadastrar_curso.html', {
                'mensagem': 'Valores de carga horária ou valor da inscrição inválidos.'
            })

    return render(request, 'escola/cadastrar_curso.html')