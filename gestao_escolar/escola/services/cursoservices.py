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
