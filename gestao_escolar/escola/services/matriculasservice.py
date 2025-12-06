from escola.models import Matricula, Aluno, Curso

class MatriculaService:

    @staticmethod
    def listar_matriculas(matricula=None):
        matriculas = Matricula.objects.select_related("aluno", "curso")
        if matricula:
            matriculas = matriculas.filter(aluno__nome__icontains=matricula) | matriculas.filter(curso__nome__icontains=matricula)
        return matriculas

    @staticmethod
    def criar_matricula(aluno_id, curso_id, data_matricula, status="PENDENTE"):

        aluno = Aluno.objects.get(id=aluno_id)
        curso = Curso.objects.get(id=curso_id)

        return Matricula.objects.create(
            aluno=aluno,
            curso=curso,
            data_matricula=data_matricula,
            status=status
        )

    @staticmethod
    def obter_matricula(id):
        return Matricula.objects.get(id=id)

    @staticmethod
    def editar_matricula(id, dados):
        m = Matricula.objects.get(id=id)
        novo_status = dados.get("status")
        if novo_status not in ["PAGO", "PENDENTE"]:
            raise ValueError("Status inválido.")

        m.status = novo_status
        m.save()

        return m

    @staticmethod
    def deletar_matricula(id):
        Matricula.objects.get(id=id).delete()
