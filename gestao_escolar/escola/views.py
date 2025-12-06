from django.shortcuts import render, redirect
from escola.services.alunoservices import AlunoService
from escola.services.cursoservices import CursoService
from escola.services.matriculasservice import MatriculaService
from django.core.exceptions import ValidationError
from django.contrib import messages


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

def deletar_aluno(request, cpf):
    try:
        AlunoService.remover_aluno_por_cpf(cpf)
        messages.success(request, "Aluno removido com sucesso!")
    except ValidationError as e:
        messages.error(request, str(e))

    return redirect("alunos")

def cursos(request):
    busca = request.GET.get("q", "")
    if busca:
        cursos = CursoService.listar_cursos_filtrados(busca)
    else:
        cursos = CursoService.listar_cursos()
    return render(request, "escola/cursos.html", {"cursos": cursos})

def matriculas(request):
    q = request.GET.get("q")
    contexto = {
        "matriculas": MatriculaService.listar_matriculas(q)
    }
    return render(request, "escola/matriculas.html", contexto)

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

def editar_curso(request, id):
    curso = CursoService.obter_curso_por_id(id)

    if request.method == "POST":
        nome = request.POST.get("nome")
        carga_horaria = request.POST.get("carga_horaria")
        valor_inscricao = request.POST.get("valor_inscricao")
        status = request.POST.get("status")

        try:
            CursoService.atualizar_curso(
                id,
                nome=nome,
                carga_horaria=carga_horaria,
                valor_inscricao=valor_inscricao,
                status=status
            )

            messages.success(request, "Curso atualizado com sucesso!")
            return redirect("cursos")

        except ValidationError as e:
            messages.error(request, str(e))

    return render(request, "escola/editar_curso.html", {"curso": curso})
    
def deletar_curso(request, id):
    try:
        CursoService.remover_curso(id)
        messages.success(request, "Curso deletado com sucesso!")
    except ValidationError as e:
        messages.error(request, str(e))

    return redirect("cursos")

def cadastrar_matricula(request):
    if request.method == "POST":
        aluno_id = request.POST.get("aluno")
        curso_id = request.POST.get("curso")
        data_matricula = request.POST.get("data_matricula")
        status = request.POST.get("status", "PENDENTE")

        MatriculaService.criar_matricula(aluno_id, curso_id, data_matricula, status)

        return render(request, "escola/cadastrar_matricula.html", {
            "mensagem": "Matrícula cadastrada com sucesso!",
            "alunos": AlunoService.listar_alunos(),
            "cursos": CursoService.listar_cursos(),
        })

    return render(request, "escola/cadastrar_matricula.html", {
        "alunos": AlunoService.listar_alunos(),
        "cursos": CursoService.listar_cursos(),
    })

def editar_matricula(request, id):
    matricula = MatriculaService.obter_matricula(id)

    if request.method == "POST":
        MatriculaService.editar_matricula(id, request.POST)
        return redirect("matriculas")

    return render(request, "escola/editar_matricula.html", {
        "matricula": matricula,
        "alunos": Aluno.objects.all(),
        "cursos": Curso.objects.all(),
    })

def deletar_matricula(request, id):
    MatriculaService.deletar_matricula(id)
    return redirect("matriculas")