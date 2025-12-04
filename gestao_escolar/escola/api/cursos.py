from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from escola.models import Curso, Matricula
from escola.serializers import CursoSerializer, MatriculaSerializer

class CursoList(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class CursoDetail(APIView):
    def get(self, request, pk):
        curso = Curso.objects.get(pk=pk)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk):
        curso = Curso.objects.get(pk=pk)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        curso = Curso.objects.get(pk=pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CursoTotalMatriculas(APIView):
    def get(self, request, pk):
        curso = Curso.objects.get(pk=pk)
        total = curso.matriculas.count()
        return Response({"curso": curso.nome, "total_matriculas": total})
