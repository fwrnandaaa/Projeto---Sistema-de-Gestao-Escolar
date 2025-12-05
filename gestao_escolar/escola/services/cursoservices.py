from escola.models import Curso
from django.core.exceptions import ValidationError

class CursoService:

    @staticmethod
    def listar_cursos():
        return Curso.objects.order_by('nome')

    @staticmethod
    def criar_curso(nome, carga_horaria, valor_inscricao, status='ATIVO'):
        if Curso.objects.filter(nome=nome).exists():
            raise ValidationError("Já existe um curso com esse nome.")

        curso = Curso(
            nome=nome,
            carga_horaria=carga_horaria,
            valor_inscricao=valor_inscricao,
            status=status
        )

        curso.save()
        return curso
        
    @staticmethod
    def listar_cursos_filtrados(texto):
        return Curso.objects.filter(nome__icontains=texto).order_by("nome")

    @staticmethod
    def obter_curso_por_id(id):
        return Curso.objects.get(id=id)

    @staticmethod
    def atualizar_curso(id, nome=None, carga_horaria=None, valor_inscricao=None, status=None):
        curso = Curso.objects.get(id=id)

        if nome: curso.nome = nome
        if carga_horaria: curso.carga_horaria = carga_horaria
        if valor_inscricao: curso.valor_inscricao = valor_inscricao
        if status: curso.status = status

        curso.save()
        return curso

    @staticmethod
    def remover_curso(id):
        curso = Curso.objects.get(id=id)
        curso.delete()
        return True