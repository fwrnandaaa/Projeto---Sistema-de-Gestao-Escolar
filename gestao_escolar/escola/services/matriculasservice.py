from escola.models import Matricula, Aluno, Curso

class MatriculaService:

    @staticmethod
    def listar_matriculas(q=None):
        qs = Matricula.objects.select_related("aluno", "curso")

        if q:
            qs = qs.filter(aluno__nome__icontains=q) | qs.filter(curso__nome__icontains=q)

        return qs

    @staticmethod
    def criar_matricula(aluno_id, curso_id, data_matricula, status="PENDENTE"):
        aluno = Aluno.objects.get(id=aluno_id)
        curso = Curso.objects.get(id=curso_id)

        Matricula.objects.create(
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
        m.aluno_id = dados["aluno"]
        m.curso_id = dados["curso"]
        m.status = dados["status"]
        m.save()
        return m

    @staticmethod
    def deletar_matricula(id):
        Matricula.objects.get(id=id).delete()
