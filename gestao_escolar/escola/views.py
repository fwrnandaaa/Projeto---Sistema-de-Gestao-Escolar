from django.shortcuts import render, redirect
from escola.services.alunoservices import AlunoService
from escola.services.cursoservices import CursoService
from django.core.exceptions import ValidationError
from django.contrib import messages

#TODO: Verificar o motivo da imagem do header sumir quando está na página de editar usuário

def home(request):
    contexto = AlunoService.obter_dados_home()
    return render(request, 'escola/home.html', contexto)

def alunos(request):
    lista = AlunoService.listar_alunos()
    busca = request.GET.get('q')
    if busca:
        lista = lista.filter(nome__icontains=busca)
    return render(request, 'escola/alunos.html', {
        'alunos': lista
    })
def editar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.email = request.POST.get('email')
        aluno.cpf = request.POST.get('cpf')
        aluno.save()

        return render(request, 'escola/editar_aluno.html', {
            'aluno': aluno,
            'mensagem': 'Dados atualizados com sucesso!'
        })

    return render(request, 'escola/editar_aluno.html', {
        'aluno': aluno
    })
def cadastrar_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        try:
            AlunoService.criar_aluno(nome, email, cpf)
            return render(request, 'escola/cadastrar_aluno.html', {
                'mensagem': 'Aluno cadastrado com sucesso!'
            })
        except ValidationError as e:
            return render(request, 'escola/cadastrar_aluno.html', {
                'mensagem': e.message
            })

    return render(request, 'escola/cadastrar_aluno.html')

def editar_aluno(request, cpf):
    aluno = AlunoService.obter_aluno_por_cpf(cpf)

    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")

        try:
            AlunoService.atualizar_aluno_por_cpf(cpf, nome=nome, email=email)
            messages.success(request, "Aluno atualizado com sucesso!")
            return redirect("alunos")

        except ValidationError as e:
            messages.error(request, str(e))

    return render(request, "escola/editar_aluno.html", {"aluno": aluno})

def deletar_aluno(request, cpf):
    try:
        AlunoService.remover_aluno_por_cpf(cpf)
        messages.success(request, "Aluno removido com sucesso!")
    except ValidationError as e:
        messages.error(request, str(e))

    return redirect("alunos")





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