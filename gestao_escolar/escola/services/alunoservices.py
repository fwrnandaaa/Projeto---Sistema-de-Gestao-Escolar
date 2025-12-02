from escola.models import Aluno, Curso, Matricula
from django.core.exceptions import ValidationError

class AlunoService:

    @staticmethod
    def listar_alunos():
        return Aluno.objects.order_by('nome')