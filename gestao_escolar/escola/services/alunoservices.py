from escola.models import Aluno, Curso, Matricula
from django.core.exceptions import ValidationError
from escola.models import Aluno, Curso, Matricula

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
    @staticmethod
    def criar_aluno(nome, email, cpf):  

        if Aluno.objects.filter(email=email).exists():  
            raise ValidationError("Já existe um aluno com esse e-mail.")
        aluno = Aluno(nome=nome, email=email, cpf=cpf) 
        aluno.save()
        return aluno
    @staticmethod
    def obter_aluno_por_cpf(cpf):
        return Aluno.objects.get(cpf=cpf)

    @staticmethod
    def atualizar_aluno_por_cpf(cpf, nome=None, email=None):
        aluno = Aluno.objects.get(cpf=cpf)

        if email and Aluno.objects.filter(email=email).exclude(cpf=cpf).exists():
            raise ValidationError("Já existe outro aluno com esse e-mail.")

        if nome:
            aluno.nome = nome
        if email:
            aluno.email = email

        aluno.save()
        return aluno

    @staticmethod
    def remover_aluno_por_cpf(cpf):
        aluno = Aluno.objects.get(cpf=cpf)
        aluno.delete()
        return True