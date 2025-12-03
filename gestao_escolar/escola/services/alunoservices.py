from escola.models import Aluno, Curso, Matricula
from django.core.exceptions import ValidationError

class AlunoService:

    @staticmethod
    def listar_alunos():
        return Aluno.objects.order_by('nome')
    
    @staticmethod
    def obter_dados_home():
        total_cursos = Curso.objects.count()
        total_alunos = Aluno.objects.count()
        total_matriculas_pagas = Matricula.objects.filter(status='PAGO').count()
        total_pendentes = Matricula.objects.filter(status='PENDENTE').count()
        
        return {
            'total_cursos': total_cursos,
            'total_alunos': total_alunos,
            'total_matriculas_pagas': total_matriculas_pagas,
            'total_pendentes': total_pendentes,
        }