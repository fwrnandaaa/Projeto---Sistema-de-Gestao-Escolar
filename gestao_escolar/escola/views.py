from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer
from escola.services.alunoservices import AlunoService


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    
    @action(detail=True, methods=['get'])
    def matriculas(self, request, pk=None ):
        aluno = self.get_object()
        matriculas = aluno.matriculas.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def total_devido(self, request, pk=None):
        aluno = self.get_object()
        matriculas_pendentes = aluno.matriculas.filter(status='PENDENTE')

        total = sum(m.curso.valor_inscricao for m in matriculas_pendentes)

        return Response({
            "aluno": aluno.nome,
            "total_devido": float(total)
        })


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(detail=True, methods=['get'])
    def total_matriculas(self, request, pk=None):
        curso = self.get_object()
        total = curso.matriculas.count()
        return Response({"curso": curso.nome, "total_matriculas": total})


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    @action(detail=True, methods=['post'])
    def pagar(self, request, pk=None):
        matricula = self.get_object()
        matricula.status = 'PAGO'
        matricula.save()
        return Response({'status': 'Matrícula marcada como paga'})
    
    @action(detail=False, methods=['get'])
    def pendencias(self, request):
        pendentes = Matricula.objects.filter(status='PENDENTE')
        total = sum(m.curso.valor_inscricao for m in pendentes)

        return Response({
            "total_matriculas_pendentes": pendentes.count(),
            "valor_total_pendente": float(total)
        })
    
def home(request):
    return render(request, 'escola/base.html')

def listar_alunos(request):
    alunos = AlunoService.listar_alunos()
    context={'alunos':alunos}
    return(request, 'escola/listar_alunos.html', context)