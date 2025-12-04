from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Aluno
from ..serializers import AlunoSerializer, MatriculaSerializer

class AlunoList(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlunoDetail(APIView):
    def get(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlunoMatriculas(APIView):
    def get(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        matriculas = aluno.matriculas.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)


class AlunoTotalDevido(APIView):
    def get(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        pendentes = aluno.matriculas.filter(status='PENDENTE')
        total = sum(m.curso.valor_inscricao for m in pendentes)

        return Response({
            "aluno": aluno.nome,
            "total_devido": float(total)
        })
