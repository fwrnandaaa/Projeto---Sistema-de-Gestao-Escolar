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
        aluno = Aluno(nome=nome, email=email, cpf=cpf)

        try:
            aluno.full_clean()  
            aluno.save()
            return aluno

        except ValidationError as e:
            raise e

        except Exception as e:
            raise ValidationError(f"Erro inesperado ao criar aluno: {str(e)}")
    @staticmethod
    def obter_aluno_por_id(id):
        return Aluno.objects.get(id=id)

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
    @staticmethod
    def editar_aluno(id, nome, email, cpf):

        aluno = Aluno.objects.get(id=id)

        aluno.nome = nome
        aluno.email = email
        aluno.cpf = cpf

        try:
            aluno.full_clean()    # validações do modelo
            aluno.save()
            return aluno

        except ValidationError as e:
            raise e

        except Exception as e:
            raise ValidationError(f"Erro inesperado ao atualizar aluno: {str(e)}")
